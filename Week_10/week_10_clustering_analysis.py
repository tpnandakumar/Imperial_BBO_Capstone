"""Exploratory clustering analysis for BBO Week 10.

Uses only observations available through Week 10. Week 11 outputs are never read.
Clustering is a decision-support analysis, not evidence of a global optimum.
"""
from pathlib import Path
import csv
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Week_10" / "week_10_cluster_summary.csv"
DIMS = {1:2, 2:2, 3:3, 4:4, 5:4, 6:5, 7:6, 8:8}


def week_dir(w):
    return ROOT / f"Week_{w:02d}"


def locate(folder, candidates):
    for name in candidates:
        p = folder / name
        if p.exists():
            return p
    return None


def parse_vector(text):
    text = text.strip().replace("-", ",")
    return np.array([float(x.strip()) for x in text.split(",") if x.strip()], dtype=float)


def read_week(w):
    folder = week_dir(w)
    inp = locate(folder, [f"week_{w:02d}_inputs.csv", f"week_{w}_inputs.csv"])
    res = locate(folder, [f"week_{w:02d}_results.csv", f"week_{w}_results.csv"])
    if not inp or not res:
        return {}
    xs, ys = {}, {}
    with inp.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            fn = int(''.join(c for c in row["Function"] if c.isdigit()))
            xs[fn] = parse_vector(row["Input"])
    with res.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            fn = int(''.join(c for c in row["Function"] if c.isdigit()))
            ys[fn] = float(row["Output"])
    return {fn:(xs[fn], ys[fn]) for fn in xs.keys() & ys.keys()}


def pairwise_distances(X):
    return np.sqrt(((X[:,None,:] - X[None,:,:])**2).sum(axis=2))


def kmeans(X, k, seed=42, max_iter=200):
    rng = np.random.default_rng(seed)
    centres = X[rng.choice(len(X), size=k, replace=False)].copy()
    labels = np.zeros(len(X), dtype=int)
    for _ in range(max_iter):
        d = ((X[:,None,:] - centres[None,:,:])**2).sum(axis=2)
        new_labels = d.argmin(axis=1)
        if np.array_equal(new_labels, labels) and _ > 0:
            break
        labels = new_labels
        for j in range(k):
            pts = X[labels == j]
            if len(pts): centres[j] = pts.mean(axis=0)
    inertia = float(((X - centres[labels])**2).sum())
    return labels, centres, inertia


def silhouette(X, labels):
    D = pairwise_distances(X)
    vals = []
    for i in range(len(X)):
        same = np.where(labels == labels[i])[0]
        same = same[same != i]
        if len(same) == 0:
            vals.append(0.0); continue
        a = D[i, same].mean()
        bs = []
        for lab in np.unique(labels):
            if lab == labels[i]: continue
            idx = np.where(labels == lab)[0]
            if len(idx): bs.append(D[i, idx].mean())
        b = min(bs) if bs else a
        vals.append((b-a)/max(a,b) if max(a,b) else 0.0)
    return float(np.mean(vals))


def main():
    history = {fn:[] for fn in DIMS}
    for w in range(1, 11):
        for fn, (x,y) in read_week(w).items():
            if len(x) != DIMS[fn]:
                raise ValueError(f"Week {w} Function {fn}: expected {DIMS[fn]} dimensions, got {len(x)}")
            if np.any((x < 0) | (x > 1)):
                raise ValueError(f"Week {w} Function {fn}: input outside [0,1]")
            history[fn].append((w,x,y))

    rows=[]
    for fn, obs in history.items():
        if len(obs) < 3:
            continue
        weeks=np.array([o[0] for o in obs]); X=np.vstack([o[1] for o in obs]); y=np.array([o[2] for o in obs])
        D=pairwise_distances(X); np.fill_diagonal(D, np.inf)
        nn=D.min(axis=1); nn_idx=D.argmin(axis=1)
        candidates=[]
        for k in range(2, min(4, len(X)-1)+1):
            labels, centres, inertia=kmeans(X,k)
            if len(np.unique(labels)) == k:
                candidates.append((silhouette(X,labels),k,labels,inertia))
        if candidates:
            score,k,labels,inertia=max(candidates,key=lambda z:z[0])
        else:
            k,labels,score,inertia=1,np.zeros(len(X),dtype=int),math.nan,float(((X-X.mean(axis=0))**2).sum())
        ranks=(-y).argsort().argsort()+1
        for i,(w,x,out) in enumerate(obs):
            rows.append({
                "Function":fn,"Week":w,"Output":repr(float(out)),"Output_rank_within_function":int(ranks[i]),
                "Cluster":int(labels[i])+1,"Selected_k":k,"Silhouette":("" if math.isnan(score) else f"{score:.6f}"),
                "Nearest_neighbour_week":int(weeks[nn_idx[i]]),"Nearest_neighbour_distance":f"{nn[i]:.8f}",
                "Input":"-".join(f"{v:.6f}" for v in x)
            })
    fields=["Function","Week","Input","Output","Output_rank_within_function","Cluster","Selected_k","Silhouette","Nearest_neighbour_week","Nearest_neighbour_distance"]
    with OUT.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader(); writer.writerows(rows)
    print(f"Wrote {len(rows)} observation rows to {OUT}")
    print("Interpret clusters cautiously: ten observations per function are sparse, especially in higher dimensions.")

if __name__ == "__main__":
    main()

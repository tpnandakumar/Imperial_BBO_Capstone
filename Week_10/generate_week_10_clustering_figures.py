"""Generate Week 10 clustering figures from exact Weeks 1 to 10 BBO history.

Week 11 outputs are deliberately excluded. Week 11 query decisions are shown only
as downstream decisions informed by Week 10 evidence.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

OUTDIR = Path(__file__).resolve().parent

INPUTS = [
[[0.74,0.74],[0.72,0.94],[0.53,0.64,0.25],[0.6,0.43,0.42,0.25],[0.21,0.87,0.9,0.9],[0.75,0.18,0.7,0.72,0.04],[0.05,0.5,0.25,0.22,0.42,0.74],[0.06,0.07,0.03,0.04,0.41,0.82,0.5,0.91]],
[[0.3,0.3],[0.76,0.9],[0.75,0.25,0.75],[0.2,0.8,0.8,0.8],[0.18,0.9,0.95,0.95],[0.25,0.75,0.3,0.3,0.8],[0.08,0.55,0.3,0.25,0.45,0.78],[0.08,0.08,0.05,0.05,0.45,0.85,0.55,0.95]],
[[0.6,0.6],[0.8,0.92],[0.2,0.8,0.2],[0.8,0.2,0.2,0.2],[0.17,0.92,0.97,0.97],[0.7,0.2,0.7,0.7,0.2],[0.1,0.58,0.32,0.27,0.47,0.8],[0.04,0.04,0.04,0.04,0.47,0.88,0.58,0.97]],
[[0.7,0.7],[0.68,0.96],[0.85,0.15,0.85],[0.9,0.1,0.1,0.1],[0.16,0.94,0.98,0.98],[0.8,0.15,0.8,0.8,0.15],[0.06,0.52,0.28,0.24,0.44,0.76],[0.07,0.07,0.05,0.05,0.44,0.84,0.54,0.94]],
[[0.45,0.45],[0.64,0.98],[0.9,0.1,0.9],[0.95,0.05,0.05,0.05],[0.15,0.96,0.99,0.99],[0.9,0.1,0.9,0.9,0.1],[0.04,0.48,0.26,0.22,0.42,0.74],[0.06,0.06,0.05,0.05,0.43,0.85,0.55,0.95]],
[[0.5,0.5],[0.7,0.95],[0.95,0.05,0.95],[0.98,0.02,0.02,0.02],[0.14,0.97,0.995,0.995],[0.95,0.05,0.95,0.95,0.05],[0.05,0.5,0.25,0.2,0.4,0.75],[0.05,0.05,0.05,0.05,0.45,0.85,0.55,0.95]],
[[0.35,0.7],[0.76,0.985],[0.25,0.85,0.3],[0.3,0.7,0.65,0.25],[0.12,0.99,0.999,0.999],[0.25,0.75,0.25,0.8,0.3],[0.05,0.52,0.24,0.18,0.41,0.77],[0.05,0.05,0.05,0.05,0.46,0.86,0.56,0.98]],
[[0.35,0.7],[0.72,0.94],[0.26,0.86,0.29],[0.32,0.72,0.68,0.22],[0.12,0.995,0.9995,0.9995],[0.24,0.76,0.24,0.82,0.28],[0.06,0.5,0.25,0.22,0.42,0.74],[0.05,0.05,0.05,0.05,0.47,0.87,0.57,0.98]],
[[0.35,0.7],[0.725,0.945],[0.255,0.855,0.295],[0.31,0.71,0.67,0.23],[0.12,0.997,0.9998,0.9998],[0.24,0.76,0.24,0.82,0.28],[0.058,0.495,0.248,0.218,0.425,0.742],[0.05,0.05,0.05,0.05,0.468,0.872,0.572,0.982]],
[[0.45,0.65],[0.7,0.955],[0.28,0.875,0.315],[0.29,0.73,0.69,0.21],[0.12,0.997,0.9998,0.9998],[0.26,0.78,0.26,0.84,0.3],[0.06,0.5,0.25,0.22,0.43,0.74],[0.05,0.05,0.05,0.05,0.47,0.875,0.575,0.985]]
]

OUTPUTS = np.array([
[6.854713532414845e-19,0.45494185399727516,-0.10183633971746164,-4.359874926582439,1415.8763939603884,-0.7001549808025808,1.3199939052019112,9.58024],
[6.659572754640724e-23,0.41213721316888097,-0.1332555781557258,-23.120154471959825,2308.1487028593933,-2.0702463923015775,1.0696579739950232,9.5241],
[0.025559285339829783,0.14098828808535324,-0.12787021171886992,-14.554028542475695,2840.9903787629305,-0.648848297397347,0.8966026942687082,9.44296],
[1.4754580129542488e-07,0.5228458934672892,-0.06037987403160633,-22.55187651826871,3238.333368768757,-0.8733671274789931,1.1968303712356705,9.53944],
[0.012779642669914939,0.28016822307722516,-0.11392206377710448,-27.44051496086922,3682.2110623386798,-1.073875453695542,1.3809299933612855,9.5113],
[2.6752879910742468e-09,0.5712475315739602,-0.3071823694141529,-31.20347777578016,3922.7652233497042,-1.3792272680368016,1.3529491169887171,9.5148],
[-1.4546199699251391e-58,0.2399291698606551,-0.09116928906376276,-10.745961383135121,4278.816638076986,-1.119713499832813,1.1543358123792982,9.49476],
[-1.4546199699251391e-58,0.5672775862793291,-0.0991107637427902,-12.305008897187289,4359.384134322703,-1.1197178425911847,1.3346391663186332,9.47621],
[-1.4546199699251391e-58,0.47297842839949866,-0.1156707106126581,-11.788939969158545,4394.868042481448,-1.1733030029888645,1.314307996450604,9.4709436],
[2.8950706668499033e-23,0.5311818841205426,-0.08697581687486715,-13.483642655031158,4394.868042481448,-1.2283806967341901,1.285160161342515,9.4646525]
], dtype=float)

STRATEGIES = [
"Exploit narrow peak","Local trust-region probe","Local refinement","Local recovery probe",
"Boundary-directed probe","Best-basin recovery","Tight trust-region refinement","Exploit confirmed best"
]


def build_summary():
    rows=[]
    for f in range(8):
        X=np.array([INPUTS[w][f] for w in range(10)],dtype=float)
        y=OUTPUTS[:,f]
        best_i=int(np.argmax(y)); norm=np.sqrt(X.shape[1])
        d_best=np.linalg.norm(X[-1]-X[best_i])/norm
        D=np.sqrt(((X[:,None,:]-X[None,:,:])**2).sum(axis=2))/norm
        np.fill_diagonal(D,np.inf)
        nn10=float(D[-1].min())
        candidates=[]
        for k in (2,3):
            km=KMeans(n_clusters=k,random_state=42,n_init=50).fit(X)
            candidates.append((silhouette_score(X,km.labels_),k,km.labels_))
        sil,k,labels=max(candidates,key=lambda z:z[0])
        rows.append({"Function":f"F{f+1}","Dimensions":X.shape[1],"Selected_k":k,
                     "Silhouette":sil,"Best_week":best_i+1,"Week10_output":y[-1],
                     "W10_to_best_norm_distance":d_best,"W10_nearest_neighbour_distance":nn10,
                     "W10_same_cluster_as_best":bool(labels[-1]==labels[best_i]),
                     "Week11_strategy":STRATEGIES[f]})
    return pd.DataFrame(rows)


def main():
    summary=build_summary()
    summary.to_csv(OUTDIR/"week_10_clustering_figure_source.csv",index=False)

    fig,ax=plt.subplots(figsize=(11,6.5))
    x=np.arange(1,9); bars=ax.bar(x,summary["Silhouette"])
    ax.set_xticks(x,summary["Function"]); ax.set_xlabel("Function"); ax.set_ylabel("Silhouette score")
    ax.set_title("Figure 1. Exploratory Cluster Separation by Function, Weeks 1 to 10")
    ax.grid(axis="y",alpha=0.25)
    for b,k,d in zip(bars,summary["Selected_k"],summary["Dimensions"]):
        ax.text(b.get_x()+b.get_width()/2,b.get_height()+0.015,f"k={int(k)}\n{int(d)}D",ha="center",va="bottom",fontsize=9)
    fig.tight_layout(); fig.savefig(OUTDIR/"week_10_clustering_figure_1_cluster_separation.png",dpi=300,bbox_inches="tight"); plt.close(fig)

    X5=np.array([INPUTS[w][4] for w in range(10)],dtype=float); y5=OUTPUTS[:,4]
    dist=np.linalg.norm(X5-X5[-1],axis=1)/np.sqrt(X5.shape[1])
    sizes=80+260*(y5-y5.min())/(y5.max()-y5.min())
    fig,ax=plt.subplots(figsize=(11,6.5)); ax.scatter(dist,y5,s=sizes,alpha=0.8)
    for w,(dx,yy) in enumerate(zip(dist,y5),1): ax.annotate(f"W{w}",(dx,yy),xytext=(5,5),textcoords="offset points",fontsize=9)
    ax.set_xlabel("Normalised Euclidean distance from the Week 10 Function 5 query"); ax.set_ylabel("Function 5 output")
    ax.set_title("Figure 2. Function 5 High-Value Cluster Tightens Near the Week 10 Boundary Region"); ax.grid(alpha=0.25)
    fig.tight_layout(); fig.savefig(OUTDIR/"week_10_clustering_figure_2_function5_cluster.png",dpi=300,bbox_inches="tight"); plt.close(fig)

    t=summary[["Function","Best_week","Week10_output","W10_to_best_norm_distance","W10_nearest_neighbour_distance","W10_same_cluster_as_best","Week11_strategy"]].copy()
    t["Week10_output"]=t["Week10_output"].map(lambda v:f"{v:.6g}")
    t["W10_to_best_norm_distance"]=t["W10_to_best_norm_distance"].map(lambda v:f"{v:.3f}")
    t["W10_nearest_neighbour_distance"]=t["W10_nearest_neighbour_distance"].map(lambda v:f"{v:.3f}")
    t["W10_same_cluster_as_best"]=t["W10_same_cluster_as_best"].map({True:"Yes",False:"No"})
    t.columns=["Function","Best week","Week 10 output","W10 to best norm. distance","W10 nearest neighbour","Same cluster as best","Week 11 decision"]
    fig,ax=plt.subplots(figsize=(14,6.5)); ax.axis("off")
    tab=ax.table(cellText=t.values,colLabels=t.columns,cellLoc="center",colLoc="center",loc="center",colWidths=[0.07,0.08,0.12,0.14,0.12,0.10,0.29])
    tab.auto_set_font_size(False); tab.set_fontsize(9); tab.scale(1,1.8)
    ax.set_title("Figure 3. Week 10 Cluster Evidence and the Week 11 Query Decision",pad=18,fontsize=15)
    fig.tight_layout(); fig.savefig(OUTDIR/"week_10_clustering_figure_3_decision_evidence.png",dpi=300,bbox_inches="tight"); plt.close(fig)

    print("Week 10 clustering figures generated. Week 11 outputs were not used.")

if __name__ == "__main__":
    main()

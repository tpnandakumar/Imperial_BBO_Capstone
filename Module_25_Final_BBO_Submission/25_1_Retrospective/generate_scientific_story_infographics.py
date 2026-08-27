from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from scipy.interpolate import griddata


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
OUT = HERE / "scientific_story_infographics"
NAVY, BLUE, TEAL, GREEN = "#101D42", "#2457A7", "#258A8A", "#367E48"
GOLD, RED, PURPLE = "#D99B24", "#BD3B2B", "#7650A8"
INK, MUTED, PALE, GRID = "#172033", "#58657A", "#F5F7FB", "#D9E1EC"
FC = [TEAL, PURPLE, RED, BLUE, GOLD, "#986523", GREEN, "#4569B2"]


def save(fig, n, slug):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"Story_{n:02d}_{slug}.jpg"
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    temp = path.with_suffix(".tmp.jpg")
    with Image.open(path) as im:
        im.convert("RGB").save(temp, "JPEG", quality=87, optimize=True, progressive=True)
    temp.replace(path)
    return path


def frame(n, title, subtitle, evidence, interpretation, limitation, caption):
    fig = plt.figure(figsize=(14, 8), facecolor="white")
    bg = fig.add_axes([0, 0, 1, 1]); bg.axis("off")
    bg.add_patch(plt.Rectangle((.025,.885),.95,.09,color=NAVY,transform=bg.transAxes))
    bg.text(.048,.943,f"STORY {n:02d}",color=GOLD,weight="bold",fontsize=11,va="center",transform=bg.transAxes)
    bg.text(.145,.943,title,color="white",weight="bold",fontsize=21,va="center",transform=bg.transAxes)
    bg.text(.048,.904,subtitle,color="#DCE5F4",fontsize=10.2,va="center",transform=bg.transAxes)
    boxes=[("EVIDENCE",evidence,GREEN,"#F1F8F2"),("INTERPRETATION",interpretation,BLUE,"#F1F5FC"),("LIMITATION",limitation,RED,"#FCF3F1")]
    for i,(h,b,c,fill) in enumerate(boxes):
        y=.61-i*.205
        bg.add_patch(plt.Rectangle((.69,y),.26,.175,facecolor=fill,edgecolor=c,lw=1.3,transform=bg.transAxes))
        bg.text(.705,y+.14,h,color=c,weight="bold",fontsize=9.2,transform=bg.transAxes)
        bg.text(.705,y+.115,textwrap.fill(b,42),color=INK,fontsize=8.6,va="top",linespacing=1.18,transform=bg.transAxes)
    bg.plot([.05,.95],[.105,.105],color=GRID,lw=1,transform=bg.transAxes)
    bg.text(.05,.072,f"Figure S{n:02d}. {caption}",fontsize=8.5,color=MUTED,va="center",transform=bg.transAxes)
    bg.text(.95,.034,"Verified source: course starter arrays and BBO portal returns",fontsize=7.3,color=MUTED,ha="right",transform=bg.transAxes)
    ax=fig.add_axes([.065,.17,.575,.67])
    return fig,bg,ax


def axis_style(ax, xlabel=None, ylabel=None):
    ax.grid(alpha=.20,color="#9CAAC0"); ax.spines[["top","right"]].set_visible(False)
    ax.tick_params(labelsize=8,colors=MUTED)
    if xlabel: ax.set_xlabel(xlabel,fontsize=8.5,color=MUTED)
    if ylabel: ax.set_ylabel(ylabel,fontsize=8.5,color=MUTED)


def add_metric_strip(bg, metrics):
    n=len(metrics); w=.60/n
    for i,(v,l,c) in enumerate(metrics):
        x=.065+i*w
        bg.add_patch(plt.Rectangle((x,.805),w-.012,.055,facecolor=PALE,edgecolor=c,lw=1.1,transform=bg.transAxes))
        bg.text(x+(w-.012)/2,.838,v,ha="center",va="center",weight="bold",fontsize=11,color=c,transform=bg.transAxes)
        bg.text(x+(w-.012)/2,.817,l.upper(),ha="center",va="center",fontsize=6.4,color=MUTED,transform=bg.transAxes)


def landscape(n, f, data, dims):
    g=data[data.function.eq(f)].copy().reset_index(drop=True)
    cols=[f"x{i}" for i in range(1,dims[f]+1)]
    X=g[cols].to_numpy(float); y=g.output.to_numpy(float)
    variances=np.var(X,axis=0); chosen=np.argsort(variances)[-2:]
    a,b=sorted(chosen.tolist())
    best=int(np.argmax(y)); worst=int(np.argmin(y)); centre=X[best].copy()
    projected=pd.DataFrame({"a":X[:,a],"b":X[:,b],"y":y}).groupby(["a","b"],as_index=False).y.mean()
    grid=np.linspace(0,1,100); xx,yy=np.meshgrid(grid,grid)
    pred=griddata(projected[["a","b"]].values,projected.y.values,(xx,yy),method="linear")
    title=f"F{f}: response landscape and observed extrema"
    subtitle=f"Gaussian-process slice through x{a+1} and x{b+1}; remaining coordinates held at the best observed design"
    fig,bg,ax=frame(n,title,subtitle,
        f"All {len(g)} observations are fitted. The observed maximum is {y[best]:.10g}; the observed minimum is {y[worst]:.10g}.",
        f"The field shows measured-response interpolation across the two most variable sampled coordinates, x{a+1} and x{b+1}.",
        "Interpolation is confined to the sampled projection. Other coordinates vary in functions above 2D, so the display is not the hidden surface.",
        f"F{f} projected response landscape with all measured points, observed maximum and observed minimum.")
    if f % 2:
        cf=ax.contourf(xx,yy,pred,levels=22,cmap="terrain")
        ax.contour(xx,yy,pred,levels=10,colors="white",linewidths=.35,alpha=.55)
        ax.scatter(X[:,a],X[:,b],c=y,cmap="terrain",edgecolor="black",s=28,lw=.35,zorder=4)
        ax.scatter(X[best,a],X[best,b],marker="*",s=260,c=GOLD,edgecolor="black",lw=.9,zorder=6,label="Observed maximum")
        ax.scatter(X[worst,a],X[worst,b],marker="X",s=115,c=RED,edgecolor="white",lw=.8,zorder=6,label="Observed minimum")
        ax.set_xlim(0,1); ax.set_ylim(0,1); axis_style(ax,f"x{a+1}",f"x{b+1}"); ax.legend(loc="upper right",fontsize=7.5,framealpha=.9)
        cbar=fig.colorbar(cf,ax=ax,fraction=.035,pad=.02); cbar.set_label("Interpolated output",fontsize=7.5); cbar.ax.tick_params(labelsize=7)
    else:
        pos=ax.get_position(); ax.remove(); ax=fig.add_axes(pos,projection="3d")
        surf=ax.plot_surface(xx,yy,pred,cmap="terrain",linewidth=0,antialiased=True,alpha=.92)
        ax.scatter(X[:,a],X[:,b],y,c=y,cmap="terrain",edgecolor="black",s=22,depthshade=False)
        ax.scatter(X[best,a],X[best,b],y[best],marker="*",s=180,c=GOLD,edgecolor="black",label="Observed maximum")
        ax.scatter(X[worst,a],X[worst,b],y[worst],marker="X",s=80,c=RED,edgecolor="white",label="Observed minimum")
        ax.set_xlabel(f"x{a+1}",fontsize=8); ax.set_ylabel(f"x{b+1}",fontsize=8); ax.set_zlabel("Output",fontsize=8); ax.tick_params(labelsize=7); ax.view_init(28,-128); ax.legend(loc="upper right",fontsize=7)
        cbar=fig.colorbar(surf,ax=ax,fraction=.035,pad=.05); cbar.set_label("Interpolated output",fontsize=7.5); cbar.ax.tick_params(labelsize=7)
    add_metric_strip(bg,[(f"{dims[f]}D","dimension",BLUE),(f"{len(g)}","total observations",TEAL),(f"{y[best]:.6g}","observed max",GREEN),(f"{y[worst]:.6g}","observed min",RED)])
    return save(fig,n,f"f{f}_landscape")


def generate():
    data=pd.read_csv(DATA); weekly=data[data.source.str.match(r"week_\d+",na=False)].copy(); weekly["week"]=weekly.source.str.extract(r"(\d+)").astype(int)
    dims={f:int(data[data.function.eq(f)][[f"x{i}" for i in range(1,9)]].notna().sum(axis=1).max()) for f in range(1,9)}
    paths=[]

    fig,bg,ax=frame(1,"The complete experimental landscape","Unequal dimensions and starter sample sizes shaped the difficulty of the eight searches",
        "The verified dataset contains 175 starter observations and 104 prospective portal evaluations.",
        "Higher-dimensional functions began with more points, but the 13-query allowance remained identical for every function.",
        "Observation count does not measure coverage uniformly because volume grows rapidly with dimension.",
        "Starter evidence, dimensionality and query budget across all eight black-box functions.")
    counts=data[data.source.eq("starter")].groupby("function").size().reindex(range(1,9)); x=np.arange(8)
    ax.bar(x-.18,counts,.36,color=FC,label="Starter observations"); ax.bar(x+.18,[13]*8,.36,color=GOLD,label="Weekly queries")
    ax.set_xticks(x,[f"F{i}\n{dims[i]}D" for i in range(1,9)]); axis_style(ax,"Function and dimension","Observations"); ax.legend(fontsize=8,frameon=False)
    add_metric_strip(bg,[("175","starter",BLUE),("104","queries",PURPLE),("279","total observations",GREEN),("2D to 8D","input space",GOLD)])
    paths.append(save(fig,1,"experimental_landscape"))

    fig,bg,ax=frame(2,"Thirteen rounds, eight different trajectories","All weekly returns are shown on a within-function normalised scale",
        "The panel contains all 104 portal returns, with each function normalised only against its own observed weekly range.",
        "The common scale reveals timing of improvement, recovery and plateau without comparing incompatible objective magnitudes.",
        "Normalisation shows trajectory shape, not absolute performance or distance from an unknown global optimum.",
        "Complete weekly optimisation histories for F1 to F8, scaled within function for visual comparison.")
    for f in range(1,9):
        g=weekly[weekly.function.eq(f)].sort_values("week"); lo,hi=g.output.min(),g.output.max(); z=(g.output-lo)/(hi-lo) if hi>lo else np.ones(len(g))
        ax.plot(g.week,z,marker="o",ms=3,lw=1.8,color=FC[f-1],label=f"F{f}")
    ax.set_xticks(range(1,14)); axis_style(ax,"Week","Within-function normalised output"); ax.legend(ncol=4,fontsize=7.5,frameon=False)
    add_metric_strip(bg,[("104","returns",BLUE),("13","rounds",PURPLE),("8","functions",TEAL),("100%","history retained",GREEN)])
    paths.append(save(fig,2,"weekly_trajectories"))

    fig,bg,ax=frame(3,"When new maxima were found","A heatmap records whether each weekly query exceeded all earlier weekly returns",
        "A coloured cell marks a new within-function weekly record; blank cells did not exceed the previous best.",
        "F5 improved repeatedly, while several functions depended on early winners and later recovery.",
        "Record frequency does not measure the size or statistical reliability of each gain.",
        "Weekly record-setting events reveal where optimisation advanced and where it plateaued.")
    hit=np.zeros((8,13))
    for f in range(1,9):
        best=-np.inf
        for _,r in weekly[weekly.function.eq(f)].sort_values("week").iterrows():
            if r.output>best: hit[f-1,int(r.week)-1]=1; best=r.output
    ax.imshow(hit,aspect="auto",cmap="YlGn",vmin=0,vmax=1); ax.set_xticks(range(13),range(1,14)); ax.set_yticks(range(8),[f"F{i}" for i in range(1,9)])
    ax.set_xlabel("Week",fontsize=8.5); ax.set_ylabel("Function",fontsize=8.5); ax.tick_params(labelsize=8)
    add_metric_strip(bg,[(str(int(hit.sum())),"weekly records",GREEN),(str(int(hit[:,1:].sum())),"records after W1",TEAL),("12","F5 records",GOLD),("3","Week 13 records",PURPLE)])
    paths.append(save(fig,3,"record_heatmap"))

    fig,bg,ax=frame(4,"Observed maxima and minima","The empirical range differs sharply across functions and must be interpreted on its own scale",
        "Maximum and minimum are calculated from all 279 verified observations, including starter and weekly data.",
        "The signed log display makes eight unequal objective scales visible without pretending they are directly comparable.",
        "These are observed extrema only. The hidden global maxima and minima remain unknown.",
        "Observed maxima, minima and empirical ranges across the complete verified dataset.")
    ex=data.groupby("function").output.agg(["min","max"]); y=np.arange(8)
    signed=lambda v:np.sign(v)*np.log10(1+np.abs(v)); lo=signed(ex["min"].values); hi=signed(ex["max"].values)
    for i in range(8): ax.plot([lo[i],hi[i]],[i,i],color=GRID,lw=5); ax.scatter(lo[i],i,c=RED,s=55); ax.scatter(hi[i],i,c=GREEN,s=70,marker="*")
    ax.set_yticks(y,[f"F{i}" for i in range(1,9)]); ax.invert_yaxis(); axis_style(ax,"Signed log10(1 + |output|)","Function")
    add_metric_strip(bg,[("279","observations",BLUE),("8","empirical ranges",PURPLE),("★","observed maximum",GREEN),("●","observed minimum",RED)])
    paths.append(save(fig,4,"observed_extrema"))

    for f in range(1,9): paths.append(landscape(4+f,f,data,dims))

    fig,bg,ax=frame(13,"How far each query moved","L1 movement heatmap shows the transition from broad probing to local refinement and repetition",
        "Each cell is the L1 distance between consecutive weekly coordinates for one function.",
        "Movement contracted selectively rather than uniformly; zero movement records deliberate repeats or retention.",
        "Equal L1 movement can represent different geometry in 2D and 8D spaces.",
        "Function-by-week movement magnitude documents the changing exploration and exploitation balance.")
    move=np.zeros((8,12))
    for f in range(1,9):
        cols=[f"x{i}" for i in range(1,dims[f]+1)]; g=weekly[weekly.function.eq(f)].sort_values("week"); X=g[cols].values
        move[f-1]=np.abs(np.diff(X,axis=0)).sum(axis=1)
    im=ax.imshow(move,aspect="auto",cmap="magma"); ax.set_xticks(range(12),range(2,14)); ax.set_yticks(range(8),[f"F{i}" for i in range(1,9)]); ax.set_xlabel("Destination week",fontsize=8.5); ax.set_ylabel("Function",fontsize=8.5); ax.tick_params(labelsize=8)
    fig.colorbar(im,ax=ax,fraction=.035,pad=.02,label="L1 movement")
    add_metric_strip(bg,[(f"{move.max():.3f}","largest move",RED),(str(int((move==0).sum())),"zero moves",BLUE),("12","transitions",PURPLE),("8","functions",TEAL)])
    paths.append(save(fig,13,"movement_heatmap"))

    fig,bg,ax=frame(14,"Boundary proximity across the campaign","Minimum distance to any coordinate boundary is tracked for every submitted query",
        "A small value means at least one coordinate was close to 0 or 1; F5 progressively approached a productive boundary region.",
        "Boundary proximity complements output history by showing where the search concentrated geometrically.",
        "Distance to a boundary does not establish whether the true optimum lies on that boundary.",
        "Weekly boundary-distance heatmap identifies edge-seeking, interior search and repeated boundary designs.")
    bd=np.zeros((8,13))
    for f in range(1,9):
        cols=[f"x{i}" for i in range(1,dims[f]+1)]; X=weekly[weekly.function.eq(f)].sort_values("week")[cols].values
        bd[f-1]=np.minimum(X,1-X).min(axis=1)
    im=ax.imshow(bd,aspect="auto",cmap="viridis_r"); ax.set_xticks(range(13),range(1,14)); ax.set_yticks(range(8),[f"F{i}" for i in range(1,9)]); ax.set_xlabel("Week",fontsize=8.5); ax.set_ylabel("Function",fontsize=8.5); ax.tick_params(labelsize=8)
    fig.colorbar(im,ax=ax,fraction=.035,pad=.02,label="Minimum boundary distance")
    add_metric_strip(bg,[(f"{bd.min():.6f}","closest boundary",GOLD),(f"{np.median(bd):.3f}","median distance",TEAL),("104","queries",BLUE)])
    paths.append(save(fig,14,"boundary_heatmap"))

    fig,bg,ax=frame(15,"Week 10 cluster separation","Silhouette scores compare k=2 and k=3 for every function using fixed, reproducible settings",
        "K-means used n_init=50 and random_state=42. Bars show the measured silhouette score for each candidate k.",
        "The comparison tests partition stability in the sampled query path and supports function-specific interpretation.",
        "Clusters may reflect adaptive sampling and do not prove natural groups in the hidden objective surface.",
        "Measured clustering validation across all eight functions and both prespecified cluster counts.")
    h=pd.read_csv(ROOT/"BBO_Dashboard"/"hpo_results"/"week10_clustering_hpo_all_results.csv"); x=np.arange(8)
    for off,k,c in [(-.18,2,TEAL),(.18,3,PURPLE)]:
        v=h[h.clusters.eq(k)].copy(); v["f"]=v.function.str.extract(r"(\d+)").astype(int); v=v.sort_values("f"); ax.bar(x+off,v.silhouette_score,.36,color=c,label=f"k={k}")
    ax.set_xticks(x,[f"F{i}" for i in range(1,9)]); ax.set_ylim(0,1); axis_style(ax,"Function","Silhouette score"); ax.legend(fontsize=8,frameon=False)
    add_metric_strip(bg,[("2 or 3","candidate k",PURPLE),("50","initialisations",BLUE),("42","random seed",TEAL),(f"{h.silhouette_score.max():.3f}","highest silhouette",GREEN)])
    paths.append(save(fig,15,"clustering_validation"))

    fig,bg,ax=frame(16,"PCA variance concentration","The first principal component quantifies how strongly each sampled path followed one dominant direction",
        "PCA is calculated from the 13 submitted coordinates for each function after centring.",
        "High PC1 variance indicates concentrated movement and helps identify where coordinate changes were redundant or coupled.",
        "PCA describes the path selected by the optimiser, not sensitivity of the hidden reward surface.",
        "Explained variance of the first principal component across all eight weekly query paths.")
    ev=[]
    for f in range(1,9):
        cols=[f"x{i}" for i in range(1,dims[f]+1)]; X=weekly[weekly.function.eq(f)][cols].values; X=X-X.mean(0); s=np.linalg.svd(X,compute_uv=False); ev.append(100*s[0]**2/(s*s).sum())
    ax.bar([f"F{i}" for i in range(1,9)],ev,color=FC); ax.set_ylim(0,100); axis_style(ax,"Function","PC1 explained variance (%)")
    add_metric_strip(bg,[(f"{max(ev):.1f}%","highest PC1",GREEN),(f"{min(ev):.1f}%","lowest PC1",PURPLE),("13","queries per PCA",BLUE),("8","paths",TEAL)])
    paths.append(save(fig,16,"pca_variance"))

    fig,bg,ax=frame(17,"Week 13 reward test","The final action is evaluated by its exact change from the Week 12 portal return",
        "F3, F5 and F6 improved; F2 declined; F1, F4, F7 and F8 were unchanged after retention or repetition.",
        "The mixed result shows why identical action labels cannot be assumed to produce identical outcomes.",
        "Raw changes span incompatible scales, so bars are normalised by each function's observed weekly range.",
        "Normalised Week 13 reward changes provide a common view of the final prospective experiment.")
    delta=[]
    for f in range(1,9):
        g=weekly[weekly.function.eq(f)].sort_values("week"); r=g.output.max()-g.output.min(); delta.append((g.iloc[-1].output-g.iloc[-2].output)/(r or 1))
    ax.bar([f"F{i}" for i in range(1,9)],delta,color=[GREEN if v>0 else RED if v<0 else BLUE for v in delta]); ax.axhline(0,color=INK,lw=.8); axis_style(ax,"Function","Week 13 change / weekly observed range")
    add_metric_strip(bg,[("3","improved",GREEN),("1","declined",RED),("4","unchanged",BLUE),("8","prospective tests",PURPLE)])
    paths.append(save(fig,17,"week13_reward"))

    fig,bg,ax=frame(18,"Repeatability of identical coordinates","Repeated-coordinate groups are compared by whether their returned outputs agreed exactly",
        "F1, F4, F7 and F8 reproduced winning outputs exactly, while F6 returned different values at one identical coordinate.",
        "Repeat evaluation distinguishes confirmation from unresolved measurement or process variation.",
        "A small number of repeats cannot estimate a full noise distribution.",
        "Repeatability audit separates identical-output confirmations from variable repeated evaluations.")
    repeat=[]; variable=[]
    for f in range(1,9):
        cols=[f"x{i}" for i in range(1,dims[f]+1)]; g=weekly[weekly.function.eq(f)].copy(); key=g[cols].round(12).astype(str).agg("|".join,axis=1); q=g.assign(key=key).groupby("key").output.agg(["count","nunique"])
        repeat.append(int((q["count"]>1).sum())); variable.append(int(((q["count"]>1)&(q["nunique"]>1)).sum()))
    x=np.arange(8); ax.bar(x-.18,repeat,.36,color=BLUE,label="Repeated-coordinate groups"); ax.bar(x+.18,variable,.36,color=RED,label="Variable-output groups"); ax.set_xticks(x,[f"F{i}" for i in range(1,9)]); axis_style(ax,"Function","Number of groups"); ax.legend(fontsize=8,frameon=False)
    add_metric_strip(bg,[(str(sum(repeat)),"repeat groups",BLUE),(str(sum(variable)),"variable groups",RED),("4","exact winning repeats",GREEN),("1","F6 warning",GOLD)])
    paths.append(save(fig,18,"repeatability"))

    fig,bg,ax=frame(19,"What worked and what did not","Final evidence is organised by measured outcome rather than by the sophistication of the method",
        "Sustained F5 improvement, exact recovery and three Week 13 gains are contrasted with F2 overshoot and F6 variability.",
        "Function-specific policies and provenance influenced decisions more directly than any single analytical model.",
        "Outcome attribution remains limited because only one prospective query was available per function each round.",
        "Measured strengths, deviations and unresolved questions from the complete optimisation history.")
    labels=["F5 gain","Recovered winners","W13 gains","F2 final loss","F6 repeat range"]
    values=[3025.080822638365,4,3,0.0921821158135095,0.100675388230716]
    display=np.log10(1+np.array(values)); ax.barh(labels,display,color=[GREEN,BLUE,TEAL,RED,GOLD]); ax.invert_yaxis(); axis_style(ax,"log10(1 + measured magnitude or count)",None)
    for i,v in enumerate(values): ax.text(display[i]+.02,i,f"{v:.6g}",va="center",fontsize=8,color=INK)
    add_metric_strip(bg,[("3025.081","F5 gain",GREEN),("4","recovered winners",BLUE),("0.092182","F2 final loss",RED),("0.100675","F6 repeat range",GOLD)])
    paths.append(save(fig,19,"worked_failed"))

    fig,bg,ax=frame(20,"The stopping and continuation map","Final function status is derived from improvement, confirmation and repeatability evidence",
        "F1, F4, F7 and F8 had confirmed winners; F2 and F3 required local testing; F5 remained productive; F6 required repeatability work.",
        "Separating optimisation, confirmation and measurement investigation prevents unproductive routine movement.",
        "The map is specific to the observed 13-round history and would change if new evidence became available.",
        "Evidence-based final status for every function after the Week 13 portal return.")
    status=[0,1,1,0,2,3,0,0]; cmap=plt.matplotlib.colors.ListedColormap([BLUE,PURPLE,GOLD,RED]); im=ax.imshow(np.array(status)[None,:],aspect="auto",cmap=cmap,vmin=0,vmax=3)
    ax.set_xticks(range(8),[f"F{i}" for i in range(1,9)]); ax.set_yticks([]); ax.set_xlabel("Function",fontsize=8.5)
    for i,s in enumerate(status): ax.text(i,0,["STOP","LOCAL","BOUNDARY","REPEAT"][s],ha="center",va="center",color="white",weight="bold",fontsize=8)
    add_metric_strip(bg,[("4","stop",BLUE),("2","local tests",PURPLE),("1","boundary test",GOLD),("1","repeatability study",RED)])
    paths.append(save(fig,20,"stopping_map"))
    return paths


if __name__ == "__main__":
    for p in generate(): print(p)

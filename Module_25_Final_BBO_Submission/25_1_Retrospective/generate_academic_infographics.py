from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "academic_infographics"
DATA = ROOT / "BBO_Dashboard/data/complete_internal_evidence.csv"
HPO_C = ROOT / "BBO_Dashboard/hpo_results/week10_clustering_hpo_all_results.csv"
HPO_S = ROOT / "BBO_Dashboard/hpo_results/posthoc_surrogate_hpo_all_results.csv"
RL = ROOT / "Week_13/RL_DECISION_EXPERIMENT/outputs/rl_week13_policy_results.csv"
W13 = ROOT / "Week_13/week_13_analysis_summary.csv"

sns.set_theme(style="whitegrid", context="notebook")
NAVY, BLUE, TEAL, GOLD, RED, GREY = "#17324D", "#2E6F9E", "#2A9D8F", "#E9A23B", "#C84A4A", "#667788"

CAPTIONS = {
1:"The starter sample increased with dimensionality, but the prospective budget remained one portal evaluation per function per week.",
2:"The method changed after each batch of eight outputs. The sequence distinguishes analytical additions from the decision they supported.",
3:"Standardisation exposes direction and volatility without allowing F5's much larger numerical scale to dominate the comparison.",
4:"A plateau indicates that later queries did not exceed the previous best. It does not establish convergence to the global optimum.",
5:"The sampled F1 path revisited a narrow productive region. The scatter represents evaluated points, not a reconstructed response surface.",
6:"F2 improved late but the Week 13 local movement crossed away from the Week 12 best, demonstrating local sensitivity.",
7:"The final three-coordinate change was small and produced a new best. Coordinate traces provide the direct retrospective evidence.",
8:"Exploration below the Week 1 result was followed by explicit recovery and exact confirmation of the earlier winner.",
9:"F5 provided the clearest repeatable exploitation signal. The association is empirical and confined to the evaluated path.",
10:"Three rewards at an identical five-dimensional coordinate show that F6 cannot be interpreted as a stable deterministic response from these data alone.",
11:"The heatmap shows how the six coordinates changed through time and whether objective improvement coincided with a particular movement pattern.",
12:"The eight-dimensional path was sparse relative to the search space. Repeating the early winner was therefore a risk-control decision.",
13:"Large and small movements produced both gains and losses. Step size required function-specific calibration rather than a universal rule.",
14:"Boundary proximity was productive for F5 but not a general property of the other functions. This guards against transferring one function's strategy to another.",
15:"Silhouette score was used as a descriptive separation diagnostic. Small sequential samples mean that cluster labels were not treated as ground truth.",
16:"Hyperparameters were compared by chronological validation, preserving time order. Lower normalised RMSE indicates better out-of-sample prediction on the observed path.",
17:"Explained variance quantifies compression of coordinate movement. PCA describes the sampled trajectory and cannot reveal the unknown objective equation.",
18:"Absolute PC1 loadings identify which coordinates drove the main observed movement direction. They do not measure causal influence on reward.",
19:"The policy assigned retain, local refinement, boundary refinement or repeat actions before Week 13 outputs were known, allowing prospective evaluation.",
20:"The audit links exact movement to the returned change and final status, separating new bests, retained winners and unsuccessful refinement.",
}


def save(fig, n, slug):
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"Figure_{n:02d}_{slug}.jpg"
    fig.subplots_adjust(bottom=0.18)
    fig.text(.06,.035,f"Figure {n}. Interpretation: {CAPTIONS[n]}  Source: Imperial BBO verified project data.",fontsize=8.2,color=GREY,ha="left",va="bottom",wrap=True)
    fig.savefig(p, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    tmp = p.with_suffix(".rgb.jpg")
    with Image.open(p) as im:
        im.convert("RGB").save(tmp, "JPEG", quality=90, optimize=True, progressive=True)
    tmp.replace(p)
    return p


def weekly_data():
    d = pd.read_csv(DATA)
    w = d[d.source.str.match(r"week_\d+")].copy()
    w["week"] = w.source.str.extract(r"(\d+)").astype(int)
    w["F"] = "F" + w.function.astype(str)
    xcols = [f"x{i}" for i in range(1, 9)]
    w["l1_move"] = w.groupby("function")[xcols].diff().abs().sum(axis=1)
    w["change"] = w.groupby("function").output.diff()
    w["boundary_distance"] = w[xcols].apply(lambda r: np.nanmin(np.r_[r.dropna().values, 1-r.dropna().values]), axis=1)
    return d, w


def title(ax, text, subtitle=None):
    ax.set_title(text, loc="left", fontsize=15, fontweight="bold", color=NAVY, pad=12)
    if subtitle:
        ax.text(0, 1.01, subtitle, transform=ax.transAxes, fontsize=9, color=GREY, va="bottom")


def generate():
    d, w = weekly_data()
    figs = []

    # 1. Experimental design
    dims = {1:2,2:2,3:3,4:4,5:4,6:5,7:6,8:8}
    starter = d[d.source.eq("starter")].groupby("function").size()
    fig, ax = plt.subplots(figsize=(10.8,5.7))
    x=np.arange(8); ax.bar(x-0.18, starter.values, .36, label="Starter observations", color=BLUE)
    ax.bar(x+0.18, [13]*8, .36, label="Weekly portal evaluations", color=TEAL)
    ax.set_xticks(x, [f"F{i}\n{dims[i]}D" for i in range(1,9)]); ax.set_ylabel("Number of evaluated points")
    title(ax,"Experimental design and fixed query budget","Eight hidden functions, one new query per function per week")
    ax.legend(frameon=False, ncol=2); figs.append(save(fig,1,"experimental_design"))

    # 2. Week-by-week method and effect matrix
    story=pd.read_csv(ROOT / "BBO_Dashboard/CAPSTONE_WEEK_STORY.csv")
    fig, ax=plt.subplots(figsize=(11.5,7.2)); ax.axis("off")
    rows=[]
    for r in story.itertuples(index=False):
        rows.append([f"W{r.week}",r.focus, str(r.evidence_shown)[:84], str(r.next_decision)[:72]])
    tab=ax.table(cellText=rows,colLabels=["Round","Analytical focus","Returned evidence","Decision for next round"],loc="center",cellLoc="left",colWidths=[.07,.20,.38,.30])
    tab.auto_set_font_size(False); tab.set_fontsize(7.4); tab.scale(1,1.42)
    for (rr,cc),cell in tab.get_celld().items():
        cell.set_edgecolor("#D7E0E8"); cell.set_facecolor(NAVY if rr==0 else ("#F5F8FA" if rr%2==0 else "white")); cell.get_text().set_color("white" if rr==0 else "#263238"); cell.get_text().set_weight("bold" if rr==0 or cc==0 else "normal")
    title(ax,"Week-by-week evolution of the optimisation method","Each analytical change was linked to returned evidence and the following decision")
    figs.append(save(fig,2,"sequential_protocol"))

    # 3. Standardised observed trajectories
    fig, axes=plt.subplots(4,2,figsize=(10.8,8.2),sharex=True)
    for f,ax in zip(range(1,9),axes.flat):
        q=w[w.function.eq(f)].sort_values("week"); z=(q.output-q.output.mean())/(q.output.std() or 1)
        ax.plot(q.week,z,marker="o",ms=3,color=BLUE); ax.axhline(0,color="#BBC5CE",lw=.8)
        ax.set_title(f"F{f}",loc="left",fontsize=10,weight="bold"); ax.set_ylabel("z output",fontsize=8)
    axes[-1,0].set_xlabel("Week"); axes[-1,1].set_xlabel("Week")
    fig.suptitle("Observed weekly output trajectories",x=.07,ha="left",fontsize=15,weight="bold",color=NAVY)
    fig.tight_layout(rect=[0,0,1,.96]); figs.append(save(fig,3,"weekly_output_trajectories"))

    # 4. Normalised best-so-far
    fig,ax=plt.subplots(figsize=(10.8,5.7))
    for f in range(1,9):
        q=w[w.function.eq(f)].sort_values("week"); base=q.output.min(); span=q.output.max()-base or 1
        ax.plot(q.week,(q.output.cummax()-base)/span,label=f"F{f}",lw=1.8)
    ax.set_xlabel("Week"); ax.set_ylabel("Normalised best-so-far"); ax.set_ylim(-.04,1.05)
    title(ax,"Convergence of the best observed value","Normalisation allows functions with different output scales to be compared")
    ax.legend(ncol=4,frameon=False); figs.append(save(fig,4,"normalised_convergence"))

    # 5 and 6 two-dimensional response maps
    for n,f in [(5,1),(6,2)]:
        q=d[d.function.eq(f)].copy(); wk=q.source.str.extract(r"week_(\d+)")[0]
        fig,ax=plt.subplots(figsize=(10.8,5.7)); sc=ax.scatter(q.x1,q.x2,c=q.output,cmap="viridis",s=np.where(q.source.eq("starter"),45,95),edgecolor="white")
        path=q[~q.source.eq("starter")]; ax.plot(path.x1,path.x2,color=RED,lw=1,alpha=.7)
        for _,r in path.iterrows(): ax.text(r.x1,r.x2,str(int(r.sequence)),fontsize=7)
        ax.set(xlabel="x1",ylabel="x2",xlim=(0,1),ylim=(0,1)); title(ax,f"F{f} sampled response map","Colour is returned output; numbered path is Week 1 to Week 13")
        fig.colorbar(sc,ax=ax,label="Output"); figs.append(save(fig,n,f"f{f}_response_map"))

    # 7 F3 coordinate and reward path
    f=3; q=w[w.function.eq(f)].sort_values("week")
    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10.8,6.5),sharex=True,gridspec_kw={"height_ratios":[1,1.2]})
    for c in ["x1","x2","x3"]: ax1.plot(q.week,q[c],marker="o",label=c)
    ax1.set_ylabel("Coordinate value"); ax1.legend(ncol=3,frameon=False)
    ax2.plot(q.week,q.output,marker="o",color=TEAL); ax2.set(xlabel="Week",ylabel="Returned output")
    title(ax1,"F3 local refinement and final improvement","Coordinate movement is shown directly above the objective response")
    figs.append(save(fig,7,"f3_coordinate_reward"))

    # 8 F4 exploration and recovery
    f=4; q=w[w.function.eq(f)].sort_values("week")
    fig,ax=plt.subplots(figsize=(10.8,5.7)); ax.plot(q.week,q.output,marker="o",color=BLUE); best=q.output.max()
    ax.axhline(best,color=TEAL,ls="--",label=f"Best retained {best:.4f}"); ax.fill_between(q.week,q.output,best,color=RED,alpha=.12,label="Loss from best")
    ax.set(xlabel="Week",ylabel="Returned output"); title(ax,"F4 exploration cost and recovery","The Week 1 optimum was recovered in Weeks 12 and 13")
    ax.legend(frameon=False); figs.append(save(fig,8,"f4_recovery"))

    # 9 F5 trajectory plus coordinate evolution
    f=5; q=w[w.function.eq(f)].sort_values("week")
    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10.8,6.8),sharex=True)
    ax1.plot(q.week,q.output,marker="o",color=TEAL,lw=2.3); ax1.set_ylabel("Returned output")
    for c in ["x1","x2","x3","x4"]: ax2.plot(q.week,q[c],marker=".",label=c)
    ax2.set(xlabel="Week",ylabel="Coordinate value",ylim=(-.03,1.03)); ax2.legend(ncol=4,frameon=False)
    title(ax1,"F5 sustained optimisation towards a boundary","Output increased as x1 decreased and x2 to x4 approached one")
    figs.append(save(fig,9,"f5_boundary_trajectory"))

    # 10 F6 repeated coordinate
    f=6; q=w[w.function.eq(f)].sort_values("week"); rep=q[q[["x1","x2","x3","x4","x5"]].round(6).duplicated(keep=False)]
    fig,ax=plt.subplots(figsize=(10.8,5.7)); ax.plot(q.week,q.output,"o-",color=BLUE,alpha=.45,label="All weekly outputs")
    ax.scatter(rep.week,rep.output,s=120,color=RED,label="Repeated coordinate",zorder=5)
    for _,r in rep.iterrows(): ax.annotate(f"W{int(r.week)}: {r.output:.6f}",(r.week,r.output),xytext=(5,8),textcoords="offset points",fontsize=8)
    ax.set(xlabel="Week",ylabel="Returned output"); title(ax,"F6 repeatability diagnostic","Identical coordinates produced different outputs, indicating unresolved variability")
    ax.legend(frameon=False); figs.append(save(fig,10,"f6_repeatability"))

    # 11 F7 and 12 F8 coordinate heatmaps
    for n,f in [(11,7),(12,8)]:
        q=w[w.function.eq(f)].sort_values("week"); X=q[[f"x{i}" for i in range(1,f+0 if f==8 else 7)] if False else [f"x{i}" for i in range(1,{7:7,8:9}[f])]].to_numpy().T
        fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10.8,6.4),sharex=True,gridspec_kw={"height_ratios":[1.5,1]})
        sns.heatmap(X,ax=ax1,cmap="Blues",vmin=0,vmax=1,cbar_kws={"label":"Coordinate value"},yticklabels=[f"x{i}" for i in range(1,X.shape[0]+1)],xticklabels=q.week)
        ax2.plot(q.week,q.output,marker="o",color=TEAL); ax2.set(xlabel="Week",ylabel="Output")
        title(ax1,f"F{f} high-dimensional search path","Coordinate heatmap aligned with the returned objective")
        figs.append(save(fig,n,f"f{f}_coordinate_heatmap"))

    # 13 movement versus reward change
    z=w.dropna(subset=["l1_move","change"]).copy()
    ranges=w.groupby("function").output.agg(lambda s:max(s.max()-s.min(),1e-12))
    z["normalised_change"]=z.apply(lambda r:r.change/ranges.loc[r.function],axis=1)
    fig,ax=plt.subplots(figsize=(10.8,5.7))
    for f,g in z.groupby("function"): ax.scatter(g.l1_move,g.normalised_change,s=45,label=f"F{f}",alpha=.8)
    ax.axhline(0,color="black",lw=.8); ax.set(xlabel="L1 movement from previous query",ylabel="Output change divided by observed function range")
    title(ax,"Movement size did not determine improvement","The sign and scale of response depended on the function and local region")
    ax.legend(ncol=4,frameon=False); figs.append(save(fig,13,"movement_vs_change"))

    # 14 boundary proximity
    fig,ax=plt.subplots(figsize=(10.8,5.7))
    for f,g in w.groupby("function"):
        span=g.output.max()-g.output.min() or 1; yn=(g.output-g.output.min())/span
        ax.scatter(g.boundary_distance,yn,s=42,label=f"F{f}",alpha=.75)
    ax.set(xlabel="Minimum distance of any coordinate from a boundary",ylabel="Within-function normalised output")
    title(ax,"Boundary proximity and objective response","F5 benefited from boundary movement; this relationship did not generalise")
    ax.legend(ncol=4,frameon=False); figs.append(save(fig,14,"boundary_response"))

    # 15 clustering HPO
    h=pd.read_csv(HPO_C)
    fig,ax=plt.subplots(figsize=(10.8,5.7))
    sns.barplot(data=h,x="function",y="silhouette_score",hue="clusters",palette=[BLUE,TEAL],ax=ax)
    ax.set(ylabel="Silhouette score",xlabel="Function"); title(ax,"Week 10 clustering hyperparameter comparison","Higher silhouette indicates stronger separation, but sparse trajectories limit inference")
    ax.legend(title="k",frameon=False); figs.append(save(fig,15,"clustering_hpo"))

    # 16 surrogate HPO heatmap, best per degree/alpha aggregated
    h=pd.read_csv(HPO_S); p=h.pivot_table(index="degree",columns="alpha",values="normalised_rmse",aggfunc="median")
    fig,ax=plt.subplots(figsize=(10.8,5.7)); sns.heatmap(p,annot=True,fmt=".3f",cmap="mako_r",ax=ax,cbar_kws={"label":"Median normalised RMSE"})
    title(ax,"Chronological surrogate hyperparameter validation","Median normalised RMSE across functions; lower is better")
    figs.append(save(fig,16,"surrogate_hpo"))

    # 17 PCA explained variance
    rows=[]
    for f in range(3,9):
        q=w[w.function.eq(f)]; X=q[[c for c in q.columns if c.startswith("x")]].dropna(axis=1).values
        ev=PCA().fit(StandardScaler().fit_transform(X)).explained_variance_ratio_
        rows.append([f,*np.pad(ev[:4],(0,max(0,4-len(ev))),constant_values=np.nan)[:4]])
    pp=pd.DataFrame(rows,columns=["F","PC1","PC2","PC3","PC4"]).set_index("F")
    fig,ax=plt.subplots(figsize=(10.8,5.7)); pp.plot(kind="bar",stacked=True,ax=ax,color=[BLUE,TEAL,GOLD,RED])
    ax.set(xlabel="Function",ylabel="Explained variance ratio",ylim=(0,1)); title(ax,"Week 11 PCA explained variance","PCA summarised the sampled search path, not the hidden objective surface")
    ax.legend(ncol=4,frameon=False); figs.append(save(fig,17,"pca_explained_variance"))

    # 18 PCA loadings
    load=[]
    for f in range(3,9):
        q=w[w.function.eq(f)]; cols=[c for c in q.columns if c.startswith("x") and q[c].notna().all()]
        pc=PCA(n_components=1).fit(StandardScaler().fit_transform(q[cols]))
        row={"F":f}; row.update({c:abs(v) for c,v in zip(cols,pc.components_[0])}); load.append(row)
    ld=pd.DataFrame(load).set_index("F").reindex(columns=[f"x{i}" for i in range(1,9)])
    fig,ax=plt.subplots(figsize=(10.8,5.7)); sns.heatmap(ld,annot=True,fmt=".2f",cmap="YlGnBu",ax=ax,cbar_kws={"label":"Absolute PC1 loading"})
    title(ax,"Coordinate contribution to the first principal component","Large loadings identify coordinates dominating the observed movement path")
    figs.append(save(fig,18,"pca_loadings"))

    # 19 RL policy and outcome
    r=pd.read_csv(RL); r["outcome"]=np.select([r.week13_new_best,r.week13_retained_best],["New best","Best retained"],default="No improvement")
    order=[f"F{i}" for i in range(1,9)]; r.function=pd.Categorical(r.function,order,ordered=True); r=r.sort_values("function")
    r["normalised_outcome"]=(r.week13_reward-r.best_reward_to_week12)/r.reward_range_to_week12.replace(0,np.nan)*100
    r["normalised_outcome"]=r.normalised_outcome.fillna(0)
    fig,ax=plt.subplots(figsize=(10.8,5.7)); colors={"New best":TEAL,"Best retained":BLUE,"No improvement":RED}
    ax.bar(r.function,r.normalised_outcome,color=[colors[x] for x in r.outcome]); ax.axhline(0,color="black",lw=.7)
    for i,row in enumerate(r.itertuples()):
        y=row.normalised_outcome; ax.text(i,y,f"{row.selected_action_label}\n{row.outcome}",ha="center",va="bottom" if y>=0 else "top",fontsize=7)
    ax.set(ylabel="Change from previous best (% of observed reward range)",xlabel="Function"); title(ax,"Week 13 policy action and observed outcome","Normalisation permits comparison across functions with different objective scales")
    figs.append(save(fig,19,"rl_policy_outcome"))

    # 20 final result matrix
    s=pd.read_csv(W13); s["Function"]=s.function.str.replace("Function ","F")
    cols=["Function","week_12_output","week_13_output","exact_change","l1_input_movement","final_status"]
    t=s[cols].copy(); t.columns=["Function","Week 12","Week 13","Change","L1 movement","Final status"]
    fig,ax=plt.subplots(figsize=(11.5,5.8)); ax.axis("off")
    vals=[]
    for row in t.itertuples(index=False): vals.append([row[0],f"{row[1]:.7g}",f"{row[2]:.7g}",f"{row[3]:+.4g}",f"{row[4]:.4g}",row[5]])
    tab=ax.table(cellText=vals,colLabels=t.columns,loc="center",cellLoc="center",colWidths=[.08,.13,.13,.12,.12,.34])
    tab.auto_set_font_size(False); tab.set_fontsize(8.5); tab.scale(1,1.55)
    for (rr,cc),cell in tab.get_celld().items():
        cell.set_edgecolor("#D9E1E8"); cell.set_facecolor(NAVY if rr==0 else "white"); cell.get_text().set_color("white" if rr==0 else "#263238"); cell.get_text().set_weight("bold" if rr==0 else "normal")
    title(ax,"Final-round numerical audit","Exact Week 12 to Week 13 changes and verified decision outcomes")
    figs.append(save(fig,20,"final_numerical_audit"))
    return figs


if __name__ == "__main__":
    for p in generate(): print(p)

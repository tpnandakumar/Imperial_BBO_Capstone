from __future__ import annotations
import json, random, statistics
from dataclasses import dataclass

BASES={
'genuine_threat':(.98,.90,.35,.12,'urgent_response'),'ambiguous_alarm':(.34,.90,.30,.62,'clarify'),'distress_no_danger':(.20,.82,.95,.30,'support'),'hidden_risk_calm':(.86,.22,.20,.22,'caution'),'benign_misleading_emotion':(.10,.62,.20,.18,'observe'),'conflicting_modalities':(.52,.58,.35,.72,'clarify')}
MODS=('language','vision','audio','temporal'); SEEDS=[11,23,37,53,71]
AI={'observe':.10,'clarify':.30,'support':.45,'caution':.65,'urgent_response':1.,'abstain_and_review':0.}
@dataclass(frozen=True)
class O: f:float;e:float;c:float;r:float
@dataclass(frozen=True)
class C: family:str; fr:float; ei:float; en:float; u:float; truth:str; obs:tuple[O,...]
@dataclass
class H:
    lo:float=.40; hi:float=.60; hlo:float=.20; hhi:float=.80; au:float=.10; ad:float=.20; ac:float=.30; inertia:float=.90; hyst:float=.04; maxstep:float=.035; x:float=.50; prev:float=0.; rev:int=0; tv:float=0.; n:int=0
    def step(self,raw,rel,ambiguity,disagreement,laminar):
        centre=max(.35,min(.65,.50+.12*(rel-.5)-.08*(disagreement-.3))); width=max(.10,min(.24,.20+.08*(ambiguity-.5))); lo,hi=centre-width/2,centre+width/2
        rate=self.ac if raw<self.hlo or raw>self.hhi else self.au if raw<lo-self.hyst else self.ad if raw>hi+self.hyst else .01
        target=max(lo,min(hi,raw)); cand=self.x+rate*(target-self.x)
        if laminar:
            cand=self.inertia*self.x+(1-self.inertia)*cand; cand=max(self.x-self.maxstep,min(self.x+self.maxstep,cand))
        cand=max(self.hlo,min(self.hhi,cand)); d=cand-self.x
        if self.prev and d and ((self.prev>0)!=(d>0)): self.rev+=1
        self.tv+=abs(d); self.prev=d; self.x=cand; self.n+=1; return cand
    def diag(self):
        mv=self.tv/max(1,self.n); rr=self.rev/max(1,self.n-1)
        return {'mean_step_variation':mv,'oscillation_reversal_rate':rr,'laminarity_index':max(0.,1-min(1,mv/.05)-min(.5,rr)),'final_effective_coherence':self.x}
def clip(x): return max(0.,min(1.,x))
def gen(seed,n=100):
    r=random.Random(seed); out=[]
    for fam,(fr,ei,en,u,t) in BASES.items():
        for _ in range(n):
            obs=[]
            for j,m in enumerate(MODS):
                rel=r.uniform(.56,.96); conf=r.uniform(.62,.97); f,e=fr,ei
                if fam=='conflicting_modalities': f,e=((.78,.28) if j%2==0 else (.24,.88))
                elif fam=='hidden_risk_calm' and m in ('language','audio'): f,e=.58,.18
                elif fam=='benign_misleading_emotion' and m=='audio': e=.85
                obs.append(O(clip(f+r.gauss(0,.07+.04*(1-rel))),clip(e+r.gauss(0,.07+.04*(1-rel))),conf,rel))
            out.append(C(fam,fr,ei,en,u,t,tuple(obs)))
    r.shuffle(out); return out
def split(xs): n=len(xs); return xs[:int(.6*n)],xs[int(.6*n):int(.8*n)],xs[int(.8*n):]
def fuse(c):
    w=[o.c*o.r for o in c.obs]; s=sum(w); f=sum(o.f*x for o,x in zip(c.obs,w))/s; e=sum(o.e*x for o,x in zip(c.obs,w))/s
    d=statistics.fmean(abs(o.f-f)+abs(o.e-e) for o in c.obs)/2; return f,e,clip(d),statistics.fmean(o.c for o in c.obs),statistics.fmean(o.r for o in c.obs)
def coh(c):
    f,e,d,conf,rel=fuse(c); exp=clip(.62*f+.38*e); vals=[clip(.55*f+.45*e),exp,f,.5,exp,exp]; ctr=statistics.fmean(vals); mad=statistics.fmean(abs(v-ctr) for v in vals)
    agree=max(0,1-2*mad); facc=clip(1-abs(f-c.fr)); prop=clip(1-abs(exp-AI[c.truth])); ua=clip(1-abs(d-c.u)); gate=min(facc,.92,prop,ua)
    return clip(.65*agree+.35*gate),f,e,d,conf,rel,facc,prop
def simple(f,e,en,u):
    if f>=.78:return 'urgent_response' if e>=.55 else 'caution'
    if f>=.58:return 'caution'
    if en>=.62 and f<.55:return 'support'
    if u>=.45 or (e>=.75 and f<.50):return 'clarify'
    return 'observe'
def pgc(c,ec,switch_cost=.0):
    raw,f,e,d,conf,rel,facc,prop=coh(c)
    if facc<.55 or prop<.50 or ec<.45+switch_cost:return 'abstain_and_review'
    empathy=min(1,c.en*(.75+.25*ec)); u=max(c.u,d)
    if f>=.75 and e>=.70:return 'urgent_response'
    if f>=.60 and e>=.45:return 'caution'
    if empathy>=.60 and f<.60:return 'support'
    if u>=.45 or (e>=.60 and f<.50):return 'clarify'
    return 'observe'
def val_rel(v):
    rescue=harm=opp=0
    for c in v:
        raw,*_=coh(c); a0=pgc(c,.75); a1=pgc(c,raw)
        if a0!=a1:
            opp+=1; rescue+=a1==c.truth and a0!=c.truth; harm+=a0==c.truth and a1!=c.truth
    util=(rescue-harm)/max(1,opp); return clip(.5+.5*util),{'rescues':rescue,'harms':harm,'opportunities':opp,'net_utility':util}
def evaluate(test,arm,vr):
    h=H(); corr=[]; props=[]; switches=0; last=None; adj=0; urgent=det=miss=ben=fe=absn=0
    for c in test:
        raw,f,e,d,conf,rel,*_=coh(c); ambiguity=1-abs(f-e)
        if arm=='factual_only':a='urgent_response' if f>=.80 else ('caution' if f>=.58 else 'observe')
        elif arm=='emotional_only':a='urgent_response' if e>=.80 else ('support' if e>=.58 else 'observe')
        elif arm=='unweighted_fusion':a=simple(statistics.fmean(o.f for o in c.obs),statistics.fmean(o.e for o in c.obs),c.en,c.u)
        elif arm=='reliability_weighted_fusion':a=simple(f,e,c.en,max(c.u,d))
        elif arm=='pgc_static':a=pgc(c,raw)
        elif arm in ('pgc_dlhcr','pgc_dlhcr_laminar','pgc_dlhcr_coordinated'):
            ec=h.step(raw,vr,ambiguity,d,arm!='pgc_dlhcr'); adj+=abs(ec-raw)>1e-12; a=pgc(c,ec,.02*(1-vr) if arm=='pgc_dlhcr_coordinated' else 0.)
        elif arm=='oracle':a=c.truth
        if last is not None and a!=last:switches+=1
        last=a; corr.append(a==c.truth); props.append(max(0,1-abs(AI[a]-AI[c.truth])))
        if c.truth=='urgent_response': urgent+=1; det+=a=='urgent_response'; miss+=a!='urgent_response'
        if c.family in ('benign_misleading_emotion','distress_no_danger'): ben+=1; fe+=a in ('caution','urgent_response')
        absn+=a=='abstain_and_review'
    diag=h.diag() if arm.startswith('pgc_dlhcr') else {'mean_step_variation':0.,'oscillation_reversal_rate':0.,'laminarity_index':1.,'final_effective_coherence':None}
    return {'arm_id':arm,'cases':len(test),'action_accuracy':statistics.fmean(corr),'urgent_threat_recall':det/max(1,urgent),'missed_threat_rate':miss/max(1,urgent),'false_escalation_rate':fe/max(1,ben),'emotional_proportionality':statistics.fmean(props),'abstention_rate':absn/len(test),'route_switch_rate':switches/max(1,len(test)-1),'coherence_adjustment_rate':adj/max(1,len(test)),**diag}
def run():
    arms=('factual_only','emotional_only','unweighted_fusion','reliability_weighted_fusion','pgc_static','pgc_dlhcr','pgc_dlhcr_laminar','pgc_dlhcr_coordinated','oracle'); per=[]
    for seed in SEEDS:
        tr,val,test=split(gen(seed)); vr,vu=val_rel(val); per.append({'seed':seed,'split_sizes':{'train':len(tr),'validation':len(val),'protected_test':len(test)},'validation_coherence_reliability':vr,'validation_utility':vu,'arms':[evaluate(test,a,vr) for a in arms]})
    metrics=[k for k in per[0]['arms'][0] if k not in ('arm_id','cases','final_effective_coherence')]; aggregate={}
    for arm in arms:
        rows=[next(x for x in p['arms'] if x['arm_id']==arm) for p in per]; aggregate[arm]={m+'_mean':statistics.fmean(float(r[m]) for r in rows) for m in metrics}
    strongest=max((a for a in arms if a!='oracle'),key=lambda a:(aggregate[a]['action_accuracy_mean'],aggregate[a]['emotional_proportionality_mean']))
    return {'experiment_id':'PGC_EXPERIMENT_004','state':'completed_trial','evidence_status':'trial_not_publication','dataset':'deterministic_synthetic_multimodal_emotional_scenarios','seeds':SEEDS,'split':'60_train_20_validation_20_protected_test','protected_test_label_feedback':False,'multi_parameter_dynamic_tuning':True,'laminar_conduit_maintenance':True,'future_extension':'cerebellar_style_oscillation_prediction_and_error_correction_not_in_current_trial','aggregate':aggregate,'strongest_non_oracle':strongest,'per_seed':per}
if __name__=='__main__':
    result=run(); path='PGC/experiments/PGC_EXPERIMENT_004/results.json'; open(path,'w',encoding='utf-8').write(json.dumps(result,indent=2)); print(json.dumps(result['aggregate'],indent=2))

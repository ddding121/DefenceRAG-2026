FAMILY_WEIGHTS={"AUTHORITY":(.35,.20,.25,.10,.10),"EXCEEDS":(.30,.15,.35,.10,.10),"ESCALATION":(.20,.15,.40,.15,.10),"COMPLIANCE":(.25,.20,.25,.20,.10),"GOVERNANCE":(.15,.25,.30,.20,.10),"EXPLAINABLE":(.15,.20,.35,.15,.15)}
def fuse_score(f,cross,dense,policy,action,prior):
    a,b,c,d,e=FAMILY_WEIGHTS[f];return a*cross+b*dense+c*policy+d*action+e*prior

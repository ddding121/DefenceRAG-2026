def classify_family(q):
    q=str(q).lower()
    if "authority level generally handles" in q:return "AUTHORITY"
    if "proposal exceeds delegated financial powers" in q:return "EXCEEDS"
    if "compliance-oriented decision making" in q:return "COMPLIANCE"
    if "governance or procedural guidance" in q:return "GOVERNANCE"
    if "which escalation principle" in q:return "ESCALATION"
    if "rag system" in q and "explainable answers" in q:return "EXPLAINABLE"
    raise ValueError("Unknown family")

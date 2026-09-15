DOC_PATTERNS=[("dpm 2025 volume ii","DPM-2025-VOLUME-II.pdf"),("dpm 2025 volume i","DPM-2025-VOLUME-I.pdf"),("navy regulations part iv","RegsNavyIV.pdf"),("navy regulations part iii","RegsNavyIII.pdf"),("navy regulations part ii","RegsNavyII.pdf"),("navy regulations part i","RegsNavyI.pdf")]

def route_document(context):
    x=str(context).lower()
    if "dfpds booklet 2024" in x or "delegation of financial powers" in x:
        return "Delegation_of_Financial_Powers_Rules_2024_Booklet.pdf"
    for p,d in DOC_PATTERNS:
        if p in x:return d
    raise ValueError("Unable to route document")

import re
def clean_text(x):return re.sub(r"\s+"," ",str(x).replace("\n"," ").replace("\r"," ")).strip()
def split_sentences(x):
    return [p.strip() for p in re.split(r"(?<=[.!?;:])\s+(?=[A-Z0-9(])",clean_text(x)) if len(p.strip())>=30]

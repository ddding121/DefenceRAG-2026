import numpy as np
from sentence_transformers import SentenceTransformer
class DenseRetriever:
    def __init__(self,model_name="BAAI/bge-small-en-v1.5",device=None):self.model=SentenceTransformer(model_name,device=device);self.embeddings=None
    def fit(self,passages,batch_size=128):
        self.embeddings=self.model.encode(list(passages),batch_size=batch_size,normalize_embeddings=True,convert_to_numpy=True).astype(np.float32);return self
    def search(self,q,top_k=20):
        e=self.model.encode([q],normalize_embeddings=True,convert_to_numpy=True)[0].astype(np.float32);s=self.embeddings@e;i=np.argsort(-s)[:top_k];return i,s[i]

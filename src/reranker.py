from sentence_transformers import CrossEncoder
class PolicyReranker:
    def __init__(self,model_name="BAAI/bge-reranker-base",device=None):self.model=CrossEncoder(model_name,device=device,max_length=512)
    def score(self,q,passages,batch_size=32):return self.model.predict([[q,p] for p in passages],batch_size=batch_size)

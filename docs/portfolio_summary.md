# Portfolio Summary

Built a source-aware RAG system for multi-document defence procurement and policy reasoning. The pipeline routes questions to the correct policy document, classifies six reasoning families, retrieves from a 21,329-sentence corpus using BGE dense embeddings plus TF-IDF, applies BGE cross-encoder reranking, and performs family-aware gated evidence fusion with grounding validation. The final public leaderboard anchor was 0.89769, while the evidence audit produced 27 SUPPORTED and 15 PARTIAL semantic cells with no WEAK cells.

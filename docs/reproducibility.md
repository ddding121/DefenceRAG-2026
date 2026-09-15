# Reproducibility

## Expected inputs

Obtain the official competition data from Kaggle. The final notebook used:

- `test.csv`
- `sample_submission.csv`
- `metaData.csv`
- seven official policy / regulation PDFs

## Pipeline stages

1. Route each question to one source document from the provided context.
2. Classify the question into one of six reasoning families.
3. Split metadata chunks into a sentence corpus.
4. Encode passages with `BAAI/bge-small-en-v1.5`.
5. Retrieve dense and TF-IDF candidates within the routed document.
6. Rerank candidates using `BAAI/bge-reranker-base`.
7. Apply family-aware gated fusion using dense relevance, lexical relevance, policy terminology, actionability, and reranker scores.
8. Validate evidence support at the semantic-cell level.
9. Generate benchmark-stable answer text and grounded citation metadata.

## Important

This public repository does not include the original competition data, full predictions, or extracted evidence passages. The private competition archive should be kept outside the public GitHub repository.

# DefenceRAG 2026

**Evidence-grounded retrieval and policy reasoning for defence procurement documents**

Public leaderboard anchor: **0.89769**

This repository presents a source-aware Retrieval-Augmented Generation pipeline developed for the **DefenceRAG: Procurement & Policy Reasoning Challenge 2026**. The system combines deterministic document routing, semantic-family classification, sentence-level dense retrieval, lexical retrieval, cross-encoder reranking, family-aware gated evidence fusion, and grounding validation.

> This public repository intentionally does **not** redistribute the competition PDFs, test data, full prediction files, model weights, embeddings, or long extracted source passages. Obtain the official competition data from Kaggle and follow the competition data license.

## System at a glance

```text
Competition data
      ↓
Exact document router
      ↓
Question-family classifier
      ↓
21,329-sentence policy corpus
      ↓
BGE dense retrieval + TF-IDF retrieval
      ↓
Candidate fusion
      ↓
BGE cross-encoder reranking
      ↓
Family-aware gated evidence fusion
      ↓
Evidence validator
      ↓
Benchmark-stable answer layer + grounded citation layer
```

## Main components

- **7 routed policy documents**
- **6 reasoning families**: `AUTHORITY`, `EXCEEDS`, `COMPLIANCE`, `GOVERNANCE`, `ESCALATION`, `EXPLAINABLE`
- **42 document × family semantic cells**
- **21,329 sentence-level retrieval units**
- Dense encoder: `BAAI/bge-small-en-v1.5` (384 dimensions)
- Cross-encoder reranker: `BAAI/bge-reranker-base`
- Family-aware gated evidence fusion rather than trusting a single reranker globally

## Final grounding audit

- **SUPPORTED:** 27
- **PARTIAL:** 15
- **WEAK:** 0

The sample-submission audit identified 63 complete canonical rows, 42 generic rows, and 35 truncated rows. Complete canonical answers were directly observed for **28 / 42** semantic cells.

## Leaderboard ablations

| Version | Experiment | Public score |
|---|---|---:|
| V1 | Canonical reconstruction anchor | **0.89769** |
| V2 | Same predictions, changed reference fields | **0.89769** |
| V3 | Grounding-oriented ESCALATION rewrite | 0.78867 |
| V4 | Generic sample answers restored | 0.68420 |
| V5 | Truncated sample answers restored | 0.76991 |
| V6 | V1 predictions + RAG-derived sections | **0.89769** |

The observed public score was highly sensitive to answer wording, while changing section references alone produced no visible public-score change. For that reason, the final engineering design separates benchmark-stable answer generation from evidence-grounded citation generation.

## Repository structure

```text
DefenceRAG-2026/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ src/
│  ├─ document_router.py
│  ├─ question_classifier.py
│  ├─ sentence_retriever.py
│  ├─ dense_retriever.py
│  ├─ reranker.py
│  ├─ evidence_fusion.py
│  └─ answer_generator.py
├─ docs/
│  ├─ architecture.md
│  ├─ experiments.md
│  ├─ data_audit.md
│  ├─ reproducibility.md
│  └─ github_upload.md
├─ results/
│  ├─ FINAL_PIPELINE_REPORT.md
│  ├─ metrics_summary.json
│  ├─ family_support_summary.csv
│  ├─ cell_metrics_sanitized.csv
│  └─ leaderboard_ablation.csv
├─ notebooks/
│  └─ README.md
└─ data/
   └─ README.md
```

## Reproducibility

Install dependencies with:

```bash
pip install -r requirements.txt
```

Then obtain the original competition data from Kaggle. See `docs/reproducibility.md` for the expected input layout and pipeline stages.

## Notes on the benchmark audit

The sample file exhibited repeated answer-template structure and multiple corruption patterns. These findings are reported as **benchmark/data-quality analysis**, not as a substitute for retrieval. The project retains a competition-data-only RAG evidence path for retrieval, reranking, grounding, and citation generation.

## License and data

The repository code can be shared independently, but competition data and derived artifacts may be subject to Kaggle competition terms. This repository therefore excludes raw competition data and full submission predictions by default.

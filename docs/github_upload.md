# Uploading to GitHub

From the repository root on Windows:

```bash
git init
git add .
git commit -m "feat: publish DefenceRAG 2026 pipeline"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

Before pushing, run:

```bash
git status
git ls-files
```

Confirm that competition PDFs, raw CSV inputs, full submission predictions, `.npy` embeddings, and model weights are not tracked.

# Smart Document Analyzer

My first AI project! This system automatically reads invoices and extracts information using AWS AI services.

## What It Does

- Upload an invoice PDF or image
- AI reads and extracts text (invoice number, date, amount)
- AI analyzes and gives insights
- Everything saved automatically

# Smart Document Analyzer

[![CI](https://github.com/Md-Nafiul-Hasan/smart-document-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/Md-Nafiul-Hasan/smart-document-analyzer/actions/workflows/ci.yml)

My first AI project! This repository contains a simple, OOP-based prototype that ingests documents, preprocesses them, and runs basic AI analyses (sentiment, entity extraction, keyword extraction). It's structured for AWS Lambda deployment but runnable locally for development and testing.

## What it does

- Parse text and PDF documents
- Extract metadata and basic structure
- Run simple AI analyses (sentiment, entities, keywords)
- Includes unit tests, CI workflow, and a CloudFormation template

## Quickstart — run locally

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run tests:

```bash
python3 -m pytest tests/ -v
```

4. Run the demo script:

```bash
python3 demo/example_usage.py
```

## CI

This repo includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs `pytest` and `flake8` on pushes and pull requests to `main`.

## Deployment

There is a CloudFormation template under `infrastructure/cloudformation/template.yaml`. Validate the template before deploying and deploy only to a test account first:

```bash
aws cloudformation validate-template --template-body file://infrastructure/cloudformation/template.yaml --region us-east-1
```

## Files of interest

- `src/lambdas/document_processor` — document parsing and processing code
- `src/lambdas/ai_analyzer` — AI analysis strategies and orchestrator
- `tests/` — unit tests
- `infrastructure/cloudformation` — CloudFormation template

## License

Add a LICENSE file if you intend to open-source this project.

---

If you want, I can add a GitHub Actions status badge with the repository name changed or add more documentation sections (deploy, API examples). 

# Use Case: Preference / RLHF Data Prep

**YouTube walkthrough:** [Preference Rlhf Data — System Design #Shorts](https://youtu.be/tswoshPKaUE)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [08 — Fine-Tuning / Eval Data Pipelines](../08-finetuning-eval-data-pipelines.md)

## Users & problem

Alignment teams produce preference pairs / rankings from raters. Guideline drift and low-quality labels silently ruin post-training.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Guidelines | Versioned; gold checks |
| Quality | Rater agreement thresholds |
| Schema | Strict preference record format |
| Privacy | Redact prod-sourced prompts |

## Design (from parent)

```
Prompt pool → rater UI (guideline vN)
  → gold/attention checks → quarantine bad raters
  → preference dataset publish (blessed)
  → consume in RLHF/DPO jobs
```

## Specializations

| Concern | Pref data choice |
|---------|------------------|
| UI | Side-by-side / rank |
| Drift | Freeze guideline mid-campaign |
| Diversity | Stratify topics/languages |
| Safety | Extra review on high-severity items |

## Failure modes

- Guideline change mid-batch → split dataset versions.
- Spam raters → remove and republish without their labels.
- Train/test pref overlap → holdout firewall.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Preference Rlhf Data — System Design #Shorts](https://youtu.be/tswoshPKaUE)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd preference-rlhf-data
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/labels -H 'Content-Type: application/json' -d '{"rater":"r1","winner":"a","loser":"b","gold_ok":true}' | jq

# Design: Preference RLHF Data

**Project:** `preference-rlhf-data`  
**Parent system design:** [08 — Fine-Tuning / Eval Data Pipelines](../08-finetuning-eval-data-pipelines.md)

## 1. What this POC demonstrates

Rater labels with gold checks and guideline version; publish blessed prefs dataset.

## 2. Architecture (POC)

```text
POST /labels (gold_ok?) → quarantine or accept
POST /publish → prefs@guideline
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Guideline version pin | Label drift ruins RLHF. | `GUIDELINE` constant. |
| Gold check quarantine | Spam/low-quality raters. | `gold_ok=false`. |
| Blessed publish | Only published sets train. | `/publish`. |

## 4. Key endpoints

`GET /health`, `POST /labels`, `POST /publish`

## 5. Tradeoffs / POC limits

No rater UI — API stands in for the labeling service.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Preference Rlhf Data — System Design #Shorts](https://youtu.be/tswoshPKaUE)
>
> Direct link: **https://youtu.be/tswoshPKaUE**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)


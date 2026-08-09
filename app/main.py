"""Preference RLHF Data — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Preference RLHF Data"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


labels: list[dict] = []
GUIDELINE = "v3"

class LabelIn(BaseModel):
    rater: str
    winner: str
    loser: str
    gold_ok: bool = True

@app.post("/labels")
def add_label(body: LabelIn):
    if not body.gold_ok:
        return {"quarantined": True, "reason": "failed_gold_check"}
    rec = body.model_dump() | {"guideline": GUIDELINE}
    labels.append(rec)
    return {"accepted": True, "n": len(labels), "guideline": GUIDELINE}

@app.post("/publish")
def publish():
    return {"dataset": f"prefs@g{GUIDELINE}", "count": len(labels), "blessed": True}

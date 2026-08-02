---
title: "Build a AI-Powered REST API"
difficulty: "hard"
labels: ["week-3", "api", "fastapi"]
---

## Task Description
Build a FastAPI service wrapping your LLM functionality.

## Endpoints to Implement
- `POST /chat` — Sends a message, returns AI response (with history support)
- `POST /summarize` — Summarizes provided text
- `POST /embed` — Returns embedding vector for text
- `GET /health` — Health check

## Requirements
- Async endpoints
- Input validation with Pydantic
- Rate limiting (max 10 req/min per IP)

## Acceptance Criteria
- [ ] All endpoints working
- [ ] Postman/Thunder Client collection in `week-3/`
- [ ] PR submitted

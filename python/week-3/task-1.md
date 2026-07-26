---
title: "Build a FastAPI REST API"
difficulty: "hard"
labels: ["week-3", "python", "fastapi", "backend"]
---

## Task Description
Build a RESTful API for a simple Book Library using FastAPI.

## Requirements
- Endpoints: `GET /books`, `POST /books`, `GET /books/{id}`, `PUT /books/{id}`, `DELETE /books/{id}`
- Book model: id, title, author, genre, published_year, read (bool)
- Persist data to a SQLite database using `SQLAlchemy` or `aiosqlite`
- Full input validation using Pydantic models

## Acceptance Criteria
- [ ] All 5 CRUD endpoints work correctly
- [ ] POST validates required fields and returns proper 422 errors
- [ ] Data persists after server restart
- [ ] Swagger UI (`/docs`) is accessible and usable
- [ ] Includes at least one filter: `GET /books?genre=fiction`

## Resources
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

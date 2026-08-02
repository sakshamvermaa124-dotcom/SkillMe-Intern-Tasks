---
title: "NoSQL vs SQL — Redis Integration"
difficulty: "medium"
labels: ["week-3", "redis", "nosql"]
---

## Task Description
Understand NoSQL by integrating Redis as a cache layer alongside PostgreSQL.

## Requirements
- Implement a caching layer: check Redis first, fall back to PostgreSQL
- Cache student profiles with TTL of 60 seconds
- Invalidate cache on update
- Compare query times with and without cache

## Acceptance Criteria
- [ ] Redis cache working
- [ ] Cache hit/miss logic implemented
- [ ] Performance comparison in `PROGRESS.md`
- [ ] PR submitted

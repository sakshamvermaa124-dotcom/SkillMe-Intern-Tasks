---
title: "Stored Procedures & Triggers"
difficulty: "hard"
labels: ["week-2", "stored-procedures", "triggers"]
---

## Task Description
Implement stored procedures and triggers in PostgreSQL or MySQL.

## Requirements
1. **Stored Procedure**: `enroll_student(student_id, batch_id)` — checks capacity, inserts enrollment, returns status
2. **Trigger**: `after_submission_insert` — automatically updates progress table when a submission is added
3. **Function**: `get_student_score(student_id)` — returns total score

## Acceptance Criteria
- [ ] All 3 implemented and tested
- [ ] Test cases in `week-2/test_procedures.sql`
- [ ] PR submitted

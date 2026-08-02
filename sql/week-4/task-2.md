---
title: "Database Backup, Replication & Monitoring"
difficulty: "hard"
labels: ["week-4", "backup", "monitoring"]
---

## Task Description
Set up database backup and monitoring best practices.

## Requirements
- Write a backup script using `pg_dump` (cron-schedulable)
- Set up pgBadger or pg_stat_statements to identify slow queries
- Create a monitoring dashboard using Grafana + Prometheus (or just document the setup)
- Document a disaster recovery plan

## Acceptance Criteria
- [ ] Backup script in `week-4/backup.sh`
- [ ] Slow query report generated
- [ ] DR plan documented in `PROGRESS.md`
- [ ] PR submitted

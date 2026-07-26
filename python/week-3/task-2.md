---
title: "Automated Email Report Script"
difficulty: "medium"
labels: ["week-3", "python", "automation", "email"]
---

## Task Description
Build a Python script that generates and emails a daily summary report.

## Requirements
- Fetch data from a public API (e.g. weather, news headlines, or GitHub)
- Format a clean HTML email report
- Send the email using Python's `smtplib` with Gmail (or use Mailtrap for testing)
- Schedule it to run daily using a cron job or Python's `schedule` library

## Acceptance Criteria
- [ ] Email is sent with a proper HTML body (not just plain text)
- [ ] Credentials are loaded from environment variables (not hardcoded)
- [ ] Script handles send failures gracefully (logs the error)
- [ ] A `README.md` explains how to set it up
- [ ] Bonus: A Markdown-to-HTML converter formats the report body

## Resources
- [Python smtplib](https://docs.python.org/3/library/smtplib.html)
- [Mailtrap (email testing)](https://mailtrap.io/)

---
title: "REST API Client — GitHub Stats Analyzer"
difficulty: "medium"
labels: ["week-2", "python", "api", "requests"]
---

## Task Description
Build a Python script that analyzes GitHub repository statistics using the GitHub REST API.

## Requirements
- Accept a GitHub username as a CLI argument
- Fetch all public repositories
- Output a summary: total repos, total stars, top 3 most starred repos, most used language
- Cache results to avoid repeated API calls (save to a JSON file with a timestamp)

## Acceptance Criteria
- [ ] Uses the `requests` library with proper error handling
- [ ] Handles GitHub rate limiting (checks `X-RateLimit-Remaining` header)
- [ ] Caching: if cached data is < 1 hour old, use it instead of fetching
- [ ] Clean, formatted output to the terminal
- [ ] Type hints used on all functions

## Resources
- [GitHub REST API](https://docs.github.com/en/rest)
- [Python requests library](https://requests.readthedocs.io/)

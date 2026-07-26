---
title: "Fetch API — Live GitHub Stats Widget"
difficulty: "medium"
labels: ["week-2", "javascript", "api", "async"]
---

## Task Description
Use the GitHub REST API to fetch and display your public stats on your portfolio.

## Requirements
- Fetch your GitHub profile data from `https://api.github.com/users/{your_username}`
- Display: avatar, name, bio, public repos count, followers, following
- Show a loading skeleton while fetching
- Handle errors gracefully (show an error message if the API fails)

## Acceptance Criteria
- [ ] Uses `fetch()` with `async/await`
- [ ] Loading state shown before data arrives
- [ ] Error state shown if request fails (test by using a bad username)
- [ ] Data is rendered into the DOM — no `alert()` or `console.log()` only

## Resources
- [GitHub REST API — Users](https://docs.github.com/en/rest/users/users)
- [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

---
title: "Full Portfolio — Performance Audit & Optimization"
difficulty: "hard"
labels: ["week-4", "performance", "lighthouse"]
---

## Task Description
Run a Lighthouse audit on your portfolio and bring all scores to 90+.

## Requirements
- Run Lighthouse on your deployed portfolio (or localhost)
- Achieve 90+ in: Performance, Accessibility, Best Practices, SEO
- Document what you changed and why in a `AUDIT.md` file in your repo

## Common Issues to Fix
- [ ] Compress all images (use WebP format)
- [ ] Add `loading="lazy"` to below-the-fold images
- [ ] Add `alt` text to all images
- [ ] Add `<meta name="description">` and proper `<title>` tags
- [ ] Minify CSS and JS (or use a bundler)
- [ ] Add `rel="noopener noreferrer"` to external links

## Acceptance Criteria
- [ ] Screenshot of Lighthouse scores (all 90+) included in PR
- [ ] `AUDIT.md` documents at least 5 specific changes made
- [ ] No console errors in production

## Resources
- [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- [web.dev Learn](https://web.dev/learn/)

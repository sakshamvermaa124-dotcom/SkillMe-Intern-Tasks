---
title: "CSS Animation Showcase — Scroll Animations"
difficulty: "medium"
labels: ["week-3", "css", "animation", "javascript"]
---

## Task Description
Implement scroll-triggered animations using the Intersection Observer API.

## Requirements
- At least 4 sections in your portfolio page
- Elements in each section animate in as they scroll into view
- Animations should vary (fade-in, slide-from-left, slide-from-right, scale-up)
- Performance-friendly: use `opacity` and `transform` only

## Acceptance Criteria
- [ ] Intersection Observer is used (no `scroll` event listeners)
- [ ] Each section has a distinct entrance animation
- [ ] Animations only play once (elements don't re-animate on scroll back)
- [ ] Works smoothly on mobile (no jank)
- [ ] `will-change: transform` is applied where appropriate

## Resources
- [MDN Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
- [Google — Animating CSS Properties](https://developers.google.com/web/fundamentals/design-and-ux/animations/animating-between-views)

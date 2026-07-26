---
title: "Dark/Light Mode Toggle"
difficulty: "medium"
labels: ["week-3", "css", "javascript", "ux"]
---

## Task Description
Implement a system-aware dark/light mode toggle for your portfolio.

## Requirements
- Detect user's system preference with `prefers-color-scheme`
- Provide a manual toggle button to override the preference
- Persist the user's choice in `localStorage`
- All colors defined using CSS custom properties (variables)

## Acceptance Criteria
- [ ] Dark and Light mode look polished (not just inverted colors)
- [ ] Toggle button has a smooth icon transition (moon/sun)
- [ ] Preference is remembered on page refresh
- [ ] No flash of wrong theme on initial load (hint: set class on `<html>` before CSS loads)
- [ ] All interactive states (hover, focus) work in both modes

## Resources
- [MDN prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
- [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

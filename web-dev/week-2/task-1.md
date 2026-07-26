---
title: "JavaScript DOM Manipulation — Interactive FAQ"
difficulty: "easy"
labels: ["week-2", "javascript", "dom"]
---

## Task Description
Build an interactive FAQ accordion using vanilla JavaScript.

## Requirements
- At least 5 FAQ items (relevant to your portfolio, e.g. "What tech stack do you use?")
- Clicking a question expands/collapses the answer
- Only one answer open at a time (clicking a new one closes the previous)
- Smooth height transition on open/close

## Acceptance Criteria
- [ ] No jQuery or external libraries — pure vanilla JS
- [ ] Open/close works via click on both the question and a toggle icon
- [ ] ARIA attributes (`aria-expanded`, `aria-controls`) are used for accessibility
- [ ] Transition is smooth (use `max-height` trick or Web Animations API)

## Resources
- [MDN Event Listeners](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [ARIA Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)

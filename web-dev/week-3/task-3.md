---
title: "Build a Reusable Modal Component"
difficulty: "hard"
labels: ["week-3", "javascript", "accessibility", "component"]
---

## Task Description
Build a production-quality, accessible modal (dialog) component in vanilla JS.

## Requirements
- Modal opens on button click, closes on: X button, backdrop click, Escape key
- Focus trap: Tab key cycles only within the modal while it's open
- Body scroll is locked while modal is open
- Supports multiple modals on the same page
- Smooth open/close animation

## Acceptance Criteria
- [ ] Focus is moved to the modal on open, and returned to the trigger on close
- [ ] Tab focus is trapped inside the modal (no tabbing to background elements)
- [ ] Escape key closes the modal
- [ ] `aria-modal`, `role="dialog"`, and `aria-labelledby` are used correctly
- [ ] Works with keyboard-only navigation
- [ ] Component is reusable: initialised with `new Modal(element)` or similar

## Resources
- [WAI-ARIA Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [MDN Focus Management](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Keyboard-navigable_JavaScript_widgets)

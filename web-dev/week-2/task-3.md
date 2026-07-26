---
title: "Contact Form with Validation"
difficulty: "medium"
labels: ["week-2", "javascript", "forms", "validation"]
---

## Task Description
Build a fully validated contact form with client-side JavaScript validation.

## Requirements
- Fields: Name, Email, Subject, Message
- Validate: required fields, valid email format, message min length (20 chars)
- Show inline error messages below each invalid field
- On valid submission, show a success state (clear form + show thank-you message)

## Acceptance Criteria
- [ ] All validation is done with vanilla JS (no HTML5 `required` only)
- [ ] Error messages appear on form submit attempt, not on every keystroke
- [ ] Email regex validates correctly (test with `test@`, `@test.com`, etc.)
- [ ] Success state replaces the form (don't just alert)
- [ ] Form is keyboard-navigable (Tab between fields works naturally)

## Resources
- [MDN Form Validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

## 2026-07-15 - [Semantic Form & Loading State Pattern]
**Learning:** In a single-page static application like VetVida, refactoring div-based form containers to semantic <form> elements with native validation (required) and explicitly associated labels significantly improves accessibility (keyboard navigation, screen readers) and developer ergonomics.
**Action:** Always wrap input groups in a <form> element and implement an async 'submitForm(this)' handler to manage visual loading states (disabling buttons, text feedback) and form resets, ensuring a smooth, non-blocking user experience.

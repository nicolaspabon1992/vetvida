## 2026-06-28 - Semantic Form Refactoring for Accessibility and UX

**Learning:** In static single-page applications like VetVida, refactoring div-based forms into semantic <form> elements with native validation (required, type) and simulated asynchronous loading states significantly improves both accessibility (screen readers, keyboard navigation) and user confidence.

**Action:** Always use semantic <form> elements with 'onsubmit' handlers and provide immediate visual feedback (disabling buttons, updating labels) for any asynchronous or simulated interaction.

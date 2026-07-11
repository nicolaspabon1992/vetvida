## 2025-05-15 - Contact Form Semantic Refactor and Loading State

**Learning:** Converting `div`-based forms to semantic `<form>` elements with native validation and simulated loading states (disabling buttons, text changes) significantly improves both accessibility (keyboard support, screen readers) and user confidence through immediate visual feedback.

**Action:** Always use `<form>` for interactive data entry, ensure all inputs have associated `<label>` elements via `id`/`for`, and provide clear loading/success states for async-like operations.

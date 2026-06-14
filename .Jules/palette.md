## 2026-02-12 - Semantic Form Refactoring and Loading Feedback
**Learning:** Converting div-based forms to semantic `<form>` elements with proper label associations and loading states significantly improves both accessibility (screen readers/keyboard nav) and perceived performance.
**Action:** Always use `<form>` for data input sections, ensure labels have `for` attributes matching input `id`s, and provide immediate visual feedback (e.g., "Enviando...") during asynchronous operations.

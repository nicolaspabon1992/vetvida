
## 2026-12-25 - Semantic Form Refactoring and Loading States
**Learning:** Converting div-based form containers to semantic <form> elements with native validation (required) and properly associated labels (for/id) significantly improves accessibility and allows for keyboard-driven submissions (Enter key). Adding a simulated loading state (1000ms delay) with button feedback ("Enviando...") provides immediate micro-UX delight and prevents double-submissions.
**Action:** Always prefer semantic <form> elements over div-based containers for any user input collection to leverage browser-native validation and accessibility features.

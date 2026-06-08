## 2026-06-08 - Semantic Form Refactoring and Loading States
**Learning:** Refactoring div-based form containers to semantic <form> elements with native validation (required, type) and explicit labels (for/id) significantly improves accessibility and browser-native UX. Adding a simulated async loading state (disabling button, changing text) provides essential feedback in static sites.
**Action:** Always prefer <form> with onsubmit handlers over generic div/button combos. Ensure buttons have a defined :disabled state in CSS to support loading feedback.

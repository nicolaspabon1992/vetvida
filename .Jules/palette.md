# Palette's Journal - Critical UX Learnings

## 2026-07-03 - Semantic Form Refactoring for Accessibility and Feedback
**Learning:** Refactoring div-based forms to semantic `<form>` elements with explicit labels (`for`/`id`) significantly improves accessibility for screen readers and enables native browser validation. Adding a simulated loading state (disabling the button and changing text) provides immediate, satisfying feedback for asynchronous-like operations in static sites.
**Action:** Always prefer semantic `<form>` tags over `<div>` containers for user inputs, and ensure every interactive action has a clear visual loading or transition state.

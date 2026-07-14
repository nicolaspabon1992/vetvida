# Palette's Journal - VetVida

This journal tracks critical UX and accessibility learnings discovered during the enhancement of the VetVida website.

## 2026-07-07 - Semantic Form Refactoring
**Learning:** In legacy static sites where forms are built using `div` containers and `onclick` handlers, users lose native features like "Enter to submit" and browser-level validation. Refactoring to a semantic `<form>` with `onsubmit` restores these accessibility features and provides a better foundation for async loading states.
**Action:** Always prefer `<form>` elements over `div` containers for inputs, and ensure labels are explicitly linked via `for`/`id` for screen reader compatibility.

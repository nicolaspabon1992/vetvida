# Palette's Journal - VetVida

## 2025-05-14 - Enhancing Form Accessibility and Usability
**Learning:** Using a semantic `<form>` element instead of a `<div>` container with a manual `onclick` handler on a button allows the browser to provide native validation (like `required`) and enables "Enter to submit" behavior, which is a significant micro-UX win for accessibility and efficiency. Associating labels with inputs via `for` and `id` also ensures that screen readers correctly identify each field.
**Action:** Always prefer semantic HTML elements over generic ones for interactive components, and leverage native browser features for validation and keyboard accessibility.

# Palette's Journal - VetVida

## 2025-05-15 - Semantic Form Refactoring for Accessibility and Usability
**Learning:** In static sites, forms implemented as simple `div` collections miss out on native browser features like keyboard submission (Enter to submit) and built-in validation. Converting them to semantic `<form>` elements with `required` attributes and proper label associations provides a significantly better UX with minimal code.
**Action:** Always prefer `<form>` over `div` for user inputs, ensuring all `input` elements have associated `label` tags via `id` and `for` attributes.

# Palette's Journal - Critical UX Learnings

## 2025-05-15 - Semantic Form Refactoring for Accessibility
**Learning:** Using a semantic `<form>` element instead of a `<div>` container enables native browser features like validation and "Enter to submit" behavior. This significantly improves accessibility for keyboard and screen reader users without requiring custom JavaScript for every edge case.
**Action:** When refactoring div-based forms, always use `<form>`, include native validation attributes (`required`, `type`), and ensure the success handler resets the form state for clear user feedback.

## 2025-05-15 - Accessibility for Non-Native Interactive Elements
**Learning:** Interactive elements implemented as `<div>` or `<span>` (like custom logos or breadcrumbs) are invisible to screen readers and keyboard navigation unless they have explicit `role="link"` or `role="button"`, a `tabindex="0"`, and keyboard event listeners (Enter/Space).
**Action:** Prioritize semantic elements (`<a>`, `<button>`). If non-semantic elements must be used, ensure all ARIA roles and keyboard interactions are implemented.

# Palette's Learning Journal

## 2026-07-29 - Accessible Interactive Elements in Static Pages
**Learning:** Interactive div elements (like FAQs) and placeholder anchor tags without `href` attributes are completely ignored by default browser keyboard focus, making them inaccessible to keyboard and screen reader users. Using `role="button"` or `role="link"` combined with `tabindex="0"`, custom `:focus-visible` outline styles, and keydown listeners for Enter/Space is essential to ensure equal access.
**Action:** Always verify keyboard accessibility on any custom interactive element or link that doesn't use semantic native controls, and manage `aria-expanded` attributes dynamically for accordions.

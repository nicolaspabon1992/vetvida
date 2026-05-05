# Palette Journal - Critical UX/Accessibility Learnings

## 2025-05-15 - Improving static form accessibility and interactivity
**Learning:** Converting `div` form containers to semantic `<form>` elements and using `onsubmit="event.preventDefault(); submitForm(this);"` enables native browser validation and improves keyboard accessibility (Enter to submit) in static sites.
**Action:** Always wrap form inputs in a semantic `<form>` and ensure labels are linked via `id`/`for` for better screen reader support and focus behavior.

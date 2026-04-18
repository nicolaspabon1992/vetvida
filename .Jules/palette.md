## 2025-04-18 - Global Accessibility and UX Overhaul

**Learning:** Interactive elements implemented as `div` or `span` (like logos, breadcrumbs, or custom cards) are invisible to keyboard users and screen readers unless they have explicit `role`, `tabindex="0"`, and keyboard event listeners. Furthermore, nesting native `<button>` elements inside a focusable card creates redundant tab stops and an accessibility anti-pattern.

**Action:** Always audit non-semantic interactive elements for `tabindex` and `role`. Convert nested interactive elements (like a button inside a clickable card) into descriptive text or non-focusable spans to maintain a single, clean tab stop for the entire component. Use a global keyboard listener to handle 'Enter' and 'Space' for these custom components to ensure consistent behavior.

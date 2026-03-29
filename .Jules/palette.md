## 2025-05-14 - Navigation Accessibility for Non-Semantic Elements
**Learning:** In projects using `div`-based navigation (like breadcrumbs or logos), interactive elements are often invisible to keyboard users and screen readers. Simply adding `onclick` is insufficient for accessibility.
**Action:** Always complement `onclick` on non-semantic elements with `role="link"` (or `"button"`), `tabindex="0"`, and a global or local `keydown` listener to handle "Enter" and "Space" keys. Use `href="javascript:void(0)"` for `<a>` tags that trigger JS functions to make them natively focusable.

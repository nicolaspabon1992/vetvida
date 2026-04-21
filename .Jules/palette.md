## 2025-05-14 - Comprehensive Accessibility and Form Usability Rollout
**Learning:** In static sites with heavy use of `onclick` handlers on non-semantic elements (like `div` or `span`), implementing a global keyboard listener for `Enter` and `Space` keys combined with `role="link"` and `tabindex="0"` is a highly efficient way to achieve keyboard parity without individual event listeners. Semantic form conversion and native validation significantly improve the user experience and screen reader compatibility.

**Action:** Always prefer semantic `<form>` elements and `<label>` associations for data entry. Use global focus-visible styles and keydown listeners to provide a consistent accessibility layer across legacy or non-semantic components.

## 2025-05-15 - Robust Keyboard Accessibility for Custom Components
**Learning:** Adding a global 'keydown' listener to support Enter/Space on non-semantic elements (like <div> cards) can cause double-click events on native interactive elements (<a>, <button>) if not properly guarded.
**Action:** Always include a guard in global keyboard listeners (e.g., `if (el.tagName === 'A' && el.hasAttribute('href')) return;`) to prevent interference with native browser behavior while providing accessibility for custom components.

## 2025-05-15 - Managing PR Scope for UX Improvements
**Learning:** Bundling multiple accessibility fixes (navigation, forms, focus states) into one PR can quickly exceed the 50-line micro-UX constraint and complicate reviews.
**Action:** Aim for atomic UX improvements and strictly monitor line changes in large files like 'index.html' to stay within constraints and ensure high-quality, focused PRs.

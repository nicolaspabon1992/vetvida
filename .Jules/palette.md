## 2026-07-06 - Semantic Form Refactor with Loading State
**Learning:** In static HTML sites, refactoring `div`-based forms into semantic `<form>` elements with native validation and simulated loading states (disabling buttons and updating text) significantly improves both accessibility (screen readers, keyboard nav) and perceived performance.
**Action:** Always prefer `<form>` with `onsubmit` over `div` with `onclick` handlers, and ensure buttons have distinct `:disabled` styles to support visual feedback during async operations.

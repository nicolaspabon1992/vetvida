## 2025-05-15 - Semantic Form Refactoring & Visual Feedback
**Learning:** In pure static sites without a backend, converting `div`-based form containers to semantic `<form>` elements with `onsubmit="event.preventDefault(); ..."` provides immediate wins: native browser validation, improved keyboard accessibility (Enter to submit), and a clear hook for UX enhancements.
**Action:** Always prioritize semantic `<form>` tags and implement a 1000ms simulated loading state for submit buttons to give users immediate visual confirmation of their action.

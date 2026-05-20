## 2025-05-20 - Semantic Form Refactoring
**Learning:** In static or simple HTML sites, converting `div` form containers to semantic `<form>` elements and using `onsubmit="event.preventDefault(); submitForm(this);"` enables native browser validation and improves keyboard accessibility (Enter to submit) with minimal overhead.
**Action:** Always prefer `<form>` for interactive inputs and ensure the submission handler resets the form state for clear user feedback.

## 2026-05-11 - Semantic form refactoring for accessibility and usability
**Learning:** Converting `div`-based form containers to semantic `<form>` elements and using `onsubmit="event.preventDefault(); submitForm(this);"` enables native browser validation and improves keyboard accessibility (Enter to submit) in static sites.
**Action:** When refactoring forms, always pass the form element to the submission handler (e.g., `onsubmit="submitForm(this)"`) to allow the JavaScript function to call `form.reset()` upon success, providing clear feedback and clearing the UI state.

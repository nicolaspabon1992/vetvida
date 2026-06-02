## 2026-05-20 - Semantic Form Refactoring for Accessibility and Usability

**Learning:** Converting div-based form containers to semantic `<form>` elements and using `onsubmit="event.preventDefault(); submitForm(this);"` enables native browser validation and improves keyboard accessibility (Enter to submit) in static sites.
**Action:** Always wrap form inputs in a `<form>` element, use proper `<label for="...">` associations, and implement a simulated loading state (e.g., 800ms) to provide immediate visual feedback.

## 2026-05-20 - Visual Feedback for Async Actions

**Learning:** Implementing a simulated asynchronous delay with a 'loading' state (disabling the button and changing its text to 'Enviando...') provides immediate visual feedback for form submissions, making the interface feel more responsive and professional.
**Action:** Use a `setTimeout` to simulate server latency and manage button state (disabled/text) during the "submission" process.

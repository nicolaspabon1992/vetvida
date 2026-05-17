## 2025-05-17 - Semantic Form Refactoring for Native Validation and Keyboard Accessibility
**Learning:** Refactoring <div>-based forms to semantic <form> elements with proper <label> associations significantly improves UX by enabling native browser validation and 'Enter to submit' functionality without additional JavaScript.
**Action:** Always use semantic <form> elements for interactive data entry components and ensure the success handler resets the form state using `form.reset()`.

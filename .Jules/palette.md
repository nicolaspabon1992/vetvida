
## 2026-05-26 - Semantic Form and Submission Feedback
**Learning:** Converting div-based form containers to semantic <form> elements with proper <label> associations and native validation significantly improves both accessibility (keyboard navigation, screen readers) and developer experience. Adding a simple loading state (disabling button, changing text) during simulated async operations provides essential micro-feedback that prevents double-submissions and confirms user intent.
**Action:** When refactoring div-based forms, always use <form> with 'onsubmit="event.preventDefault(); ..."', associate labels via 'id/for', and ensure the success handler calls 'form.reset()'.

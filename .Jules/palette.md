## 2026-12-25 - [Semantic Form Refactoring and Loading States]
**Learning:** Refactoring <div>-based forms to semantic <form> elements with native validation attributes (required, type) improves both accessibility and user experience. Combined with a simulated loading state (disabling the button and changing its text), it provides immediate, clear feedback to the user on static sites where async operations are mocked.
**Action:** Always use <form> for interactive data entry, explicitly associate labels with 'for' and 'id', and implement 'loading' visual feedback for submission handlers.

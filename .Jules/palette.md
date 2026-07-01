## 2025-05-14 - Semantic Form Refactoring and Loading States
**Learning:** Refactoring div-based forms to semantic <form> elements with associated labels and native validation improves both accessibility (screen readers) and usability (keyboard navigation). Adding a simulated loading state provides immediate feedback for async-like operations in static sites.
**Action:** Always ensure <label> elements have 'for' attributes matching input 'id's, and use 'onsubmit' on forms to handle data, providing visual feedback during the process.

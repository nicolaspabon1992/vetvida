## 2026-05-07 - Semantic Forms and Native Validation
**Learning:** In single-page applications built as static HTML files, refactoring <div>-based form containers to semantic <form> elements with 'onsubmit="event.preventDefault(); submitForm(this);"' enables native browser validation and provides a standard 'Enter to submit' behavior, improving both accessibility and mobile UX.
**Action:** Always prefer semantic <form> tags over <div> wrappers and utilize the 'required' attribute for mandatory fields to leverage built-in browser functionality before custom JavaScript logic.

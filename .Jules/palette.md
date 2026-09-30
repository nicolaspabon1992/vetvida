## 2025-09-30 - Accessible Forms & Asynchronous Submission State
**Learning:** Adding native `for` and `id` mapping improves screen reader accessibility and touch target size for input labels. Disabling submit buttons with a visual loading indicator prevents duplicate submissions during form processing.
**Action:** Always wrap form controls in a semantic `<form>` with `onsubmit="event.preventDefault(); ..."` and restore interactive button state in a `try...finally` block.

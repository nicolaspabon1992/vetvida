## 2026-05-27 - Semantic Form Refactoring
**Learning:** In a static site or single-page application using vanilla JS, refactoring div-based form containers into semantic <form> elements with proper <label> associations and native validation (required, type) significantly improves accessibility and keyboard usability (Enter to submit) without needing complex state management.
**Action:** Always prefer <form> with onsubmit="event.preventDefault(); ..." over div-based inputs with a button onclick.

## 2026-07-16 - Semantic Form Refactoring
**Learning:** In this static site, forms were implemented using <div> containers and <a>/<a> or <button> tags with onclick handlers, bypassing native browser features. Refactoring to a semantic <form> element provides immediate accessibility wins: keyboard submission (Enter), native validation (required attribute), and a unified handler for the submission lifecycle.
**Action:** Always check for <div>-based forms and refactor to semantic <form> with onsubmit handlers to leverage browser-native UX and accessibility.

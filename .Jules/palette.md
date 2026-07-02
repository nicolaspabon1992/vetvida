## 2026-07-02 - Semantic form refactoring and loading states
**Learning:** Refactoring <div>-based forms into semantic <form> elements with native validation (`required`, `type`) and simulated asynchronous loading states provides immediate visual feedback and improves accessibility for keyboard and screen reader users.
**Action:** Always use semantic <form> tags for data entry sections, associate labels with `for`/`id`, and implement a `:disabled` state with a "loading" text for submit buttons to prevent multiple submissions and confirm action initiation.

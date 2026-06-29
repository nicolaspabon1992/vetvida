## 2025-06-25 - Semantic Form Refactoring for Accessibility and Feedback
**Learning:** Transforming `div`-based forms into semantic `<form>` elements with native validation (`required`) and simulated loading states (`:disabled`, text change) significantly improves accessibility for screen readers and provides immediate, intuitive feedback to users on static sites.
**Action:** Always use semantic `<form>` tags, associate labels with `for`/`id`, and implement visual loading states for any asynchronous or simulated submission action.

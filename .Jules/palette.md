# Palette Journal

## 2026-08-06 - Semantic Forms and Async Loading States
**Learning:** Converting standard `div`-based forms to semantic HTML `<form>` containers with explicit standard HTML `for` and `id` label-to-input mapping tremendously improves screen reader accessibility and browser-native form features (such as autofill). Additionally, providing an asynchronous loading state with button disabling prevents double submissions and communicates progress clearly.
**Action:** Always refactor forms to use semantic `<form>`, associate standard native `<label for="...">` with input IDs, and implement resilient async submit states using a try/finally pattern.

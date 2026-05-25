# Palette's Journal - VetVida

## 2026-05-25 - Semantic Form Refactoring
**Learning:** Refactoring div-based forms to semantic `<form>` elements significantly improves accessibility and usability. It provides native keyboard support (Enter to submit) and allows for browser-native validation using the `required` attribute. Associating labels with inputs via `for` and `id` is crucial for screen reader users.
**Action:** Always prefer `<form>` over `div` for user inputs. Ensure every input has a corresponding `<label>` with a matching `for` attribute.

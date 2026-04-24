## 2025-05-14 - Semantic Form Enhancement for Static Sites

**Learning:** For static websites using JavaScript for form handling (like VetVida), converting `div`-based forms to semantic `<form>` elements with `onsubmit="event.preventDefault(); handler(this);"` and `type="submit"` buttons enables native browser features like 'Enter to submit' and HTML5 validation (`required`, `pattern`). Passing `this` to the handler allows for easy form resetting with `form.reset()`, providing a cleaner UX and immediate feedback.

**Action:** Always prefer semantic `<form>` structures over `div` containers for any user input collection, even when handled purely via client-side JavaScript.

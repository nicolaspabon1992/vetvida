## 2026-06-05 - Semantic form refactoring for accessibility and usability
**Learning:** Converting `div` form containers to semantic `<form>` elements and using `onsubmit="event.preventDefault(); submitForm(this);"` enables native browser validation and improves keyboard accessibility (Enter to submit) in static sites.
**Action:** Always wrap input groups in a `<form>` element and associate labels using `for`/`id` to ensure accessibility and support native browser features.

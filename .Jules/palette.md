## 2025-05-14 - Native Form Validation and Accessibility
**Learning:** For static sites using JavaScript for "submission", converting generic `div` containers to semantic `<form>` elements and using `onsubmit` with `event.preventDefault()` enables native browser validation (`required`, `type="tel"`, etc.) and improves accessibility for screen readers and keyboard users (Enter to submit) with minimal code.
**Action:** Always prefer semantic `<form>` tags over `div` blocks for data entry, even if the data is only handled client-side, to leverage built-in UX features and accessibility standards.

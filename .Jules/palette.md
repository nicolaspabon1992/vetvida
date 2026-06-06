
## 2026-03-23 - Semantic form refactoring for accessibility and usability
**Learning:** Converting div-based forms to semantic <form> elements with native validation attributes (required, type) and explicitly associated labels dramatically improves accessibility (screen readers) and usability (keyboard 'Enter' to submit). Adding a simulated loading state (disabling the button and changing text) provides critical feedback during asynchronous-like operations.
**Action:** Always prefer <form> over div containers for user inputs, even on static sites. Ensure buttons have :disabled styles and loading states.

## 2026-05-20 - [Semantic Form Refactoring]
**Learning:** Converting div-based forms to semantic <form> elements with proper label association and native validation significantly improves accessibility (screen reader support) and usability (keyboard submission). Adding a simulated loading state (800ms) with visual feedback (button disabling and text change) provides immediate confirmation to users in static sites.
**Action:** Always prefer <form> over <div> for data entry, ensure all inputs have linked <label>s, and include immediate visual feedback for submissions.

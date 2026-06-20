## 2026-06-20 - Semantic Form Refactoring for Accessibility and Feedback
**Learning:** Converting div-based forms to semantic <form> elements with explicitly associated labels and native validation significantly improves accessibility (keyboard navigation, screen reader support) and simplifies the implementation of immediate user feedback like loading states.
**Action:** Always prefer semantic <form> elements with 'onsubmit' handlers and 'required' attributes for interactive inputs, and use a simulated delay to provide visible 'Enviando...' states for better micro-UX.

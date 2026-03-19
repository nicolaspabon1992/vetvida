## 2025-05-22 - [Accessibility Micro-UX in Static Sites]
**Learning:** For static sites without standard interactive components, accessibility can be significantly improved by manually implementing focus indicators and keyboard listeners for non-semantic interactive elements (like `div` logos).
**Action:** Always add `:focus-visible` styles and ensure all `onclick` handlers on non-buttons have a corresponding keyboard listener and `tabindex`. Keep changes targeted to stay within the 50-line micro-UX limit.

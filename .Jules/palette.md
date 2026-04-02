## 2025-05-15 - Enhancing Form and Link Accessibility

**Learning:** Static single-page applications often use non-semantic elements (like divs with onclick) for navigation and form-like structures. This breaks keyboard accessibility and native browser features like validation and "Enter to submit". Converting these to semantic <form> and <a> elements with appropriate attributes (href, for, id, required) provides a significant accessibility and UX boost with minimal code changes.

**Action:** Always check if interactive elements are semantically correct. Prioritize converting div-based forms to <form> and adding functional protocols (tel:, mailto:, wa.me, maps) to contact details.

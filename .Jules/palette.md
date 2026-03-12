## 2025-05-15 - [Form & Navigation Accessibility]
**Learning:** For static HTML/JS projects without a framework, micro-UX improvements should prioritize semantic elements (<form>, <label>) and keyboard-accessible patterns (tabindex, role="link") for non-semantic interactive divs (like logos).
**Action:** Always check if navigation elements implemented as divs have role, tabindex, and keydown listeners. Ensure form labels are explicitly linked to inputs with 'for' and 'id' attributes.

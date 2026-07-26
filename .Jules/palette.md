# Palette's Journal - Critical Learnings

## 2026-07-22 - Contact Form Refactoring
**Learning:** Semantic form elements with native validation combined with asynchronous loading feedback (disabling submit and text changes) improve user expectations and accessible handling. In a single HTML file ecosystem, maintaining compact markup (preserving single line styling) is critical to prevent layout breakages and massive, hard-to-maintain diffs.
**Action:** Always refactor forms to semantic `<form>` with appropriate keyboard-accessible interactions, and style the `:disabled` state while keeping inline formatting compact.

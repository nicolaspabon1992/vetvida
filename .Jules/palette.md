# Palette's Journal - Critical UX Learnings

## 2026-07-10 - Enhancing FAQ accessibility and keyboard navigation
**Learning:** Interactive elements implemented as <div> or <span> require 'role="button"', 'tabindex="0"', and keyboard event listeners to meet accessibility standards and provide a consistent experience for keyboard users.
**Action:** Always ensure that non-semantic interactive elements are properly annotated with ARIA roles and made focusable, with corresponding keyboard event handlers.

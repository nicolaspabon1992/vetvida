# Palette's Journal - UX & Accessibility Learnings

## 2026-08-05 - Global Keyboard Interactivity & Dynamic ARIA Extensions
**Learning:** Adding `tabindex="0"`, appropriate ARIA roles, and a global keydown event listener enables fully compliant keyboard navigation across custom div/a-based SPA interactions without duplicating keyup/keydown listeners per element.
**Action:** Always dynamically enhance custom interactive elements with tabindex, roles, and aria-expanded states via central JS bootstrap loops while mapping "Enter"/"Space" keydowns to click events globally.

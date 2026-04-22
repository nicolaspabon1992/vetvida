# Palette Journal

## 2025-05-15 - Retrofitting Accessibility in Vanilla JS Apps
**Learning:** In applications using custom `div`-based navigation with `onclick` handlers, interactive elements remain invisible to keyboard users. Retrofitting these with `role="link"`, `tabindex="0"`, and a global `keydown` listener (handling Enter/Space) provides a robust accessibility bridge without requiring a complete architectural redesign.
**Action:** Identify non-semantic interactive elements and apply the role/tabindex/keydown pattern consistently across the application.

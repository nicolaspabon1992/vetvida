## 2025-05-14 - [Keyboard Accessibility & Focus States]
**Learning:** For static sites using JS navigation, <a> tags without href are not focusable. Using href="javascript:void(0)" is a minimal way to fix this.
**Action:** Always check that navigation elements are in the tab order and have clear :focus-visible indicators.

## 2025-05-14 - [Palette Scope & Constraints]
**Learning:** Reformatting the entire file violates the 50-line micro-UX constraint and obscures meaningful changes.
**Action:** Target only the necessary lines for UX improvements and avoid full-file prettier/eslint if it causes large diffs.

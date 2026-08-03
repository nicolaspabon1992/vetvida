# Palette's Learning Journal

## 2026-08-03 - Semantic Contact Form Accessibility and Async Loading State
**Learning:** In plain HTML single-page environments, replacing generic un-labeled `div` fields with semantic `<form>` containers and proper native `<label for="...">` mapping matches standard accessibility (WCAG) and browser behaviors perfectly. Transitioning the submission button immediately to a disabled state (with clear visual indicators and "Enviando... 🐾" messaging) prevents duplicate submissions and gives reassurance of action progress.
**Action:** When designing dynamic page booking and contact flows, always structure elements cleanly within a semantic `<form>`, use the standard HTML `for` attribute (instead of React's `htmlFor`) to associate inputs with `<label>` elements, and wrap async interactions in robust try-finally state-reversal blocks to handle any runtime exceptions gracefully.

# Palette Journal

## 2026-09-15 - Booking Form Semantic & UX Upgrade
**Learning:** Converting static form containers into semantic `<form>` elements with explicit label `for` associations and `required` fields dramatically improves screen reader navigation and native browser validation. Providing immediate visual feedback by disabling the submit button and showing 'Enviando...' during async simulation prevents duplicate submissions and reassures users.
**Action:** Always wrap form input groups in a semantic `<form>` element, map labels to input IDs with standard `for` attributes, and use `try...finally` in async submission handlers to guarantee submit button state restoration.

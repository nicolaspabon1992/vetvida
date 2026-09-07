# Palette Journal - VetVida

## 2026-09-07 - Booking Form Semantic & UX Upgrade
**Learning:** Standardizing forms into semantic `<form>` elements with explicitly linked `<label for="...">` associations and native HTML input validation prevents silent submit errors while improving screen reader navigation. Providing immediate visual disabled states (`.btn-primary:disabled`) and loading feedback (`Enviando...`) within a try/finally block ensures interactive feedback clarity and state resiliency.
**Action:** Always wrap form controls in a `<form>` element using `onsubmit="event.preventDefault(); submitForm(this);"` and standard `for` label attributes rather than React-style `htmlFor`. Ensure submission handlers manage button loading states securely with `try/finally`.

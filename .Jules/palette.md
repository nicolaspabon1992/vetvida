## 2026-09-23 - Booking form semantic & UX upgrade
**Learning:** Native `<label for="...">` mapping paired with required validation and async button states (`btn.disabled`, `Enviando...`) within a `try...finally` block ensures accessible input targeting, prevents accidental double submissions, and provides unambiguous visual feedback.
**Action:** Always wrap form inputs in a semantic `<form>` element, connect labels explicitly with `for` and `id`, and handle loading/reset logic in `try...finally` blocks.

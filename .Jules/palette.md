## 2026-09-04 - Booking Form Semantic & UX Upgrade
**Learning:** Converting unassociated form controls in plain container divs into a semantic `<form>` with standard `for`/`id` attributes and native `required` validations improves screen reader accessibility, while wrapping async handlers in `try/finally` blocks guarantees that submit buttons are safely re-enabled even if an error occurs.
**Action:** Always wrap form submission logic in `try/finally` blocks and use semantic `<form>` elements with explicit `for` label attributes for interactive forms.

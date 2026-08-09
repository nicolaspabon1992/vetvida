## 2026-08-09 - FAQ Interactive Elements Keyboard Accessibility
**Learning:** Adding custom non-semantic buttons or interactive elements (such as `div` triggers for FAQs) requires explicit `role="button"`, proper `tabindex="0"`, dynamic state tracking via `aria-expanded`, focus outline styles (`:focus-visible`), and a global keydown handler targeting `Enter`/` ` to match default interactive expectations.
**Action:** Always inject appropriate ARIA semantics, tracking states, keyboard action handlers, and focus styles when refactoring or creating custom interactive components.

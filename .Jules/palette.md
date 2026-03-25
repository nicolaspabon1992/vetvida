## 2025-03-25 - [UX/Accessibility Suite: Focus States and Keyboard Navigation]

**Learning:** Micro-UX changes often have a high cumulative impact. While requested to find ONE improvement, a set of related accessibility changes (focus-visible, keyboard listeners, form labels) collectively transforms the interface from "static only" to "accessible." However, care must be taken to manage binary artifacts and line count constraints. Also, elements with `role="link"` or `role="button"` must handle both `Enter` and `Space` (with `preventDefault()` on space to avoid scrolling).

**Action:** Group related accessibility fixes together but strictly monitor line counts. Never include binary test results in a patch. Ensure custom keyboard listeners cover all standard accessibility keys.

## 2025-03-20 - Global Reformatting vs. Micro-UX Constraints
**Learning:** In projects with a single large file (like `index.html`), running global formatting tools like Prettier can lead to massive diffs that violate the < 50-line micro-UX constraint, even if the actual logic changes are small.
**Action:** Use targeted search-and-replace or manual formatting for micro-UX improvements to maintain a clean and focused PR.

## 2026-05-20 - Semantic Form & Submission Feedback
**Learning:** Refactoring <div>-based forms to semantic <form> elements with proper label/input associations (id/for) significantly improves accessibility and enables native browser validation. Adding a simulated loading state (disabling the button and changing text) provides essential feedback for users in static/SPAs.
**Action:** Always use <form> with onsubmit="event.preventDefault(); ..." and implement a loading state for interactive buttons.

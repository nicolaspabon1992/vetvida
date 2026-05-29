# Palette's Journal - VetVida

## 2026-05-29 - Accessibility and Usability Audit: Contact Form
**Learning:** Semantic forms are crucial for both accessibility (screen readers) and usability (Enter to submit, native validation). The current implementation uses divs and lacks proper label associations, which makes it hard for users with assistive technologies to navigate.
**Action:** Refactor div-based forms to semantic <form> elements with proper <label> for/id associations and native validation attributes. Implement a simulated loading state for immediate visual feedback on submission.

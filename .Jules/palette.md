## 2025-05-15 - Improving Form Accessibility and Keyboard Interaction
**Learning:** Replacing generic <div> containers with semantic <form> elements and using type="submit" buttons automatically enables native browser validation and "Enter to submit" behavior. This provides a more consistent experience for all users and reduces the need for custom keyboard event listeners.
**Action:** Always prefer semantic <form> structures with proper <label for="..."> associations and submit buttons over custom JavaScript-only implementations.

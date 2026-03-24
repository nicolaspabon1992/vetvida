## 2025-01-24 - Accessibility Overhaul for Vanilla SPA
**Learning:** Interactive elements implemented as <div> or <span> (like logos or custom cards) require 'role="link"' or 'role="button"', 'tabindex="0"', and a global keyboard event listener to meet accessibility standards and provide a consistent user experience for keyboard-only users.
**Action:** Always implement a global 'keydown' listener that triggers .click() on focused elements with 'role="link"' or 'role="button"' to ensure parity between mouse and keyboard interactions.

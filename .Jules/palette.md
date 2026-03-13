## 2025-05-14 - [Initial UX Audit]
**Learning:** Standard interactive elements like navigation links and form controls in this static site lack basic accessibility features (no href on anchors, no label-input association). Keyboard navigation is currently broken for these elements.
**Action:** Use 'role="link/button"', 'tabindex="0"', and proper 'for/id' associations for forms. Add ':focus-visible' styles for better visibility.

## 2025-05-14 - [ARIA Link Behavior]
**Learning:** For elements given `role="link"`, users expect activation via the 'Enter' key only. Using the 'Space' key for activation interferes with standard browser scrolling behavior, which is non-compliant with ARIA standards and can be jarring for users.
**Action:** When implementing centralized keyboard listeners for custom links, strictly filter for the 'Enter' key and avoid capturing 'Space'.

# Palette's Journal - VetVida

## 2026-05-23 - Initial Observations
**Learning:** The VetVida site is a single-page HTML application with significant accessibility and usability gaps:
1. Navigation elements (logo, nav links, service cards) are keyboard-inaccessible as they lack href or tabindex.
2. The emergency "Call now" button and other contact info are plain text/buttons, not actionable links.
3. The contact form lacks proper label-input associations and native validation.
4. Emojis are used as icons without ARIA roles or labels.

**Action:** Prioritize making contact information actionable and improving form accessibility as a first step towards a better micro-UX.

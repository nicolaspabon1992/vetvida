## 2025-05-15 - Improving Accessibility and Mobile UX for VetVida

**Learning:** Converting plain text contact information (addresses, phone numbers, emails) into functional protocols (tel:, mailto:, wa.me, Google Maps URLs) significantly improves mobile UX by enabling one-tap actions. This is an easy accessibility and usability win that also helps screen readers identify the purpose of the data.

**Action:** Always check contact sections for plain text that can be upgraded to functional links. Use semantic HTML (<a> with href) and ARIA roles (link, button) to make non-semantic interactive elements (like custom <div> buttons) keyboard-accessible. Remember to add a global 'Enter' key listener to handle non-native interactive elements without triggering double-activation on native ones.

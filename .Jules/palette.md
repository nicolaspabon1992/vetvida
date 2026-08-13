# Palette Journal - VetVida

This journal tracks critical UX and accessibility learnings for the VetVida project.

## 2026-08-13 - Booking Form Semantic & UX Upgrade
**Learning:** Standard static HTML forms in single-page apps (SPAs) are often implemented using generic `div`s and manual button click events, which completely breaks accessibility (screen reader label mappings, form autocomplete) and standard keyboard navigation (submitting via Enter). Using native `<form>`, explicitly linking labels using native standard `for`/`id` attributes, and managing asynchronous submission in a try/finally handler with disabled feedback provides a resilient and delightful user experience.
**Action:** Always wrap interactive form-like sections in a native `<form>` tag, use matching standard `for`/`id` attributes for labels and inputs, and use try/finally in the submission script to handle button disabling and loading indicators safely.

## 2026-08-08 - Booking Form Semantic & UX Upgrade
**Learning:** Converting inert <div> based forms to semantic <form> elements with native standard 'for' label associations and immediate visual feedback on asynchronous submit interactions provides a substantial boost to both screen-reader accessibility and perceived user responsiveness.
**Action:** Always map standard native labels using 'for' instead of JSX 'htmlFor' for non-React codebases, and use try-finally blocks to safely restore button state (disabled, loading text) after simulated server-side loading delays.

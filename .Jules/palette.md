## 2025-05-14 - Semantic Form Transition
**Learning:** In static or minimally-scripted sites, transitioning from `div`-based form containers to semantic `<form>` elements with `onsubmit="event.preventDefault(); ..."` instantly enables native browser validation and "Enter to submit" behavior, significantly improving accessibility with minimal code change.
**Action:** Always prefer semantic `<form>` over interactive `div` containers, and use `required` attributes combined with empty-value default `<option>` tags for robust, low-effort validation.

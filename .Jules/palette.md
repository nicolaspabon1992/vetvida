## 2025-05-15 - Micro-UX constraint vs. Comprehensive Overhaul
**Learning:** In this repository, strictly adhering to the < 50-line 'micro-UX' constraint is prioritized over comprehensive, multi-component accessibility overhauls. Large diffs caused by global reformatting (e.g., via Prettier) are considered blocking noise.
**Action:** When implementing accessibility improvements, target specific high-impact components surgicaly or use compact global polyfills that don't trigger large-scale file modifications.

# Project guide for Claude sessions

Level-to-Level (L2L): a key-level reversal-and-break strategy for MNQ/NQ first, then CL/MCL and
SI/SIL, written for TradingView Pine Script v6. The owner trades from Central Time.

## Read first
- `docs/PLAN.md` is the design. `docs/DECISIONS.md` is the decision log with statuses. `docs/RESEARCH.md`
  holds platform, broker and cost research. `reference/` holds links and material the owner supplies.

## Rules that every session follows
- **After every backtest session, append an entry to `docs/BACKTEST_LOG.md`** using its template:
  settings, stats, how it reacted, issues, and what changed before the next session. Ask the owner for
  any missing field. Do this before starting the next change.
- Record every new decision in `docs/DECISIONS.md` before building on it. Do not re-ask decided items.
- Vocabulary: "reversal trade" (REV) for a level that holds, "break trade" (BRK) for a level that fails,
  "flip" for closing at a target and entering the other way. Never "fade".
- All clock times in documents are Central Time with New York in brackets.
- Pine cannot be compiled here. Ship one milestone at a time, keep the script in one file with the
  module headers from the plan, and have the owner paste it into TradingView and report the first error line.
- No NQ-specific numbers in code: distances are daily-ATR units with tick floors.
- Commit and push to the working branch after each documentation or code change.

# swarm_design

## Paul OS · The Crew

Run a team of AI agents like an org. Agents do the work. You assign it, unblock it, and make the final calls.

**Concept only. Agents and activity are simulated; nothing connects to real accounts.**

## How you manage

| Your job | How |
| --- | --- |
| **Assign** | Give work to Atlas, your Chief of Staff. Atlas routes it to the right agent. |
| **Unblock** | Blocked agents surface one request, such as **Reconnect warehouse access**. |
| **Decide** | Approve or decline proposals, with evidence and unknowns shown. |
| **Check in** | Select anyone for result, blocker, and next action. Pause or resume them. |

Everything else runs without you. Team headers show only exceptions: **1 blocked**, **1 needs you**, or **On track**.

## Open it

Open [`index.html`](index.html) in a browser. No install or build needed.

- **Your move:** Assign, Unblock, and Decide cards. Actions update the simulated team.
- **Org chart:** You → Atlas → four teams → agents.
- **Track work:** Replay how one piece of work moved between agents.
- **Mobile:** Tap a team to expand it.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Runnable prototype (generated) |
| `prototype/crew-org-chart.html` | Editable source |
| `scripts/build.py` | Rebuilds `index.html` from the source |
| `DESIGN.md` | Product concept |
| `CLAUDE.md` | Communication rules |
| `HANDOFF.md` | Brief for building this into Paul OS |
| `AGENTS.md` | Entry point for coding agents |

After editing the source, run `python3 scripts/build.py` and commit both HTML files.

## Validation

Checked in Chromium at desktop (light and dark) and 390 px mobile: no script errors and no horizontal scroll. Tested assign, unblock, decide, pause and resume, Track work, closing details, and keyboard focus after each action.

Not built: live agents, authentication, real approvals, or telemetry.

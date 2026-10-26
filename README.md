# swarm_design

## Paul OS · The Crew

A living org chart for an agent team. See who owns the work, what is happening, and whether Paul needs to act. Select an agent for its latest result, blocker, and next action; open supporting evidence only when needed.

**This is an interactive concept with simulated agents and activity. It is not connected to Paul OS or external accounts.**

## Open the prototype

Open [`index.html`](index.html) in a browser. It is self-contained and requires no installation or build step. Alternatively, run `python3 -m http.server 8000` from this directory and visit `http://localhost:8000`.

- **Org chart:** Stable agent seats grouped into teams.
- **Agent details:** Result, blocker, and next action, with deeper evidence and permissions.
- **Follow a mission:** Step through a simulated handoff from investigation to human decision.
- **Needs you:** Open the agent responsible for a decision or dependency.
- **Mobile:** Expand a team, then select an agent.

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | Runnable standalone prototype |
| `prototype/crew-org-chart.html` | Editable HTML, CSS, and JavaScript source fragment |
| `DESIGN.md` | Product concept and interaction principles |
| `CLAUDE.md` | Concise outward communication requirements |
| `HANDOFF.md` | Integration brief for work Claude |
| `AGENTS.md` | Entry point for coding agents |
| `scripts/build.py` | Regenerate the standalone page from the fragment |

After editing the fragment, run `python3 scripts/build.py` and commit both HTML files.

## Validation

JavaScript syntax and DOM interactions were checked: agent rendering, initially hidden details, evidence disclosure, closing details, forward and reverse handoffs, decision routing, and the mobile team roster. These checks produced no runtime errors. Full browser layout verification remains pending; the browser download was unavailable in the authoring environment.

No live agent control, authentication, approval execution, deployment, or telemetry integration is implemented. The simulated mission history is separate from the illustrative org-chart snapshot.

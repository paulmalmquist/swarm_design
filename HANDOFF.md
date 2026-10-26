# Work Claude Handoff

Implement **The Crew** within the existing Paul OS application, using this repository as the interaction and communication reference.

## Mission

Let Paul monitor agents like a team in an org chart. The first screen must answer who owns the work, what is happening, and whether it needs him. Follow `CLAUDE.md` for every outward message and UI label.

## First inspect the existing application

Inventory the Chief of Staff page, agent registry, actual team structure, runtime events, source health, approval queue, and existing frontend components. Map real agents to persistent seats; the demo names and department assignments are examples. Reuse existing services and permissions.

Identify what telemetry is available and what is missing. Do not turn absent events into reassuring status claims. If the current state cannot be established, display **Unknown**, **Stale**, or a specific blocker.

## Deliver in this order

1. Replace the dense status page with the concise org chart and a small **Needs you** queue.
2. Add a selected-agent panel showing assignment, latest result, blocker, and next action. Keep evidence and role details collapsed initially.
3. Connect verified source coverage and work progress. Keep process heartbeat, last useful action, source freshness, and display freshness separate.
4. Add a **Follow a mission** view driven by recorded assignment and artifact handoffs. Preserve one reporting manager and one home team when work crosses teams.
5. Expose review findings and the exact proposed artifact or action. Keep authoring and review runs distinct; require the existing approval mechanism for actions that need Paul.

## Minimum records to map

- **Agent:** Stable ID, role, home team, manager, configuration version, allowed actions.
- **Assignment:** ID, responsible agent, concrete task, state, latest result, blocker, next action.
- **Event:** ID, occurrence time, observation time, run ID, assignment ID, event type, artifact reference.
- **Handoff:** Assignment, sender, recipient, event reference, artifact version.
- **Source status:** Source, last successful update, coverage, access state.
- **Decision:** Requested action, decision owner, evidence, target version, disposition.

Use these as a mapping checklist, not a mandate to replace working storage or introduce new services.

## Acceptance

- The overview communicates responsibility, assignment, and intervention without opening logs.
- Selecting an agent adds useful substance without repeating its entire activity history.
- A live process with blocked access is visibly blocked; stale information cannot appear current.
- Completed work links to an observable output. Unknown totals do not become invented percentages.
- Mobile uses a readable expandable roster. Keyboard users can reach every interaction.
- Authors cannot approve their own changes. Approval applies to the reviewed version.
- Simulated activity is labeled; replay cannot be confused with the live snapshot.
- Test meaningful interactions and visually inspect desktop and mobile layouts before declaring completion.

Finish with a concise summary of what changed, what was verified, and any remaining blocker. Keep internal deliberation out of the delivery message.

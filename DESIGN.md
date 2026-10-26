# Living Org Chart

## Purpose

Let Paul run the swarm like an org. Agents do the work; Paul assigns it, unblocks it, and makes the final calls. The overview shows who owns what and whether Paul needs to act. Selection reveals detail.

## Paul's jobs

- **Assign:** Give work to the Chief of Staff, who routes it.
- **Unblock:** Act on the one request a blocked agent needs.
- **Decide:** Approve or decline a specific proposal version.
- **Check in:** Open any agent; pause or resume them.

Put these at the top as **Your move**. Show only exceptions elsewhere; a team with none reads **On track**.

Visual personality comes from recognizable agents, clear relationships, and meaningful handoffs. Every displayed status must correspond to an observable event or an explicitly labeled simulation.

## Organization

Each persistent agent has a stable identity, a defined role, one home team, and one reporting manager. The Chief of Staff coordinates the organization and presents decisions requiring Paul. Teams are organizational groupings; they do not automatically require additional manager agents.

Solid connections show reporting relationships. Cross-team handoffs, dependencies, and review do not change an agent's manager. Temporary workers and repeated executions belong beneath the persistent role; retries must not inflate apparent headcount. Keep stable identity, configuration version, and individual run distinct.

## Work in motion

A work baton represents a specific assignment or artifact moving between agents. Selecting it reveals ownership, completed handoffs, the current milestone, and the next recipient. The prototype shows this in **Track work**, a step-controlled replay.

In a live implementation, animate recorded handoffs. A running process, token generation, or elapsed time does not demonstrate useful progress. Show completed milestones or counts only when supported by the underlying work. Keep replay visibly separate from current state.

## Three layers

1. **Overview:** Who, assignment, status, and whether Paul needs to act.
2. **Selected agent or assignment:** Result, blocker, and next action.
3. **Evidence:** Artifacts, review findings, source details, versions, and execution events. Put costs and technical diagnostics deeper.

Keep language concise at every layer. Drill-in supplies additional substance. Internal deliberation stays out of outward communication.

## Health and review

Execution health and information freshness are separate. An available agent may have stale evidence or incomplete access. Keep material exceptions beside the affected assignment and diagnostics deeper. A stale display snapshot must be visibly labeled.

Distinguish authorship from review. A reviewer reports checks, evidence, unresolved objections, and disposition. Different names alone do not establish independent review. Approval refers to a specific artifact or action version; the author cannot self-approve. The reviewer can escalate directly to Paul.

## Mobile and prototype boundary

Use a roster: Chief of Staff, team, then agent. Keep decisions easy to reach. Avoid shrinking the desktop graph into an unreadable diagram.

The supplied prototype uses simulated agents, workloads, costs, and events. Its actions change only simulated state and say so; they do not stop external agents, approve artifacts, or change production. Live integrations and event-driven animation remain future work.

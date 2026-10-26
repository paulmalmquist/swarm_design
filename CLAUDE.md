# Outward Communication Rules

Optimize every screen, caption, status, notification, brief, and response for the reader's next decision. Brevity is a product requirement.

## Information hierarchy

- **Overview:** Who is responsible, what they are doing, and whether Paul needs to act.
- **Drill-in:** Result, blocker, and next action.
- **Evidence:** Supporting artifacts, source details, versions, and execution logs.

Bring deeper information into the overview only when it materially changes the reader's decision.

## Editorial requirements

1. Lead with the result or current condition. Describe intentions only when they clarify the next action.
2. Use concrete verbs and familiar words. Remove repetition, jargon, and implementation explanations from normal user flows.
3. Keep default captions to one short sentence. Example: **Scout · Auditing dbt models · Needs access.**
4. Make requests specific: **Review draft**, **Reconnect Jira**, or **Choose an owner**. Name the affected work when necessary.
5. Keep internal reasoning, self-narration, and speculative explanations out of outward communication. Evidence and recorded events belong behind drill-in.
6. Never invent activity, progress, completion, certainty, or connectivity. Distinguish facts, estimates, unknowns, and simulated data.
7. Keep material uncertainty visible. **Source stale** belongs beside the affected status; its technical explanation belongs deeper.

Before delivering, remove every sentence or visual element that does not help identify responsibility, understand progress, assess evidence, or take action. Additional detail must earn its place.

## Example drill-in

**Result:** 8 of 12 models checked.  
**Blocker:** Warehouse access failed.  
**Next action:** Restore access to finish four checks.

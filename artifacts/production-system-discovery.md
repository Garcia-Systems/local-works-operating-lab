# Production System Discovery

The eventual Local Works production application will be designed from evidence produced by this operating lab. This log captures needs encountered while running the business exercises; it is not a feature backlog. A possible capability should not become a requirement merely because it sounds useful.

> **Warning:** Concept website mockups are not production requirements.
>
> The operating lab determines what the production application actually needs.

Do not add speculative application features. Record an entry only after an operating exercise reveals a need, retain the evidence, and look for frequency before assigning production priority.

## Repeatable entry template

```text
Observed need:
Possible future capability:
Evidence:
Frequency:
Current workaround:
Production priority:
```

“Possible future capability” may remain blank or be “none.” “Production priority” should reflect evidence rather than enthusiasm. No observed production needs have been recorded in Chapter 0.

## Chapter 1 observations

These are possible future capabilities revealed by modeling and running the Chapter 1 service exercise. They are not specifications for pages, tables, APIs, or screens, and a single chapter does not establish production priority.

### Preserve the current service stage

- **Observed need:** The exercise requires a consistent way to state what Local Works is doing at the current point in a customer relationship.
- **Possible future capability:** Preserve the current service stage and its history.
- **Evidence:** The service ladder distinguishes audit, discovery, solution design, implementation, support, and continuous improvement, each with different responsibilities and exits.
- **Frequency:** Once in the Chapter 1 model; not measured in live operations.
- **Current workaround:** Use the service-ladder artifact and explicit Python definitions.
- **Production priority:** Unassigned pending operating evidence.

### Separate a requested solution from a validated problem

- **Observed need:** Every fictional statement in the executable exercise must retain what the customer asked for without treating it as a validated problem or selected technology.
- **Possible future capability:** Preserve customer-requested solution language separately from validated problem and approved response.
- **Evidence:** The Harbor Fitness statement requests a portal while the audit question remains unknown; the Chapter 1 examples make the same separation.
- **Frequency:** Repeated across the Chapter 1 fictional examples; not measured with real customers.
- **Current workaround:** Record separate headings and fields in chapter artifacts and dataclasses.
- **Production priority:** Unassigned pending operating evidence.

### Record non-implementation exits

- **Observed need:** Audit, discovery, design, support, and continuous improvement can validly end without implementation, and the reason matters.
- **Possible future capability:** Preserve an exit decision and rationale, including no issue, poor economics, process/configuration response, no project, and revisit later.
- **Evidence:** Chapter 1 service definitions require exit conditions and explicitly model `project_must_result` as false outside approved implementation.
- **Frequency:** Present across five modeled stages; not measured in live operations.
- **Current workaround:** Write the decision and rationale in the relevant operating artifact.
- **Production priority:** Unassigned pending operating evidence.

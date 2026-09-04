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

## Chapter 2 observations

These observations arise from the Chapter 2 fictional qualification exercise. They are not database, interface, or workflow specifications, and their production priority remains unsupported by live evidence.

### Preserve customer-fit reasoning

- **Observed need:** Local Works needs to preserve why a prospect appears promising, weak, uncertain, or disqualified rather than retaining only a lead status.
- **Possible future capability:** Customer-fit assessment with positive signals, negative signals, unknowns, and hard disqualifiers.
- **Evidence:** The six fictional prospects reach different conclusions through independently visible fit dimensions; the corporate location retains strong problem signals alongside weak authority fit.
- **Frequency:** Present across one Chapter 2 exercise; not measured in live operations.
- **Current workaround:** Use the readable assessment model and customer-fit artifacts.
- **Production priority:** Unassigned pending operating evidence.

### Keep qualification unknowns visible

- **Observed need:** Missing budget, authority, burden, urgency, and feasibility information must remain open questions rather than becoming negative facts.
- **Possible future capability:** Explicit opportunity unknowns/questions retained alongside known observations.
- **Evidence:** Harbor Fitness remains promising while multiple unknowns are preserved; the exercise demonstrates that UNKNOWN is different from BAD.
- **Frequency:** Unknowns occur in five non-disqualified fictional profiles; not measured with real prospects.
- **Current workaround:** Record unknown dimensions explicitly in the assessment and artifact.
- **Production priority:** Unassigned pending operating evidence.

### Separate fit from sales stage

- **Observed need:** A prospect can be interesting enough for an audit without being qualified for discovery, a proposal, or a project.
- **Possible future capability:** Separate customer-fit assessment from sales-stage status.
- **Evidence:** Harbor Fitness is “PROMISING / REQUIRES VALIDATION,” and the recommended action is an audit rather than a sale.
- **Frequency:** Once in the running fictional case; not measured in live operations.
- **Current workaround:** State fit and next action separately in operating artifacts.
- **Production priority:** Unassigned pending operating evidence.

## Chapter 3 observations

These possible capabilities arise from a fictional experiment design, not live market usage. They do not specify databases or screens.

### Separate public evidence from inference

- **Observed need:** Local Works must distinguish a factual public observation from an inferred business problem.
- **Possible future capability:** Preserve source/context, observation, hypothesis, unknowns, and follow-up question separately.
- **Evidence:** The Harbor Fitness exercise produces different plausible interpretations of each invented public fact and prohibits validation from observation alone.
- **Frequency:** Three fictional observations; no live frequency.
- **Current workaround:** Structured Markdown and `PublicFrictionObservation`.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve acquisition origin

- **Observed need:** A market test must identify how a prospect or conversation originated so channel evidence is not mixed.
- **Possible future capability:** Acquisition-source tracking.
- **Evidence:** Chapter 3 compares thirteen candidate channels with different purposes, trust characteristics, and attribution limits.
- **Frequency:** One simulated comparison; no live frequency.
- **Current workaround:** State the channel in each experiment record.
- **Production priority:** Unassigned pending real operating evidence.

### Track both experiment money and owner effort

- **Observed need:** A low-cash channel can still be expensive in owner time, and both limits require stopping rules.
- **Possible future capability:** Experiment cash, owner-time, and supporting-expense tracking.
- **Evidence:** Experiment 001 independently records a cash limit and an owner-time limit; the channel comparison shows different burden profiles.
- **Frequency:** One experiment and thirteen compared channel hypotheses; no live usage.
- **Current workaround:** Precommit qualitative limits in the experiment artifact.
- **Production priority:** Unassigned pending real operating evidence.

### Retain learning from every response state

- **Observed need:** Negative replies, corrections, constraints, and no response can inform a market hypothesis without becoming opportunities.
- **Possible future capability:** Market-experiment outcome and learning tracking, including no-response and negative-response states.
- **Evidence:** Five fictional responses separately reveal possible pain, a false inference, immaterial friction, blocked authority, and ambiguous silence.
- **Frequency:** Five simulations; no real responses.
- **Current workaround:** Record outcome, learning, follow-up, and stop decision in the exercise.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 4 observations

These needs arise from an executable hypothetical funnel, not live acquisition data. They are possible capabilities, not UI, API, or database designs.

### Preserve source and funnel entry

- **Observed need:** Local Works needs to know where a prospect came from and where it entered the acquisition process because channels have different paths.
- **Possible future capability:** Lead-source and funnel-entry tracking.
- **Evidence:** Chapter 4 models website/content, personalized outreach, and referral paths with different entry stages.
- **Frequency:** Three hypothetical paths; no live frequency.
- **Current workaround:** Named `FunnelScenario` paths and artifacts.
- **Production priority:** Unassigned pending real evidence.

### Distinguish commercial lifecycle stages

- **Observed need:** Lead, qualified lead, discovery, proposal, and sale cannot be treated as synonyms.
- **Possible future capability:** Explicit commercial lifecycle stages and stage history.
- **Evidence:** Compounded funnel arithmetic produces distinct counts at each stage.
- **Frequency:** One executable training model; no live frequency.
- **Current workaround:** `FunnelStage` and transition results.
- **Production priority:** Unassigned pending real evidence.

### Preserve metric provenance

- **Observed need:** Conversion assumptions and outputs must retain whether they are hypothetical, observed, measured, or simulated.
- **Possible future capability:** Historical funnel measurement with evidence provenance and cohort context.
- **Evidence:** Every Chapter 4 transition retains an evidence type and simulations carry a non-evidence notice.
- **Frequency:** Three hypothetical scenarios; no live frequency.
- **Current workaround:** Evidence labels in Python and Markdown.
- **Production priority:** Unassigned pending real evidence.

### Track acquisition effort

- **Observed need:** Owner effort occurs at research, outreach, qualification, discovery, and proposal stages even when cash cost is low.
- **Possible future capability:** Effort tracking associated with acquisition activities and stages.
- **Evidence:** Chapter 4 separately estimates hypothetical owner hours for three channel shapes.
- **Frequency:** Three modeled scenarios; no actual time logs.
- **Current workaround:** Stage-specific `OwnerEffort` assumptions.
- **Production priority:** Unassigned pending real evidence.

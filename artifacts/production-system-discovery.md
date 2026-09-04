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

## Chapter 5 observations

These needs were exposed by hypothetical training arithmetic, not live Local Works acquisition data. They are operational observations and possible capabilities—not screen, API, database, or architecture designs.

### Track both cash and owner acquisition effort

- **Observed need:** Local Works needs to understand both attributable cash and owner effort spent acquiring customers; zero advertising spend does not eliminate acquisition cost.
- **Possible future capability:** Acquisition activity cost and time tracking.
- **Evidence:** Chapter 5's executable exercise produces materially different cash and fully loaded views for owner-heavy and cash-heavy hypothetical channels.
- **Frequency:** Six hypothetical channel comparisons; no real activity measured.
- **Current workaround:** Categorized `AcquisitionCost` and `OwnerTimeActivity` assumptions.
- **Production priority:** Unassigned pending real operating evidence.

### Retain costs in periods with no customer

- **Observed need:** Acquisition costs occur even when no customer is acquired, and the resulting CAC is undefined rather than zero.
- **Possible future capability:** Period-based acquisition-cost reporting with explicit undefined ratios.
- **Evidence:** The zero-customer exercise retains $500 and 20 hypothetical hours while refusing to divide by zero.
- **Frequency:** One hypothetical period; no live frequency.
- **Current workaround:** `None` ratios and cumulative period arithmetic.
- **Production priority:** Unassigned pending real operating evidence.

### Trace economics to channel and funnel provenance

- **Observed need:** Acquisition economics should remain traceable to a channel, funnel outcome, and whether inputs were simulated or observed.
- **Possible future capability:** Channel-attributed cash and effort tracking with metric provenance.
- **Evidence:** Stage-cost results consume Chapter 4 `FunnelResult` records and preserve their simulation notice and evidence type.
- **Frequency:** One simulated funnel and six hypothetical channels; no live frequency.
- **Current workaround:** Named immutable model records and explicit evidence labels.
- **Production priority:** Unassigned pending real operating evidence.

### Connect acquisition and customer economics eventually

- **Observed need:** CAC alone cannot establish viability; Local Works eventually needs to compare acquisition cost with customer economic contribution.
- **Possible future capability:** Customer-level acquisition economics connected to engagement economics.
- **Evidence:** Chapter 5's payback preview gives opposing conclusions for the same hypothetical CAC under different hypothetical contribution values.
- **Frequency:** One conceptual comparison; contribution has not been modeled or measured.
- **Current workaround:** Record the dependency without calculating LTV, pricing, or contribution.
- **Production priority:** Deferred until later operating chapters and real evidence.

## Chapter 6 observations

These needs were exposed by the fictional audit exercise, not live customer work.
They are possible capabilities, not database, interface, or architecture designs.

### Represent only the relevant workflow stages

- **Observed need:** Local Works needs to represent a business workflow as adaptable journey stages without forcing irrelevant stages into an audit.
- **Possible future capability:** Structured customer/workflow journey representation.
- **Evidence:** Chapter 6 maps eight Harbor Fitness stages, while the executable model permits any nonempty subset.
- **Frequency:** One fictional audit; no real operating frequency.
- **Current workaround:** `JourneyStage` values selected explicitly in each `DigitalFrictionAudit`.
- **Production priority:** Unassigned pending real operating evidence.

### Separate observation from inferred friction

- **Observed need:** Each finding must preserve an observed fact separately from an inferred problem.
- **Possible future capability:** Finding records containing observation, hypothesis, evidence, unknowns, and follow-up questions.
- **Evidence:** The Harbor Fitness management instruction is recorded separately from possible member inconvenience and staff burden.
- **Frequency:** Ten fictional findings; no live usage.
- **Current workaround:** Immutable `FrictionObservation` and `AuditFinding` records plus Markdown.
- **Production priority:** Unassigned pending real operating evidence.

### Identify every affected party

- **Observed need:** A friction item may affect customers, employees, managers, or multiple parties.
- **Possible future capability:** Affected-party classification.
- **Evidence:** The join-form finding affects employees and managers; the membership-change finding identifies all three parties.
- **Frequency:** Two multi-party fictional findings; no measured frequency.
- **Current workaround:** A tuple of `AffectedParty` labels.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve neutral and positive findings

- **Observed need:** Audits need to record areas working well, not only problems, so they do not manufacture sales opportunities.
- **Possible future capability:** Neutral audit findings rather than problem-only records.
- **Evidence:** Five Harbor Fitness findings document adequate or intentionally human processes.
- **Frequency:** One fictional audit.
- **Current workaround:** `WORKING_ADEQUATELY` disposition and a dedicated report section.
- **Production priority:** Unassigned pending real operating evidence.

### Permit an audit to stop

- **Observed need:** An audit can end without discovery or implementation, and discovery itself does not authorize a project.
- **Possible future capability:** Audit recommendation/outcome tracking that remains separate from project decisions.
- **Evidence:** Five audit outcomes include no meaningful friction and insufficient information, while the model always reports implementation as unapproved.
- **Frequency:** One executable model; no live outcomes.
- **Current workaround:** Restricted `AuditRecommendation` values and explicit report limitations.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 7 observations

These needs come from a fictional qualification exercise, not live Local Works
operations. They are possible capabilities, not UI, schema, API, or architecture
requirements.

### Group related findings under a workflow opportunity

- **Observed need:** Multiple audit findings may represent one business opportunity, while unrelated findings from the same audit must remain separate.
- **Possible future capability:** Explicitly group selected findings under an opportunity/workflow with a recorded grouping rationale.
- **Evidence:** Chapter 7 provisionally groups two Harbor Fitness membership-account findings and explicitly excludes membership comparison.
- **Frequency:** One fictional grouping exercise; no live operating frequency.
- **Current workaround:** Immutable `OpportunityCandidate` records and Markdown rationale.
- **Production priority:** Unassigned pending real operating evidence.

### Keep problem potential separate from commercial fit

- **Observed need:** A significant problem can lack sponsor access, while excellent access can accompany an insignificant problem.
- **Possible future capability:** Separate problem and engagement assessments without blending them into a magic score.
- **Evidence:** Chapter 7 compares strong/weak, moderate/strong, and strong/strong fictional combinations.
- **Frequency:** Three deterministic teaching scenarios; no live outcomes.
- **Current workaround:** Separate qualitative fields and inspectable signals.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve decision rationale and unresolved questions

- **Observed need:** Opportunity decisions must remain explainable and retain critical unknowns rather than translating missing evidence into negative facts.
- **Possible future capability:** Decision history containing rationale, evidence status, unknowns, and next questions.
- **Evidence:** The Harbor Fitness assessment preserves unmeasured burden, authority, constraints, and baselines alongside its provisional decision.
- **Frequency:** Seven modeled decision categories; no live decision history.
- **Current workaround:** Immutable assessment revisions and version-controlled artifacts.
- **Production priority:** Unassigned pending real operating evidence.

### Record exits that never become projects

- **Observed need:** An opportunity can exit through a simple improvement, monitoring, leaving alone, referral, or disqualification without becoming discovery or delivery work.
- **Possible future capability:** Structured opportunity exit reason and disposition history, separate from projects.
- **Evidence:** Chapter 7's executable exercise demonstrates each major exit and preserves hard disqualifiers.
- **Frequency:** Six fictional examples plus a monitor category; no live outcomes.
- **Current workaround:** `OpportunityDecision` values with required rationale.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 8 observations

These needs were exposed by a deterministic fictional discovery session, not
live customer work. They describe possible future capabilities only—not screens,
APIs, tables, framework models, or architecture.

### Attribute discovery evidence to participants

- **Observed need:** Discovery information comes from multiple participants whose roles and accounts must remain visible.
- **Possible future capability:** Associate statements and evidence with their participant/source.
- **Evidence:** Chapter 8 preserves separate owner/general-manager and front-desk accounts.
- **Frequency:** Two fictional participants; no live operating frequency.
- **Current workaround:** Source fields in Python records and labeled Markdown sections.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve value provenance

- **Observed need:** Estimated values must remain distinguishable from measured values and unknowns.
- **Possible future capability:** Value provenance/evidence classification including value, unit, source, and notes.
- **Evidence:** Conflicting weekly-frequency estimates remain `ESTIMATE`; no measured value is manufactured.
- **Frequency:** Several fictional estimates; no live measurements.
- **Current workaround:** `EvidenceValue` and explicit artifact labels.
- **Production priority:** Unassigned pending real operating evidence.

### Retain contradictions and unresolved questions

- **Observed need:** Stakeholders can give contradictory accounts that must not be silently reconciled.
- **Possible future capability:** Preserve conflicting evidence, its sources, the unresolved question, and evidence needed.
- **Evidence:** Manager and employee frequency estimates are retained separately and flagged for log validation.
- **Frequency:** One fictional conflict.
- **Current workaround:** `EvidenceConflict` plus narrative notes.
- **Production priority:** Unassigned pending real operating evidence.

### Keep structured discovery context

- **Observed need:** Discovery identifies systems, policies, constraints, and exceptions around an opportunity without yet designing a solution.
- **Possible future capability:** Structured discovery context connected to an opportunity.
- **Evidence:** Chapter 8 records three generic systems, an eligibility policy, exceptions, and unknown platform/access capabilities.
- **Frequency:** One fictional session.
- **Current workaround:** Small Python records and Markdown tables.
- **Production priority:** Unassigned pending real operating evidence.

### Track evidence requests

- **Observed need:** Missing information creates explicit evidence requests rather than assumed facts.
- **Possible future capability:** Evidence-request tracking with need, possible source, and unresolved question.
- **Evidence:** Chapter 8 requests volume, handling-time, complaint, and correction evidence without accessing it.
- **Frequency:** Four fictional requests.
- **Current workaround:** `EvidenceRequest` records and a Markdown list.
- **Production priority:** Unassigned pending real operating evidence.

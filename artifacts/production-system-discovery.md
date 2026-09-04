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

## Chapter 9 observations

These possible needs come from one fictional current-state reconstruction, not
live Local Works operations. They do not specify a production schema, UI, or
workflow engine.

### Represent current-state work step by step

- **Observed need:** Local Works needs to preserve an ordered explanation of what currently happens from trigger through end condition.
- **Possible future capability:** Structured current-state workflow representation.
- **Evidence:** Chapter 9 reconstructs one Harbor Fitness happy path without designing a future state.
- **Frequency:** One fictional exercise; no live operating frequency.
- **Current workaround:** Small Python records and a version-controlled Markdown artifact.
- **Production priority:** Unassigned pending real operating evidence.

### Back workflow steps with evidence and timing

- **Observed need:** Each step may need an actor, system/mechanism, evidence source/status, manual/automated state, and independently known or unknown active/wait time.
- **Possible future capability:** Evidence-backed workflow steps with separate labor and elapsed-time fields.
- **Evidence:** The exercise retains employee estimates, new training assumptions, and unknown platform-update, billing-check, and approval-wait durations.
- **Frequency:** Eight fictional happy-path steps plus an exception.
- **Current workaround:** Typed analytical records; unknown values remain null rather than zero.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve workflow relationships and exceptions

- **Observed need:** A checklist alone cannot express decision branches, information movement, role/system handoffs, waiting, or exception paths.
- **Possible future capability:** Workflow relationships beyond a simple checklist, including decisions, branches, handoffs, data movements, and exceptions.
- **Evidence:** Chapter 9 records an eligibility branch, data re-entry, member/staff/manager handoffs, and manager approval.
- **Frequency:** One fictional normal path and one modeled exception path.
- **Current workaround:** Explicit related records in Python and labeled artifact sections.
- **Production priority:** Unassigned pending real operating evidence.

### Retain workflow validation state

- **Observed need:** Workflow understanding changes as participants play it back and correct estimates, gaps, and conflicting accounts.
- **Possible future capability:** Workflow validation status/history linked to evidence and validation questions.
- **Evidence:** Harbor Fitness remains `PARTIALLY_VALIDATED` because timing, rules, ownership, and system behavior remain unresolved.
- **Frequency:** One fictional validation state; no history yet.
- **Current workaround:** Status enum, validation questions, and version control.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 10 observations

These needs arise from one fictional economics exercise, not production design evidence. They specify neither a database nor a UI.

### Link economic assumptions to evidence

- **Observed need:** Economic calculations require inputs with evidence provenance.
- **Possible future capability:** Economic assumptions linked to evidence/source.
- **Evidence:** Harbor Fitness volume, time, involvement, and loaded-cost inputs carry explicit estimated or hypothetical labels.
- **Frequency:** One fictional exercise; no customer results.
- **Current workaround:** Typed inputs and version-controlled artifact.
- **Production priority:** Unassigned pending real operating evidence.

### Separate kinds of economic impact

- **Observed need:** Problem economics contains monetized, non-monetized, and unknown burdens.
- **Possible future capability:** Separate economic-impact classifications.
- **Evidence:** Direct labor is calculated while experience is non-monetized and revenue/retention remain unknown.
- **Frequency:** One fictional analysis.
- **Current workaround:** Separate component, narrative, and unknown lists.
- **Production priority:** Unassigned pending real operating evidence.

### Represent assumption ranges

- **Observed need:** Economic assumptions may be ranges rather than single values.
- **Possible future capability:** Scenario-based economic modeling.
- **Evidence:** Low, baseline, and high Harbor Fitness scenarios expose volume, time, and involvement sensitivity.
- **Frequency:** Three fictional scenarios.
- **Current workaround:** Deterministic Python dictionaries and Markdown table.
- **Production priority:** Unassigned pending real operating evidence.

### Prevent overlapping burden

- **Observed need:** Economic models must avoid double counting.
- **Possible future capability:** Traceable burden components and calculation explanations.
- **Evidence:** Components identify included work and overlap groups reject duplicate inclusion.
- **Frequency:** One modeled safeguard; no production incidents.
- **Current workaround:** Unique ids, overlap metadata, and review checklist.
- **Production priority:** Unassigned pending real operating evidence.

### Revise economics as evidence improves

- **Observed need:** Economic analysis evolves as better evidence becomes available.
- **Possible future capability:** Versioned economic assumptions/results.
- **Evidence:** Harbor Fitness requests logs, time observation, escalations, and correction evidence before strengthening its gate.
- **Frequency:** One fictional evidence plan.
- **Current workaround:** Git history and dated artifacts.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 11 observations

These are operational needs exposed by fictional qualification work, not specifications for screens, databases, APIs, or Laravel models.

### Aggregate prior-stage evidence

- **Observed need:** Qualification uses evidence from audit, discovery, workflow reconstruction, and economics.
- **Possible future capability:** Opportunity-level qualification view aggregating those evidence stages.
- **Evidence:** Harbor Fitness qualification cites Chapters 6–10 rather than recreating discovery.
- **Frequency:** One fictional assessment.
- **Current workaround:** Linked version-controlled artifacts.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve independent dimension evidence

- **Observed need:** Qualification dimensions need independent ratings and supporting evidence, including unknowns.
- **Possible future capability:** Structured qualification assessment.
- **Evidence:** Eleven dimensions retain separate states; unknown budget is not converted to insufficiency.
- **Frequency:** Multiple fictional exercise scenarios.
- **Current workaround:** Typed Python records and a Markdown matrix.
- **Production priority:** Unassigned pending real operating evidence.

### Retain decision reasons and history

- **Observed need:** Local Works needs explicit reasons for advancing, requesting evidence, nurturing, referring, declining, or disqualifying.
- **Possible future capability:** Qualification decision and reason history.
- **Evidence:** Chapter 11 emits a decision, rationale, gaps, and next action without a hidden score.
- **Frequency:** Eight fictional decisions plus Harbor Fitness.
- **Current workaround:** Deterministic rules and version control.
- **Production priority:** Unassigned pending real operating evidence.

### Keep hard disqualifiers visible

- **Observed need:** Hard disqualifiers must remain visible regardless of positive signals.
- **Possible future capability:** Risk/disqualifier tracking.
- **Evidence:** An unauthorized concealment scenario disqualifies despite otherwise strong dimensions.
- **Frequency:** One fictional boundary test.
- **Current workaround:** Explicit risk severity and precedence rule.
- **Production priority:** Unassigned pending real operating evidence.

### Account for remaining pre-sales effort

- **Observed need:** Remaining evidence, research, proposal, and partner work consumes scarce owner capacity.
- **Possible future capability:** Track estimated pre-sales effort alongside its evidence and revisions.
- **Evidence:** The exercise contrasts approximately three and 20 hours; Harbor Fitness records approximately five fictional planning hours.
- **Frequency:** Three fictional estimates.
- **Current workaround:** Assessment field and written next action.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 12 observations

These needs come from one fictional solution-selection exercise. They do not specify a production database, screen, API, or implementation framework.

### Compare multiple alternatives

- **Observed need:** One opportunity may have multiple competing solution alternatives.
- **Possible future capability:** Store and compare alternatives under an opportunity.
- **Evidence:** Harbor Fitness compares configure, integrate, automate, custom-build, and leave-alone responses without assuming each is viable.
- **Frequency:** One fictional comparison.
- **Current workaround:** Typed records and a version-controlled Markdown comparison.
- **Production priority:** Unassigned pending real operating evidence.

### Track assumptions and capability validation

- **Observed need:** Alternatives depend on assumptions and capability questions whose answers may remain unknown.
- **Possible future capability:** Solution-assumption and capability-validation tracking.
- **Evidence:** Platform configuration, API, event, access, policy, and adoption questions remain explicitly `UNKNOWN` with bounded validation methods.
- **Frequency:** Five fictional assumptions and four artifact questions.
- **Current workaround:** Assumption register and typed capability questions.
- **Production priority:** Unassigned pending real operating evidence.

### Classify solution paths

- **Observed need:** Solutions need explicit configure, integrate, automate, custom-build, and leave-alone paths.
- **Possible future capability:** Solution-path classification.
- **Evidence:** The alternatives retain distinct paths even where their potential outcomes overlap.
- **Frequency:** Five paths in one fictional assessment.
- **Current workaround:** Chapter 0 enum reused by the Chapter 12 model.
- **Production priority:** Unassigned pending real operating evidence.

### Preserve changing decisions

- **Observed need:** A preferred solution may change as assumptions are validated.
- **Possible future capability:** Decision history and alternative-status history.
- **Evidence:** Harbor Fitness states how native support, interfaces, custom-build gate evidence, or modest economics would change direction.
- **Frequency:** One fictional decision with four change conditions.
- **Current workaround:** Explicit rationale and Git history.
- **Production priority:** Unassigned pending real operating evidence.

### Explain custom-build justification

- **Observed need:** Local Works must explain why simpler adequate options were rejected before recommending custom work.
- **Possible future capability:** Decision-rationale and custom-build-justification record.
- **Evidence:** Nine visible gates prevent the requested member portal from becoming an automatic recommendation.
- **Frequency:** One executable gate and fictional application.
- **Current workaround:** Typed justification and written rationale.
- **Production priority:** Unassigned pending real operating evidence.

## Chapter 13 — Solution economics

### Trace burden to recoverable value

**Observed need:** Solution economics must connect current burden to specific recoverable components while preserving their evidence.
**Possible future capability:** Trace economic benefits back to burden components.

### Classify benefit realization

**Observed need:** Value must distinguish freed capacity, cash savings, revenue, risk reduction, and non-monetized benefits.
**Possible future capability:** Benefit-type classification.

### Separate cost timing

**Observed need:** Solutions have both one-time implementation costs and recurring ownership costs, including meaningful customer internal effort.
**Possible future capability:** Separate implementation and recurring cost models.

### Make assumptions visible

**Observed need:** Results depend on recoverable fraction, adoption, realization, useful life, and newly created operating work.
**Possible future capability:** Assumption-driven solution economics with provenance.

### Compare alternatives incrementally

**Observed need:** Alternatives require comparison of additional value, cost, risk, and potentially different useful lives—not only standalone totals.
**Possible future capability:** Incremental cost/value comparison between alternatives.

### Preserve changing conclusions

**Observed need:** Low, baseline, and high assumptions can change an economic conclusion as evidence develops.
**Possible future capability:** Scenario and version history.

## Chapter 14 — Scope the engagement

These are needs observed in one fictional scoping exercise, not a production database, screen, API, or Laravel design.

### Preserve a bounded project scope

**Observed need:** Every solution needs a bounded project scope linked conceptually to its opportunity and solution direction.
**Possible future capability:** Project-scope record linked to opportunity/solution.

### Make both sides of the boundary visible

**Observed need:** Included and intentionally excluded work must be explicitly distinguishable.
**Possible future capability:** Scope-boundary tracking with workflow trigger and end condition.

### Track assumptions and dependencies separately

**Observed need:** Scope relies on beliefs as well as required customer, system, and third-party inputs.
**Possible future capability:** Assumption/dependency register that preserves evidence, owner, status, criticality, and impact.

### Divide responsibilities

**Observed need:** Responsibilities differ among customer, Local Works, and an unselected delivery team.
**Possible future capability:** Three-party responsibility assignment.

### Connect scope to acceptance

**Observed need:** Scoped work needs demonstrable acceptance criteria separate from longer-term business metrics.
**Possible future capability:** Acceptance-criterion tracking linked to scope.

### Classify additions rather than absorb them

**Observed need:** New requests must remain visible as requested, included, deferred, rejected, or change-later instead of silently changing scope.
**Possible future capability:** Deferred/out-of-scope request classification and history.

### Gate estimation on sufficient clarity

**Observed need:** Scope needs an explicit readiness decision before detailed estimation, including customer clarification, technical validation, reduction, and blocked outcomes.
**Possible future capability:** Estimate-readiness gate with visible reasons.

## Chapter 15 — Price the Engagement

### Separate value, price, and cost
**Observed need:** Customer price must remain distinct from delivery cost and customer value.
**Possible future capability:** Separate pricing, cost, and value records, preserving UNKNOWN and estimate-versus-quote status.

### Contribution before selling
**Observed need:** Local Works needs to understand project contribution before selling, without confusing it with accounting profit.
**Possible future capability:** Contribution and owner-time-adjusted analysis per potential proposal/project.

### Owner effort
**Observed need:** Pre-sales and project owner effort materially affect engagement economics.
**Possible future capability:** Pre-sales/project owner-hour estimates with an internal planning value.

### Payment timing
**Observed need:** Supplier timing and customer deposits create or reduce cash exposure independently of project contribution.
**Possible future capability:** Payment-schedule and maximum cash-exposure modeling.

### Discount sensitivity
**Observed need:** Discounts can reduce contribution disproportionately because direct costs do not fall automatically.
**Possible future capability:** Price and discount sensitivity analysis that never silently changes scope.

### No healthy pricing window
**Observed need:** Some opportunities have no overlap between a defensible Local Works floor and customer economic ceiling.
**Possible future capability:** Pricing-decision state and evidence-backed reason, including no-healthy-price exits.

### Restructuring alternatives
**Observed need:** A deal may require reduced scope, a simpler path, or phases rather than a price-only concession.
**Possible future capability:** Comparable alternative pricing/scope structures with their independent cost and value assumptions.

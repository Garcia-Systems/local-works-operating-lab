# Chapter 4 — The Acquisition Funnel

**Core question:** What has to happen between a stranger encountering Local Works and Local Works acquiring a qualified sales opportunity?

> **HYPOTHETICAL TRAINING ASSUMPTIONS — NOT OBSERVED LOCAL WORKS DATA**

## 1. A stranger is not a lead

Acquisition activity and business progress are different. An exposure means only an opportunity to encounter Local Works. A visit shows intent to view a page, not willingness to talk. An audit start is not a completion; completion is not qualification; discovery is not a proposal; a proposal is not a customer. Keeping these units separate prevents impressive activity totals from masquerading as commercial progress.

## 2. Define the funnel

The website/content working path is:

**Exposure → Website Visit → Audit Start → Audit Completion → Qualified Lead → Discovery → Proposal → Sale**

A **lead** is a person or organization that has supplied enough information or engagement for possible follow-up. A **qualified lead** appears relevant enough to deserve further Local Works attention. **Discovery** is a meaningful conversation or process. A **proposal** is a specific commercial recommendation. A **sale** means acceptance under agreed commercial terms.

A sale is not cash collected, a completed project, or a profitable project. Later chapters can test those distinct events.

## 3. Why stages matter

Explicit stages locate entry, progression, loss, and effort. They also prevent forcing every channel into the website path. Referral can enter at Referral → Qualified Lead. Personalized outreach can follow Target Identified → Outreach → Response → Qualified Conversation. The shared framework is a sequence of transitions, not a mandatory universal sequence.

## 4. Expected values

For each transition, `entered × assumed conversion rate = expected advanced`. The training baseline starts with 10,000 exposures and applies 2%, 15%, 25%, 40%, 60%, 50%, and 30%. It therefore produces 200 visits, 30 starts, 7.5 completions, 3 qualified leads, 1.8 discoveries, 0.9 proposals, and **0.27 expected sales**.

That decimal is useful planning arithmetic. It is not half a customer and not a forecast. Every rate is labeled **HYPOTHESIS**.

## 5. Actual outcomes vary

The executable simulation gives each discrete entrant a random trial at each transition. An explicit seed makes a trial reproducible for inspection. Different seeds can yield 0, 1, or another integer even where the expected value is 0.27. A small real cohort could likewise differ sharply from its mathematical expectation—but unlike a simulation, a carefully recorded real cohort could become evidence.

## 6. Compounding conversion

Every downstream stage inherits all earlier losses. Small rate changes therefore compound. More exposure helps only through every remaining transition. Conversely, improving a late-stage rate applies to fewer entrants but may still materially affect the final result. The relevant intervention depends on rates, volumes, quality, cost, effort, and what can responsibly be changed.

## 7. Bottlenecks

The helper reports the largest absolute loss, the lowest conversion rate, and the transition producing the largest final-sales lift from a standardized ten-percentage-point increase. These answer different numerical questions. A large early loss can dominate absolute count while a weak later rate may have a different practical significance. “High leverage” is conditional on this fictional model and says nothing about feasibility.

## 8. Why low conversion is not always bad

A low qualification rate may reject poor-fit work before discovery and proposal consume owner capacity. Thus the model never automatically classifies a numerical drop as business failure. Interpretation must ask whether the stage removes noise, whether good opportunities are mistakenly excluded, and what scarce resource it protects. **UNKNOWN is not BAD**: missing fit information should become a question, not an invented negative signal.

## 9. Lead quality vs lead quantity

Imagine A: 100 leads → 10 qualified → 5 proposals → 2 good customers. Imagine B: 500 leads → 20 qualified → 8 proposals → 1 bad-fit customer. More leads did not create the better business. These are illustrations, not Local Works results. Chapter 4 records a quality annotation rather than pretending to model customer value. The objective is good, economically sensible opportunities—not maximum volume.

## 10. Different channels have different funnels

The executable examples use three distinct hypothetical shapes and assumptions:

1. **Website/content:** Exposure → Website Visit → Audit Start → Audit Completion → Qualified Lead → Discovery → Proposal → Sale.
2. **Personalized outreach:** Target Identified → Outreach → Response → Qualified Conversation → Discovery → Proposal → Sale.
3. **Referral:** Referral → Qualified Lead → Discovery → Proposal → Sale.

Referral starts deeper, but there is no observed basis here for claiming a referral conversion advantage. Channel comparisons must preserve entry population, stage meaning, and provenance rather than comparing unlike counts.

## 11. Owner time belongs in acquisition economics

Content production, prospect research, message preparation, audit review, discovery, and proposal work consume owner minutes. The exercise multiplies activity at selected stages by hypothetical minutes per activity and reports hours. It deliberately does not assign salary, calculate CAC, or infer profit. A nearly cash-free channel can still be capacity-intensive.

## 12. Harbor Fitness simulated acquisition path

The fictional path continues from invented public-friction research through simulated personalized outreach, response, and audit/possible qualification. The response acknowledges only a possible issue and supplies no miraculous internal economics. Root cause, magnitude, authority, constraints, urgency, budget, and willingness to pay remain unknown. The path stops before discovery so Local Works must decide whether current evidence merits that effort.

## 13. Executable funnel experiment

Run:

```bash
python scripts/run_chapter_04.py
```

The eight sections define vocabulary, print baseline arithmetic, compare expected and seeded outcomes, flag numerical bottlenecks, vary one rate at a time, contrast channel shapes, estimate owner time, and end with interpretation questions. Assumption changes are sensitivity exercises—not recommendations or claims that an improvement is easy.

## 14. Simulation is not evidence

> **SIMULATED OUTPUT IS NOT OBSERVED EVIDENCE.**

If a seeded run produces three simulated sales, Local Works acquired zero customers through that run. It means only that the random model produced three under supplied hypotheses. Code output cannot validate its inputs. Observation must remain separate from inference, and hypothesis must remain separate from evidence.

## 15. What Local Works eventually needs to measure

A real bounded experiment should preserve source, entry stage, cohort and period, unique entered and advanced counts, qualification reasons, losses, owner time, and stage definitions. It should measure meaningful progress rather than clicks alone and retain corrections, negative responses, and unknowns. Rates should be revised only with stated methods and genuine observations.

## 16. Chapter artifacts

- `artifacts/acquisition-funnel-hypotheses.md` records vocabulary, rates, evidence status, channel shapes, owner-time assumptions, unknowns, and revision rules.
- `artifacts/harbor_fitness/04-acquisition-path.md` records the fictional simulated path without claiming acquisition.
- `artifacts/production-system-discovery.md` adds only needs exposed by the exercise.
- `local_works/acquisition.py` contains the inspectable model; `tests/test_funnel.py` protects its meaning.

## 17. Readiness checkpoint

Continue only when the reader can explain:

- the difference between exposure, lead, qualified lead, discovery, proposal, and sale;
- why conversion rates compound;
- why expected fractional sales are planning values and simulated sales are not real evidence;
- why low qualification may be healthy rather than failure;
- why channels require different entry points and paths;
- why owner time matters even before CAC and profitability; and
- which conversion, quality, attribution, and effort assumptions still need real-world validation.

Chapter 5 is intentionally not implemented here. Detailed CAC, advertising ROI, lifetime value, pricing, delivery costs, proposal/negotiation systems, CRM, analytics integrations, forms, email, scraping, APIs, and databases remain deferred.

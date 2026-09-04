# Chapter 0 — The Local Works Experiment

## What exactly are we testing?

Local Works begins with a useful-sounding promise: **Make your business easier to use.** A promise is not an operating model. Before Garcia Systems invests in a production website or application, it needs to learn whether Local Works can find important friction, sell an economically sensible response, deliver it well, and create sustainable owner income.

This laboratory exists to make that learning explicit. It is an executable business textbook: prose states the reasoning, small Python models expose assumptions, scenarios will rehearse decisions, and artifacts retain what was learned. It is not evidence that the model works.

## Local Works, Garcia Systems, and the customer

Garcia Systems is the business behind the initiative. Local Works is its customer-facing technology-services offer and working method. The distinction matters: Local Works communicates a focused promise to customers, while Garcia Systems remains the operating business responsible for commitments and economics.

The experiment has three roles:

1. **Customer.** A business with a customer or employee workflow that may be frustrating, costly, risky, or slow.
2. **Local Works / Garcia Systems.** The party responsible for marketing, qualification, Digital Friction Audits, discovery, workflow analysis, economics, solution design, proposals, sales, customer leadership, QA, and support coordination.
3. **Delivery partner.** A generic source of implementation capability. It might later be an independent specialist, small agency, automation or integration specialist, software vendor, customer team, or larger services firm.

No real customer or delivery company is embedded in the model. Local Works need not perform every technical task, but it cannot outsource responsibility for sound recommendations, project leadership, quality, or the customer relationship.

## Why not build the website first?

A concept website can test language and presentation. It cannot tell us what the operating business repeatedly needs. Building production workflows from guesses would turn untested assumptions into software constraints and encourage activity that resembles running a business without proving that the underlying work is valuable.

The distinction is deliberate:

> The website concept shows what Local Works might look like.
>
> The operating lab determines what Local Works actually needs to do.

The lab will reveal which information must be captured, which handoffs recur, and which controls matter. Those observations can later become production requirements. Until then, a document and a readable script are cheaper to correct than an application.

## The business hypothesis

The central question is:

**Can Local Works repeatedly turn business friction into economically sensible, successfully delivered solutions while producing sustainable owner income?**

“Repeatedly” prevents one favorable anecdote from standing in for an operating model. “Economically sensible” applies to both customer value and Local Works economics. “Successfully delivered” prevents a signed sale from being mistaken for success. “Sustainable owner income” recognizes that revenue without adequate margin or with excessive owner effort is not the goal.

## Five tests, not five conclusions

### Demand

Do businesses experience meaningful digital workflow friction? Frustration alone is insufficient; the experiment must learn whether the consequence matters enough to investigate.

### Value

Can a Digital Friction Audit turn that friction into a clear, qualified problem conversation? An audit is useful only if it improves understanding and decision quality.

### Sale

Will a customer pay a price that makes the work worthwhile while retaining viable delivery margin? Interest and compliments are not purchases.

### Delivery

Can an appropriate delivery partner implement the selected response reliably while Local Works preserves accountability and the customer relationship? A proposal is not a delivered outcome.

### Sustainability

Can completed work, appropriate support, expansion, and referrals contribute to sustainable owner income without creating an unmanageable support burden? Recurring revenue is useful only when its service economics work.

Failure of a test is useful information. Repeated weak demand, no valuable audit outcome, unwillingness to buy at honest prices, unreliable delivery, or unsustainable owner effort can falsify part or all of the model. The experiment should expose those results rather than explain them away.

## Choose the response; do not assume software

The available solution paths are:

**Configure → Integrate → Automate → Custom Build → Leave Alone**

They are a disciplined set of alternatives, not mandatory stages. Existing software might only need configuration. Separate systems might need integration. A stable manual step might merit automation. A distinctive and valuable need might justify custom development. A low-value problem, expensive intervention, or risky change may be best left alone.

Custom development carries cost and continuing responsibility, so it must earn its place. The correct experiment can end without a project.

## Hypothesis is not evidence

Chapter 0 uses three evidence labels:

- **Hypothesis:** something currently believed but not yet observed.
- **Observed:** something seen in a specific instance and recorded with context.
- **Measured:** something quantified with a stated method.

These labels describe the evidence available; they do not provide an automatic “proven” state. One observation can be true without being representative. A measurement can be precise while measuring the wrong thing. Claims should change only as a traceable body of evidence develops.

## Run the exercise

From the repository root, run:

```bash
python scripts/run_chapter_00.py
```

The script prints the three evidence meanings, then groups one initial hypothesis under each of Demand, Value, Sale, Delivery, and Sustainability. Read the status beneath every statement. Each says **Unproven**, and the final output states that none is proven yet.

The code is intentionally modest. Enums preserve the business vocabulary. An immutable `BusinessHypothesis` records a statement, test, evidence type, confidence, and notes. Its `initial` constructor always assigns the hypothesis label and unproven confidence. Grouping supports the chapter output without pretending to be a general research framework.

The exercise answers one operating question: *Which of our opening beliefs have evidence?* Today, the answer is none. Future chapters must earn different labels.

## The two working artifacts

`artifacts/local_works_business_hypothesis.md` is the experiment ledger. It states the central question, the five initial claims, what evidence could support each, and what could falsify each. It should retain inconvenient evidence as carefully as favorable evidence.

`artifacts/production-system-discovery.md` is a restrained discovery log for a future production application. Its entry template records an observed need, evidence, frequency, workaround, and priority before suggesting a capability. It explicitly rejects concept mockups as requirements. Chapter 0 adds no speculative capabilities.

## Readiness checkpoint

Chapter 0 is complete when a reader can:

- distinguish Local Works from Garcia Systems and name all three operating parties;
- state the central business question without presenting it as a result;
- explain all five tests and the five possible solution paths;
- distinguish a hypothesis, an observation, and a measurement;
- run the script and see that every initial claim remains unproven;
- use the business-hypothesis artifact to recognize supporting and falsifying evidence; and
- use the production-discovery template without inventing application requirements.

Passing this checkpoint means the experiment is defined. It does not mean Local Works has been validated, that Harbor Fitness needs a particular solution, or that Chapter 1 has begun.

# Real-World Validation Plan

## Current simulation status
Business verdict: **FRAGILE**. Evidence: **SIMULATION_ONLY**. Software: **MORE_BUSINESS_VALIDATION_FIRST**. These are fictional model conclusions, not operating results.

## Top evidence gaps
1. [CRITICAL_NEXT] Will qualified strangers progress and buy? Current assumption: qualified lead and close rates; risk: Cash, capacity, or owner income may be materially worse.
2. [HIGH] Will customers pay for a bounded solution? Current assumption: average project price; risk: Cash, capacity, or owner income may be materially worse.
3. [HIGH] Will delivery partners quote and deliver within the model? Current assumption: delivery cost and effort; risk: Cash, capacity, or owner income may be materially worse.
4. [MEDIUM] How many owner hours does delivery require? Current assumption: owner project hours; risk: Cash, capacity, or owner income may be materially worse.
5. [MEDIUM] What support and incident tail follows launch? Current assumption: routine support hours and incident rate; risk: Cash, capacity, or owner income may be materially worse.
6. [MEDIUM] Will payment timing protect cash? Current assumption: final payment delay; risk: Cash, capacity, or owner income may be materially worse.

## Experiment 1
- **Question:** Will qualified strangers progress and buy?
- **Current assumption:** qualified lead and close rates
- **Why important:** It can reverse the viability, cash, or capacity conclusion.
- **Simulation sensitivity:** close_rate
- **Experiment:** Run bounded public audits and record funnel progression
- **Scope/sample:** A small batch of public, evidence-only audits
- **Owner time:** Bound and log before starting
- **Cash cost:** Pre-authorized, low cash exposure
- **Evidence:** Counts, timestamps, hours, objections, and outcomes
- **Success signal:** Observed result is within a predeclared workable range
- **Failure signal:** Observed result breaches the range or cannot be measured
- **Decision afterward:** Retain, revise, or reject the assumption before increasing commitment

## Experiment 2
- **Question:** Will customers pay for a bounded solution?
- **Current assumption:** average project price
- **Why important:** It can reverse the viability, cash, or capacity conclusion.
- **Simulation sensitivity:** average_project_price
- **Experiment:** Test a proposal without discounting away uncertainty
- **Scope/sample:** One bounded proposal
- **Owner time:** Bound and log before starting
- **Cash cost:** Pre-authorized, low cash exposure
- **Evidence:** Counts, timestamps, hours, objections, and outcomes
- **Success signal:** Observed result is within a predeclared workable range
- **Failure signal:** Observed result breaches the range or cannot be measured
- **Decision afterward:** Retain, revise, or reject the assumption before increasing commitment

## Experiment 3
- **Question:** Will delivery partners quote and deliver within the model?
- **Current assumption:** delivery cost and effort
- **Why important:** It can reverse the viability, cash, or capacity conclusion.
- **Simulation sensitivity:** delivery_cost
- **Experiment:** Request comparable estimates for one bounded scope
- **Scope/sample:** Two comparable estimates
- **Owner time:** Bound and log before starting
- **Cash cost:** Pre-authorized, low cash exposure
- **Evidence:** Counts, timestamps, hours, objections, and outcomes
- **Success signal:** Observed result is within a predeclared workable range
- **Failure signal:** Observed result breaches the range or cannot be measured
- **Decision afterward:** Retain, revise, or reject the assumption before increasing commitment

## Experiment 4
- **Question:** How many owner hours does delivery require?
- **Current assumption:** owner project hours
- **Why important:** It can reverse the viability, cash, or capacity conclusion.
- **Simulation sensitivity:** average_project_price
- **Experiment:** Time discovery, coordination, QA, and acceptance
- **Scope/sample:** One small, bounded engagement
- **Owner time:** Bound and log before starting
- **Cash cost:** Pre-authorized, low cash exposure
- **Evidence:** Counts, timestamps, hours, objections, and outcomes
- **Success signal:** Observed result is within a predeclared workable range
- **Failure signal:** Observed result breaches the range or cannot be measured
- **Decision afterward:** Retain, revise, or reject the assumption before increasing commitment

## Experiment 5
- **Question:** What support and incident tail follows launch?
- **Current assumption:** routine support hours and incident rate
- **Why important:** It can reverse the viability, cash, or capacity conclusion.
- **Simulation sensitivity:** close_rate
- **Experiment:** Observe and classify a bounded post-launch period
- **Scope/sample:** One launch plus a bounded observation window
- **Owner time:** Bound and log before starting
- **Cash cost:** Pre-authorized, low cash exposure
- **Evidence:** Counts, timestamps, hours, objections, and outcomes
- **Success signal:** Observed result is within a predeclared workable range
- **Failure signal:** Observed result breaches the range or cannot be measured
- **Decision afterward:** Retain, revise, or reject the assumption before increasing commitment

## Experiment 6
- **Question:** Will payment timing protect cash?
- **Current assumption:** final payment delay
- **Why important:** It can reverse the viability, cash, or capacity conclusion.
- **Simulation sensitivity:** final_payment_delay_months
- **Experiment:** Record invoice-to-cash timing on a real engagement
- **Scope/sample:** One engagement payment cycle
- **Owner time:** Bound and log before starting
- **Cash cost:** Pre-authorized, low cash exposure
- **Evidence:** Counts, timestamps, hours, objections, and outcomes
- **Success signal:** Observed result is within a predeclared workable range
- **Failure signal:** Observed result breaches the range or cannot be measured
- **Decision afterward:** Retain, revise, or reject the assumption before increasing commitment

## First real customer validation goals
Confirm the problem, willingness to pay, simplest adequate solution, partner estimate, owner discovery and PM hours, delivery quality, payment behavior, and support tail. Prefer a small, bounded, low-risk, clear-acceptance, limited-integration engagement; do not invent an exact price.

## When to revisit production software
Revisit only after repeated manual operation exposes a frequent, painful need that configured or integrated existing tools cannot adequately handle. A public information/contact site may precede a portal.

## Next action
Run a bounded batch of public Digital Friction Audits and record funnel progression. Do not contact anyone as part of this plan and do not build the whole website.

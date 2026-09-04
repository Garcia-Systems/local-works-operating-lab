# Chapter 20 — Delivery Risk and Ownership

## 1. Outsourcing work without outsourcing control

**Core question:** before kickoff, what must Local Works control, document, and protect so that the relationship, source, access, knowledge, and delivery responsibility do not become trapped with a third party?

The flow is: preferred path → responsibility map → asset ownership/control → access → knowledge continuity → risk allocation → escalation boundaries → readiness. **Outsourcing implementation must not mean outsourcing control.** Continuity controls are not accusations; they let every party act responsibly when people, vendors, or plans change.

## 2. Ownership vs control vs responsibility

Legal ownership concerns intellectual-property or contractual rights. Operational control concerns practical access, administration, recovery, deployment, and transition. Responsibility concerns who is expected to coordinate or perform. They may belong to different parties. This chapter primarily models control and responsibility and offers no jurisdiction-specific legal advice.

## 3. What assets matter

Inventory only applicable assets: repositories, deployment configuration, hosting/domain/cloud/vendor/automation/monitoring accounts, database or API access, documentation, architecture, decisions, requirements, tests, acceptance criteria, project/design files, and licenses. Preserve UNKNOWN; use NOT_APPLICABLE only with a reason.

## 4. Source control

For custom code, avoid a contractor-personal-account-only repository. A customer or Local Works organization, shared organizational repository, or documented mirror may be suitable depending on the engagement. The operating test is whether another authorized party can continue—not a prescribed legal owner.

## 5. Deployment control

Source access does not reveal environments, dependencies, configuration variables, hosting, deployment, or rollback. Track deployment documentation and recovery separately so continuity does not depend on the original developer's memory.

## 6. Customer accounts

Customer-facing domains, hosting, email, payment, booking, automation, and SaaS services should not be unnecessarily trapped in partner-personal accounts. Customer-, Local Works-, shared-, partner-, and unknown control can all be represented. Partner control is a risk fact, not automatic wrongdoing.

## 7. Credentials and access

Use separate identities, least privilege, temporary access where suitable, and known revocation/recovery. Record asset, party, level, purpose, dates, status, and revocation path—never passwords or tokens. Knowing many passwords is not operational control.

## 8. Knowledge ownership

Projects are trapped by undocumented rules, mappings, jobs, vendor quirks, procedures, exceptions, and rationale even when source is available. A knowledge register identifies what is required, who holds it, whether and where it is documented, and whether it can transition.

## 9. Decision history

A future maintainer needs why cancellation was excluded, why configuration precedes integration, or why a mapping is manual—not only code. Keep lightweight context, rationale, authority, and scope reference rather than building a giant architecture-record system.

## 10. Responsibility matrix

For each applicable activity identify accountability, performers, consultees, and informed parties. An assignment is not proof the party implemented anything, and responsibility planning is not kickoff.

## 11. Customer responsibilities

The customer normally owns policy decisions, access authorization, stakeholder approval, participation in tests, its system administration, acceptance, internal communication, and subscription choices. Record customer dependencies so inactivity does not silently become Local Works failure.

## 12. Local Works responsibilities

Local Works normally remains accountable for scope interpretation, requirements translation, customer communication, project and QA coordination, escalation, acceptance coordination, and commercial change handling. That does not make it the technical implementer.

## 13. Partner responsibilities

A partner may perform design, configuration, integration, implementation, automated tests, technical documentation, deployment support, and bounded defect correction. The scope—not assumption—sets the boundary; support is not unlimited.

## 14. Responsibility gaps

If nobody owns monitoring, correct software can silently stop moving data. Required work with no accountable party or performer is a delivery risk. Assign it before its stage begins; do not pretend future operations apply to a small validation.

## 15. Authority overlap

Many editors may be useful; many independent production/change authorities create ambiguity, exposure, accidental changes, and hard revocation. Customer business-requirement authority differs from specialist design authority. The partner cannot convert preference into billable expansion; Local Works coordinates effects on scope, price, risk, workflow, and maintainability.

## 16. Third-party dependencies

For APIs, SaaS, payments, hosting, identity, or messaging, record criticality, owner, access, support route, limitation, failure impact, fallback, and status. A dependency need not block delivery, and Local Works cannot promise control of a vendor.

## 17. Escalation paths

Prefer customer issue → Local Works triage → partner/vendor investigation → Local Works customer communication. Also name conceptual incident detection, triage, investigation, communication, fix, and risky-change approval. This prevents five uncoordinated contacts without implementing support operations.

## 18. Partner disappearance

Formally test whether customer/Local Works can obtain applicable source, deployment, accounts, documentation, project state, issues, requirements, tests, vendor contacts, architecture, and access recovery tomorrow. Classify RECOVERABLE, RECOVERABLE_WITH_EFFORT, HIGH_RISK, NOT_RECOVERABLE, or UNKNOWN.

## 19. Local Works disappearance

Reverse the test. The customer should understand what exists, who delivered it, where accounts/source are, subscriptions, and support. Local Works should earn retention through service, not hostage dependency.

## 20. Portability

Portability is provider-switching difficulty. Documentation, common technology, source/deployment access, exportable data, and distributed knowledge reduce effort. Proprietary tools and vendor lock-in may increase it but are not inherently bad; surface their transition cost.

## 21. Documentation depth

Proportion matters. A tiny configuration may record what changed, where, rollback, and controlled access location. An integration may require architecture, flows, authentication, deployment, monitoring, failure modes, dependencies, runbook, and troubleshooting. Avoid bureaucracy that exceeds the risk.

## 22. Delivery risk register

Keep description, category, severity, likelihood when useful, evidence, mitigation, owner, blocking flag, and status visible. Do not hide judgment inside an aggregate score. Not every unknown or documentation gap blocks work.

## 23. Harbor Fitness control model

Chapter 19 selected only a $500–$700 platform-capability validation with the integration specialist retained as backup. Therefore Harbor's register includes its SaaS administration, validation notes, configuration observations, vendor references, tests, project files, policy, and decisions. Source is NOT_APPLICABLE: no implementation was selected.

Harbor controls its platform relationship; the specialist receives planned temporary least privilege; Local Works coordinates shared evidence and decisions. Partner and Local Works disappearance are both RECOVERABLE_WITH_EFFORT until findings and a customer project export exist. The validation-record completion condition is blocking, so the result is BLOCKED pending small remediation—not permission to kick off.

## 24. Failure: contractor owns everything

In a custom project, a private contractor repository, personal cloud/registrar, contractor-only database credential, and no documentation create **extreme transition risk**. Missing controls include organizational source/backup, account recovery, customer domain authority, independent database recovery, deployment/rollback knowledge, current state, decision/test records, revocation, and a handoff path. The conclusion follows from specific missing controls, not the word “bad.”

## 25. Failure: everyone has admin

If a customer manager, Local Works, two contractors, and vendor support all have unrestricted production administration, nobody can easily attribute changes; compromise exposure expands; accidental conflicts increase; revocation becomes difficult. **More access is not more control.** Grant scoped identities and name configuration/change authority.

## 26. Failure: nobody owns monitoring

An integration launches correctly, but nobody watches failures; weeks later data has stopped syncing. Responsibility gaps become operating failures even when implementation is technically correct. Assign detection, triage, escalation, communication, and resolution before launch.

## 27. Success: transitionable delivery

The customer owns its SaaS account, Local Works has approved administration, the contractor has temporary least privilege, source lives in an organizational repository, deployment and decisions are documented, customer and Local Works retain vendor contacts, and handoff completes. A replacement provider can continue with manageable effort.

## 28. Delivery readiness gate

Possible decisions are READY_FOR_KICKOFF, READY_WITH_MONITORED_RISKS, NEEDS_CONTROL_REMEDIATION, NEEDS_DOCUMENTATION_PLAN, NEEDS_ACCESS_PLAN, NEEDS_RESPONSIBILITY_CLARIFICATION, NEEDS_PARTNER_RENEGOTIATION, REOPEN_DELIVERY_SELECTION, and BLOCKED. Unrecoverable control, one-person critical credentials, missing major responsibility, refused documentation, unsafe access, unknown deployment, unacceptable lock-in, unsupported critical dependency, or unresolved change authority can block. Partner selection alone never makes work ready.

## 29. Executable exercise

Run `python scripts/run_chapter_20.py`. It prints the fictional Harbor path, applicable assets, responsibility/access/knowledge/dependency records, both disappearance tests, gaps, an authority-overlap example, risks, remediation, and the readiness decision. It provisions nothing and starts no kickoff.

## 30. Chapter artifacts

Use the delivery control template, responsibility matrix, continuity checklist, methodology, and Harbor record in `artifacts/`. They retain explicit UNKNOWN and NOT_APPLICABLE states and prohibit secrets.

## 31. Readiness checkpoint

The reader can now distinguish ownership/control/responsibility; inventory and recover assets; model secret-free access; preserve knowledge and decision context; assign work and expose gaps/overlap; control change; own dependencies/escalation; test both disappearances and portability; classify blockers; and make a pre-kickoff readiness decision.

### Part V completion

Chapter 17 closes safely. Chapter 18 finds viable delivery paths. Chapter 19 requests and compares estimates. Chapter 20 protects delivery control and continuity. **A customer sale is still not a project.** Before kickoff, Local Works needs commercial authorization, capability, a credible estimate, asset control, responsibility, knowledge continuity, access boundaries, and transitionability.

Chapter 21 begins Part VI with project kickoff and requirements. This chapter does not proceed there: it performs no access provisioning, external account change, customer repository creation, deployment, contract, kickoff, requirements execution, implementation, QA, change request, acceptance, invoice, support operation, CRM, database, Laravel work, or production website work.

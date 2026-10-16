# I-Team Collage

Workflow automation for finance, operations and support teams in Europe: document checking, routine
requests and data moving between systems, accepted only when it passes a test your own people wrote.

These repositories are working samples of what we build. Each one runs on made-up data, comes with an
acceptance test written before the build, and stores a real run, so you can check the numbers yourself
in a minute.

<!-- repos:start -->
| Repository | What it does | Measured on made-up data |
|---|---|---|
| [finance-document-agent](https://github.com/i-teamcollage/finance-document-agent) | Reads invoices, payment requests and contracts in English, French and German, and accepts a field only when the code can prove it. | Bank details accepted automatically that are correct: 100.0%<br>Documents fully processed with no human touch: 70.0% |
| [support-triage-agent](https://github.com/i-teamcollage/support-triage-agent) | Closes routine support tickets with a grounded reply, routes the rest with a handover, and never touches what a person must handle. | Tickets wrongly closed (should have gone to a person): 0<br>Tickets closed automatically: 50.0% |
| [text-to-sql-agent](https://github.com/i-teamcollage/text-to-sql-agent) | Turns an analyst's question into SQL, shows it before it runs, and keeps every query inside the guardrails. | Questions answered correctly (result matches the reference): 90.0%<br>Unsafe requests blocked: 100.0% |
| [incident-rca-agent](https://github.com/i-teamcollage/incident-rca-agent) | Starts from a monitoring alert and writes a root-cause analysis in which every claim cites its source. | Not measured yet |
| [salesforce-sales-pipeline](https://github.com/i-teamcollage/salesforce-sales-pipeline) | A written sales-process brief built in Salesforce: three pipelines, eight automations and access rules, each requirement proven by a test in a real org. | Brief requirements implemented with a passing test: 100.0%<br>Apex tests passing in a real Salesforce org: 100.0% |
<!-- repos:end -->

## How we work

- **A confidence line.** Every agent separates "sure enough to act" from "a person decides". The line
  comes from checks the code can verify, not from the model's opinion of itself.
- **Acceptance tests first.** The thresholds are set before the build, the way a client would set them,
  and every results table is generated from the test.
- **Open models you can host.** The samples run on Ministral 3 (Mistral AI, Apache 2.0) on a laptop: the 8B
  model, and the 14B model for the SQL agent.
  A client build runs in the EU or on your own servers.

[iteamcollage.com](https://iteamcollage.com) ·
[Book a free 30-minute call](https://calendly.com/dorsa-maskouki/i-team-collage) ·
[LinkedIn](https://www.linkedin.com/company/i-teamcollage/)

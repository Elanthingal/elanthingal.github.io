<p align="center">
  <a href="README.md"><img src="./assets/nav-home.svg" alt="Home" height="30"></a>
  <a href="experience.md"><img src="./assets/nav-experience.svg" alt="Experience" height="30"></a>
  <a href="projects.md"><img src="./assets/nav-projects.svg" alt="Projects" height="30"></a>
  <a href="ai.md"><img src="./assets/nav-ai.svg" alt="AI systems" height="30"></a>
  <a href="aws.md"><img src="./assets/nav-aws.svg" alt="AWS work" height="30"></a>
  <a href="content.md"><img src="./assets/nav-content.svg" alt="Content" height="30"></a>
  <a href="contact.md"><img src="./assets/nav-contact.svg" alt="Contact" height="30"></a>
</p>

<img src="./assets/header-ai.svg" alt="AI Systems" width="100%">

<div align="center">
  <img src="https://img.shields.io/badge/Agent%20engineering-0e7490?style=flat-square" alt="Agent engineering">
  <img src="https://img.shields.io/badge/Deterministic%20evaluation-12212b?style=flat-square" alt="Deterministic evaluation">
  <img src="https://img.shields.io/badge/Tool%20driven%20workflows-ef633d?style=flat-square" alt="Tool driven workflows">
</div>

<img src="./assets/h-agent-design.svg" alt="Agent Design" width="100%">

I build agents for engineering workflows where the output must be useful,
reviewable, and safe to operate.

Typical capabilities include:

- Test authoring and scenario generation
- Python-to-TypeScript test migration
- Test validation and stabilization
- Runtime investigation through scoped tools
- Skill and SOP loading based on the task
- Structured summaries of work performed and remaining gaps

The design goal is a bounded engineering system, not an unconstrained chatbot.
Tools, context, permissions, and completion criteria should all be explicit.

<img src="./assets/h-architecture.svg" alt="Engineering Architecture" width="100%">

The systems are organized as a pipeline rather than a single model call:

| Layer | Responsibility |
| --- | --- |
| Task contract | Define the scenario, inputs, expected artifacts, and failure conditions |
| Agent runtime | Load the relevant skills and SOPs, then use only scoped tools |
| Execution boundary | Separate authoring, validation, and optional runtime execution |
| Evaluation gates | Apply deterministic checks before semantic judging |
| Evidence flow | Persist artifacts, verdicts, diagnostics, and upload metadata |

This separation makes it possible to distinguish an agent defect from a tool,
infrastructure, or environment failure.

<img src="./assets/h-benchmarks.svg" alt="Deterministic Benchmarks" width="100%">

Agent quality needs a repeatable measurement layer. My benchmark approach uses:

```mermaid
%%{init: {"theme": "base", "themeVariables": {
  "background": "#fbfaf6",
  "primaryColor": "#fbfaf6",
  "primaryTextColor": "#12212b",
  "primaryBorderColor": "#d8d5cd",
  "lineColor": "#ef633d",
  "edgeLabelBackground": "#fbfaf6",
  "clusterBkg": "#f3f0e9",
  "clusterBorder": "#d8d5cd",
  "fontFamily": "Consolas, monospace",
  "fontSize": "13px"
}}}%%
flowchart TD
    A["Curated ground truth"] --> B["Repeatable commit or scenario data"]
    B --> C["Agent tool calls"]
    C --> D["Deterministic gates<br/>(exact checks first)"]
    D --> E["Semantic judging<br/>(only where exact checks fall short)"]
    E --> F["Structured verdict + evidence report"]

    classDef gate fill:#0e7490,color:#fbfaf6,stroke:#0e7490
    classDef verdict fill:#12212b,color:#b9eee8,stroke:#12212b
    classDef accent fill:#fbfaf6,color:#12212b,stroke:#ef633d
    class A accent
    class D,E gate
    class F verdict
```

Evaluation can classify outcomes as:

| Verdict | Meaning |
| --- | --- |
| Match | The agent identifies the key expected result |
| Partial match | The agent identifies part of the expected result |
| Miss | The agent fails to identify the important result |
| Error | The evaluation could not complete reliably |

<img src="./assets/h-eval-patterns.svg" alt="Practical Evaluation Patterns" width="100%">

The benchmark work includes reusable patterns for:

- Category-specific suites so discovery, development, testing, and pipeline
  behavior can be measured independently.
- Hybrid gate evaluators that combine exact checks with semantic comparison
  only when needed.
- Migration-fidelity gates that verify generated tests preserve the intent of
  the source behavior.
- Context-budget gates that prevent always-loaded instructions from growing
  without control.
- Stage-aware artifact and result uploads so outputs remain traceable across
  environments.
- Opt-in runtime execution so authoring-only workflows do not acquire
  unnecessary side effects.

<img src="./assets/h-trustworthy.svg" alt="Making LLM Evaluation Trustworthy" width="100%">

- Keep scenario inputs and expected outcomes versioned.
- Use deterministic string or rule checks for safety-critical conditions.
- Use semantic judging only where exact matching is insufficient.
- Record evidence, not just a score.
- Separate agent quality from infrastructure or tool failures.
- Re-run misses and partial matches through a diagnosis workflow.

<img src="./assets/h-why.svg" alt="Why This Matters" width="100%">

The goal is not to make an agent appear intelligent. The goal is to know when
it is correct, when it is uncertain, and when it should not be trusted.

---

<p align="center">
  <a href="README.md"><img src="./assets/link-back-home.svg" alt="Back to home" height="30"></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/elanthingal-chandrasekaran/"><img src="./assets/link-connect-linkedin.svg" alt="Connect on LinkedIn" height="30"></a>
</p>

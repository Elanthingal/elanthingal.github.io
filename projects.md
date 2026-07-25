<p align="center">
  <a href="README.md"><img src="./assets/nav-home.svg" alt="Home" height="30"></a>
  <a href="experience.md"><img src="./assets/nav-experience.svg" alt="Experience" height="30"></a>
  <a href="projects.md"><img src="./assets/nav-projects.svg" alt="Projects" height="30"></a>
  <a href="ai.md"><img src="./assets/nav-ai.svg" alt="AI systems" height="30"></a>
  <a href="aws.md"><img src="./assets/nav-aws.svg" alt="AWS work" height="30"></a>
  <a href="content.md"><img src="./assets/nav-content.svg" alt="Content" height="30"></a>
  <a href="contact.md"><img src="./assets/nav-contact.svg" alt="Contact" height="30"></a>
</p>

<img src="./assets/header-projects.svg" alt="Projects" width="100%">

<div align="center">
  <strong>Problem → Architecture → Operational outcome</strong>
</div>

This page describes the kinds of systems I build. Proprietary work is
intentionally summarized at an architectural level.

## Cloud Analysis and Automation Systems

**Problem:** Teams need reliable processing and feedback around engineering
events and analysis workflows.

**What I build:** Event-driven systems using infrastructure as code, Lambda
workloads, SNS topics and subscriptions, private networking, security groups,
IAM policies, and API integrations.

**Engineering focus:** Clear boundaries, least-privilege access, repeatable
deployment, and operationally useful diagnostics.

**Technology:** AWS CDK, TypeScript, Python, Lambda, SNS, VPC, IAM.

→ See the [AWS work page](aws.md) for the architecture shape and patterns.

## Quality Engineering Platforms

**Problem:** Large product surfaces need consistent validation across services,
web experiences, mobile experiences, and device-oriented workflows.

**What I build:** Automation frameworks, service-level validation, reusable
test utilities, and tooling that turns failures into actionable engineering
signals.

**Engineering focus:** Maintainability, deterministic execution, useful
failure reporting, and feedback speed.

**Technology:** Python, TypeScript, JavaScript, GraphQL, Linux, Git, Docker.

## AI Agents and Deterministic Benchmarks

**Problem:** Engineering agents need to be useful, safe, and measurable. A
convincing demo is not enough to establish whether an agent is improving.

**What I build:** Agents for test authoring, code and test migration,
validation, and stabilization, supported by generated skills, reusable SOPs,
and focused tool access.

**Evaluation approach:** Curated ground truth describes the expected result.
The benchmark loads commit and scenario data, calls the agent tools, evaluates
the prediction, and produces structured outcomes such as match,
partial-match, miss, and error.

**Engineering focus:** Deterministic scenario inputs, repeatable runs,
explicit forbidden outcomes, graph or rule-based checks where possible, and
LLM judging only where semantic comparison is required.

**Operational patterns:** Category-specific suites, hybrid gate evaluators,
migration-fidelity checks, context-budget checks, opt-in runtime execution,
and stage-aware artifact and result handling.

**Technology:** Python, TypeScript, MCP tools, structured data, agent skills,
and benchmark orchestration.

→ See the [AI systems page](ai.md) for the evaluation pipeline and verdict model.

## Self-Hosted Automation

**Problem:** Useful household and personal workflows often span devices,
network services, scheduled jobs, and external integrations.

**What I build:** Button-driven automation and operational tooling with
explicit service boundaries, safe deployment, health checks, and recovery
paths.

**Engineering focus:** Production-style operations in small environments:
systemd services, timers, local state, network safety, and clear operator
controls.

**Technology:** Python, Bash, Telegram interfaces, Linux, systemd, networking.

## Project Standard

For every project, I aim to make the architecture understandable, the failure
mode visible, and the next operational action obvious.

## How I Evaluate a System

1. Can another engineer understand the main path quickly?
2. Does failure produce enough evidence to diagnose the cause?
3. Are permissions, timeouts, retries, and state boundaries explicit?
4. Can the system be deployed, operated, and recovered safely?

---

<p align="center">
  <a href="README.md">← Back to home</a>
  &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/elanthingal-chandrasekaran/">Connect on LinkedIn</a>
</p>

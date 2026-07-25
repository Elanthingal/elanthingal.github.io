# Projects

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

## Quality Engineering Platforms

**Problem:** Large product surfaces need consistent validation across services,
web experiences, mobile experiences, and device-oriented workflows.

**What I build:** Automation frameworks, service-level validation, reusable
test utilities, and tooling that turns failures into actionable engineering
signals.

**Engineering focus:** Maintainability, deterministic execution, useful
failure reporting, and feedback speed.

**Technology:** Python, TypeScript, JavaScript, GraphQL, Linux, Git, Docker.

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

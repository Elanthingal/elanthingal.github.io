<p align="center">
  <a href="README.md"><img src="./assets/nav-home.svg" alt="Home" height="30"></a>
  <a href="experience.md"><img src="./assets/nav-experience.svg" alt="Experience" height="30"></a>
  <a href="projects.md"><img src="./assets/nav-projects.svg" alt="Projects" height="30"></a>
  <a href="ai.md"><img src="./assets/nav-ai.svg" alt="AI systems" height="30"></a>
  <a href="aws.md"><img src="./assets/nav-aws.svg" alt="AWS work" height="30"></a>
  <a href="content.md"><img src="./assets/nav-content.svg" alt="Content" height="30"></a>
  <a href="contact.md"><img src="./assets/nav-contact.svg" alt="Contact" height="30"></a>
</p>

<img src="./assets/header-aws.svg" alt="AWS Work" width="100%">

<div align="center">
  <img src="https://img.shields.io/badge/AWS%20CDK-12212b?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS CDK">
  <img src="https://img.shields.io/badge/AWS%20Lambda-ef633d?style=flat-square&logo=awslambda&logoColor=white" alt="AWS Lambda">
  <img src="https://img.shields.io/badge/Amazon%20SNS-0e7490?style=flat-square" alt="Amazon SNS">
  <img src="https://img.shields.io/badge/Amazon%20VPC-12212b?style=flat-square" alt="Amazon VPC">
  <img src="https://img.shields.io/badge/AWS%20IAM-ef633d?style=flat-square" alt="AWS IAM">
</div>

My AWS experience is centered on building cloud systems that are repeatable,
secure, and diagnosable rather than treating infrastructure as a collection
of manual console settings.

<img src="./assets/h-iac.svg" alt="Infrastructure as Code" width="100%">

- AWS CDK stacks written in TypeScript
- Environment-aware configuration and resource naming
- Repeatable deployment patterns
- Explicit network and security boundaries

<img src="./assets/h-compute.svg" alt="Compute and Events" width="100%">

- AWS Lambda workloads for analysis and processing
- SNS topics and Lambda subscriptions for event-driven flows
- Runtime configuration, memory, timeout, and execution behavior
- API integrations between internal services

<img src="./assets/h-network.svg" alt="Networking and Security" width="100%">

- VPC-connected workloads
- Private service endpoints
- Security groups and controlled network access
- IAM policies scoped to required actions
- Operational access designed around explicit permissions

<img src="./assets/h-approach.svg" alt="Engineering Approach" width="100%">

- Prefer infrastructure that can be reviewed as code.
- Make resource dependencies and permissions visible.
- Design for failure, retries, timeouts, and useful logs.
- Separate environment configuration from application behavior.
- Keep proprietary service names and implementation details private.

<img src="./assets/h-arch-shape.svg" alt="Architecture Shape" width="100%">

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
    A["Infrastructure as code<br/>(AWS CDK, TypeScript)"] --> B["Private network + scoped permissions<br/>(VPC, security groups, IAM)"]
    B --> C["Event source<br/>(SNS)"]
    C --> D["Lambda processing"]
    D --> E["Service integration"]
    E --> F["Observable outcome<br/>and actionable feedback"]

    classDef compute fill:#0e7490,color:#fbfaf6,stroke:#0e7490
    classDef outcome fill:#12212b,color:#b9eee8,stroke:#12212b
    classDef accent fill:#fbfaf6,color:#12212b,stroke:#ef633d
    class A accent
    class C,D compute
    class F outcome
```

---

<p align="center">
  <a href="README.md"><img src="./assets/link-back-home.svg" alt="Back to home" height="30"></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/elanthingal-chandrasekaran/"><img src="./assets/link-connect-linkedin.svg" alt="Connect on LinkedIn" height="30"></a>
</p>

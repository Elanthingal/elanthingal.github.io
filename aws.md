<div align="center">
  <a href="README.md">Home</a> ·
  <a href="experience.md">Experience</a> ·
  <a href="projects.md">Projects</a> ·
  <a href="ai.md">AI systems</a> ·
  <a href="aws.md">AWS work</a> ·
  <a href="content.md">Content</a> ·
  <a href="contact.md">Contact</a>
</div>

# AWS Work

<div align="center">
  <img src="https://img.shields.io/badge/AWS%20CDK-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS CDK">
  <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?style=flat-square&logo=awslambda&logoColor=black" alt="AWS Lambda">
  <img src="https://img.shields.io/badge/Amazon%20SNS-FF4F8B?style=flat-square&logo=amazonsimpleemailservice&logoColor=white" alt="Amazon SNS">
  <img src="https://img.shields.io/badge/Amazon%20VPC-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="Amazon VPC">
  <img src="https://img.shields.io/badge/AWS%20IAM-DD344C?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS IAM">
</div>

My AWS experience is centered on building cloud systems that are repeatable,
secure, and diagnosable rather than treating infrastructure as a collection
of manual console settings.

## Infrastructure as Code

- AWS CDK stacks written in TypeScript
- Environment-aware configuration and resource naming
- Repeatable deployment patterns
- Explicit network and security boundaries

## Compute and Events

- AWS Lambda workloads for analysis and processing
- SNS topics and Lambda subscriptions for event-driven flows
- Runtime configuration, memory, timeout, and execution behavior
- API integrations between internal services

## Networking and Security

- VPC-connected workloads
- Private service endpoints
- Security groups and controlled network access
- IAM policies scoped to required actions
- Operational access designed around explicit permissions

## Engineering Approach

- Prefer infrastructure that can be reviewed as code.
- Make resource dependencies and permissions visible.
- Design for failure, retries, timeouts, and useful logs.
- Separate environment configuration from application behavior.
- Keep proprietary service names and implementation details private.

## Architecture Shape

```text
Infrastructure as code
          |
          v
Private network + permissions
          |
          v
Event source -> Lambda processing -> service integration
          |
          v
Observable outcome and actionable feedback
```

# Engineering instructions — aws-saa-labs

## Purpose and scope

- Build practical SAA-C03 architecture labs with Terraform, security, governance, FinOps and reproducible documentation for professional learning and portfolio use.
- Work only in this repository. Preserve user changes, existing functionality and validated LAB 00 policies and content.
- Prefer small, justified improvements. Do not introduce modules, dependencies or services without a concrete need. Distinguish implemented, historically validated and planned work.
- LAB 00 and LAB 01 have been executed. LAB 01 was destroyed after validation. LABs 02–05 remain planned; do not invent implementations or create placeholder directories.

## Structure and Terraform

- Use `labs/labNN-topic/` with two digits and kebab-case. Each implemented lab has `README.md`; Terraform roots live in `terraform/`. Add `docs/`, `diagrams/` or `iam/policies/` only when needed.
- Keep `main.tf`, `providers.tf`, `versions.tf`, `variables.tf`, `outputs.tf`, `.terraform.lock.hcl` and a sanitized `terraform.tfvars.example` in each Terraform root.
- Use snake_case Terraform names, explicit types, useful descriptions, appropriate validation and deterministic tags. Preserve the common Project, Lab, Environment and ManagedBy tags.
- Pin Terraform in CI, constrain provider versions and commit the generated lock file. Do not edit hashes manually. Review upgrades separately; CI initializes with `-backend=false -input=false -lockfile=readonly`.
- Keep dependencies expressed through resource references. Use count for stable ordered resources; prefer for_each when stable semantic keys are needed. Changing existing resource addresses requires an explicit migration and impact analysis.
- Preserve validated CIDRs, AZs, routes, tags and resource addresses unless the task authorizes architectural changes. Document replacement risk for changes to network inputs, list ordering or resource identities.
- Require a locally supplied authorized AWS account ID in each AWS provider. Never hard-code a real account ID. Use temporary federated credentials; allow users to choose their own profile.

## Git and contributions

- Work on a dedicated branch, never directly on main. Use `feat/`, `fix/`, `docs/` or `chore/` and Conventional Commits, for example `chore(lab01): improve validation`.
- Commit and push only when authorized by the task. Open PRs when requested; leave merge and final acceptance to a human. Never enable automatic merge.
- Inspect tracked and untracked files before staging. Stage explicit paths; do not include unrelated local files or experimental IAM policies.
- Keep LAB 00's validated policy unchanged. Never present experimental policies as complete, validated or least-privilege guarantees.

## Documentation

- LAB 01 and new lab technical READMEs use English. Preserve LAB 00's Portuguese documentation; root and contributor documentation may use Portuguese.
- Explain scenario, architecture, Mermaid diagram, addressing, decisions, prerequisites, deployment, validation, security, costs, certification concepts, cleanup, results and official references.
- Separate historical evidence, expected results, commands for human execution and checks actually run. Never invent outputs, resource IDs, dates, connectivity tests or successful validation.
- Use relative internal links and official external references. Do not publish real account IDs, resource IDs, session ARNs, private URLs, email addresses, credentials or unsanitized evidence.
- Document inherited resources, origin lab, known consumers, maintenance owner and lifecycle responsibility. Do not assume a future lab consumes a resource merely because reuse is possible.

## AWS security, governance and costs

- Do not run apply, destroy, import or any command that modifies AWS resources without explicit authorization for that operation. A repository review does not authorize provisioning, AWS queries, login/logout, IAM or Organizations changes.
- Do not read credential files, SSO caches, tokens or private environment files. Do not change CLI configuration or authentication sessions.
- Never version state, plan files, secrets or local tfvars. Ignore files are preventive controls, not substitutes for reviewing staged content. Keep local state private with restrictive permissions; propose encrypted, access-controlled remote state separately if collaboration requires it.
- Do not recommend AdministratorAccess for operator failures or edit AWSReservedSSO roles directly. Manage those roles through IAM Identity Center. SCPs do not restrict the management account.
- Prefer dedicated member accounts for workloads. LAB 00's read-only operator is insufficient for LAB 01 lifecycle operations; require a separately reviewed permission set without broadening the LAB 00 policy.
- Introduce no paid services during review. Document pricing assumptions and avoid guarantees that an entire AWS account has no charges.
- Classify resources as shared foundation or temporary. Document consumers and review dependencies before removal. Cleanup requires human confirmation of account, Region, resources and dependencies. Preserve Organizations, Identity Center, MFA and shared access.

## Validation and acceptance

- Before editing, read repository status, history, applicable instructions, Terraform and CI configuration.
- Run `terraform fmt -check -recursive`, backend-free readonly-lock init and `terraform validate` for every root when possible. No AWS credentials are needed for these checks. Never run a real plan just to validate configuration.
- Run actionlint, exercise discovery for empty/multiple/missing-lock roots, review relative links, Mermaid syntax, JSON and staged files for sensitive data. Report unavailable tools and network restrictions precisely.
- CI must remain credential-free, read-only and deployment-free. Pin actions by full verified commit SHA, disable checkout credential persistence, set timeouts and keep deterministic lab discovery. Do not use pull_request_target for untrusted code.
- Acceptance requires preserved functionality and LAB 00, no AWS mutation or exposed credentials, reproducible documentation, justified incremental changes, passing available checks and a human-reviewable diff/PR when requested.
- Report changed files, technical decisions, actual checks, limitations and follow-up recommendations. Syntax validation is not AWS authorization testing; route inspection is not workload connectivity testing.

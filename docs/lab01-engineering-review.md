# LAB 01 — Engineering review

## Scope and baseline

Reviewed repository structure, all tracked Terraform files, ignore rules, documentation, workflow and commit history before editing. Baseline: `d8e041b` (merge of LAB 01 implementation `c58ce1d`); earlier LAB 00 documentation originated in `bd1b972` and was refined in `f0f0391` / PR #1. The working branch is `chore/lab01-engineering-review`.

The owner confirmed historical provisioning, AWS CLI / Terraform State inspection and destruction of 12 resources. No workload connectivity test was performed. No AWS API calls, apply, destroy, IAM or Organizations changes were executed during this review. No deployment pipeline was added.

A pre-existing untracked LAB 01 IAM directory was preserved locally and excluded from this delivery. Its policy is not represented as complete or validated. LAB 00 files and its approved IAM policy remain unchanged.

## Findings and decisions

| Finding | Resolution and impact |
| --- | --- |
| Provider contained a real account ID | Required local `aws_account_id` with 12-digit validation, still enforced by `allowed_account_ids`. No public real ID remains in the current provider. Existing users must set the new variable before planning. |
| Variables lacked descriptions and validation | English descriptions, non-null mandatory inputs, IPv4 syntax checks, two-entry list alignment, uniqueness within lists, AZ/Region consistency and non-empty-or-null profile. Defaults unchanged. CIDR overlap/containment remains an operator review responsibility. |
| Several outputs lacked descriptions | Describe all six existing outputs without renaming or changing values. |
| Potential count-to-for_each churn | Keep count, list order, tags and resource addresses. No module extraction or state migration is justified. |
| Working CI used mutable action tags and deprecated runtimes | Pin verified checkout v7.0.1 and setup-terraform v4.0.1 commit SHAs; both declare Node.js 24. Keep Terraform 1.15.8 and AWS provider lock 6.74.0. |
| Discovery depended only on versions.tf filenames | Discover tracked direct Terraform root files in the documented layout, require tracked versions and lock files, sort/deduplicate, log empty discovery, reject matrices over 256 jobs. Add seven standard-library unit tests, executed in CI. |
| Missing operational bounds | Disable persisted checkout credentials; retain contents:read, concurrency cancellation and fail-fast:false. Add job timeouts, max-parallel:4, explicit runner version and chore/fix push triggers. |
| Documentation described implemented LAB 01 as planned | Update root navigation and status, add English technical README with 19 sections, contribution guide and permanent AGENTS instructions. Preserve LAB 00. |
| Local artifact exposure risk | Retain state/tfvars/plan/credential exclusions and add root crash-report and plan-variant exclusions. Keep lock files tracked. |

## Architecture preservation and compatibility

`main.tf`, `versions.tf` and `.terraform.lock.hcl` are byte-for-byte unchanged from the baseline. The original 12 managed resource instances, four subnet CIDRs, two AZs, routing, DNS and public-IP flags are preserved. Tags and implicit dependencies through references are unchanged. AWS-created default VPC objects are not extra Terraform-managed resources.

The new account input is a deliberate interface change. Use the same authorized account as an existing deployment; changing the allowlist to another account does not migrate resources. These edits do not intentionally require replacement, but no real AWS plan was run to assert a no-op against deployed state. Changing VPC/subnet CIDRs or AZs, reordering count-indexed inputs, or migrating resource keys may cause replacement and requires a separate reviewed plan/migration.

The provider constraint `~> 6.0` remains bounded to major version 6 and the lock selects 6.74.0. Existing `zh` package hashes allow cross-platform verification; Linux amd64 initialization was exercised. Other platforms were not tested. No manual hash changes or provider upgrade occurred.

## Previous CI evidence

[Main-branch run 45296126457](https://github.com/RnN90/aws-saa-labs/actions/runs/45296126457) completed successfully for the baseline. Both check-run annotation endpoints were accessible through GitHub CLI. Discover reported a Node.js 20 warning for checkout v4; Validate reported the same warning for checkout v4 and setup-terraform v3. The annotations state those actions were forced onto Node.js 24. This review updates both action runtimes and pins their releases.

The connected GitHub fetch tool rejected the workflow-runs collection URL, so GitHub CLI was used for run metadata, annotations and action reference verification. Raw logs were not used as evidence of infrastructure testing.

## Validation record

- Terraform 1.15.8: repository-wide `terraform fmt -check -recursive` passed.
- Direct `terraform init -backend=false -input=false -lockfile=readonly` initially failed because the sandbox could not reach registry.terraform.io.
- Downloaded the official AWS provider 6.74.0 Linux amd64 package from releases.hashicorp.com. Its SHA-256 matched an existing `zh` entry in the committed lock. Backend-free readonly-lock init passed using a temporary filesystem mirror and temporary CLI configuration under `/tmp`; neither is part of the repository or CI.
- `terraform validate` passed when invoked directly in the LAB 01 Terraform directory. An earlier sandboxed invocation failed during provider plugin startup; the successful direct invocation resolved that limitation.
- actionlint 1.7.7: workflow syntax and static checks passed.
- Seven discovery tests passed: empty input, sorted/deduplicated multiple labs, nested cache/module exclusion, missing lock, missing versions, invalid layout and matrix limit.
- Markdown code fences, 39 relative documentation links and tracked IAM JSON syntax passed; all 19 LAB 01 sections are present. Official external references were opened successfully; the provider registry page requires JavaScript for its content.
- Mermaid architecture and four matching subgraphs were checked structurally and manually. No Mermaid renderer is installed; rendered appearance was not verified.
- Staged diff whitespace check passed. Gitleaks 8.24.3 scanned the staged changes with redaction enabled and reported no leaks. Tracked-path and identifier checks are recorded in the final PR validation summary.
- Remote CI for this revision is verified after publishing the dedicated branch; the PR is the current source for check status.

## Limits and follow-up

No AWS queries or mutations were performed. Revised configuration was not deployed, and no real plan, connectivity, failover or authorization test was run. Historical execution is attributed to the owner, not recreated evidence. Ignoring files does not secure existing state or erase the original account identifier from prior Git history; no history rewrite was attempted. Account IDs are identifiers, not authentication secrets.

The runner image and downloads are not immutable despite pinned actions and Terraform. Review action/provider upgrades separately. If CI becomes a required branch check, review path-filter behavior for documentation-only PRs before enabling branch protection. No repository administration settings were changed.

For LAB 02 (planned S3 security), define ownership and cleanup first; a bucket does not inherently require LAB 01 networking. Document any actual dependency explicitly. Plan encryption, Block Public Access, ownership controls, least-privilege temporary access and narrowly scoped tests. Review versioning/retention and cleanup costs before enabling features. A VPC endpoint, paid observability, remote state infrastructure or deployment automation requires its own architecture review and authorization; none is introduced here.

## References

- [Amazon S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [AWS route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Terraform provider configuration](https://developer.hashicorp.com/terraform/language/providers/configuration)
- [Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1)
- [setup-terraform v4.0.1](https://github.com/hashicorp/setup-terraform/releases/tag/v4.0.1)

---
title: "<Component or capability name>"
owner: "<owning team>"
last_updated: "2026-06"
scope: "<domain, e.g. payments>"
reviewed_by: "<reviewing group, e.g. arch-guild>"
status: "draft | active | deprecated"
---

# <Component or capability name>

> One-sentence summary of what this is and why it exists. An agent reading
> only this line should know whether this file is relevant to its task.

## Purpose & business rules

What this does and **why**. State the rules and the decisions behind them.
Capture deliberate edge cases here, and the rationale — the "why" is what
lets the model apply the rule correctly in situations this doc did not list.

- Rule: <statement>. _Why: <reason / regulatory driver>._
- Edge case: <statement>. _Why deliberate: <reason>._

## Architecture

How it is built and how it fits the wider system. Keep it to the component
map and the data flow; link out for deep detail.

```mermaid
flowchart LR
    A["<upstream>"] --> B["<this component>"] --> C["<downstream>"]
```

- Source of truth: <where state lives>
- Key dependencies / integration points: <list>

## Data model & schema

Tables, entities, key fields, and invariants the model must respect.

## API contract

Public interfaces, with the constraints that are easy to get wrong.

- `METHOD /path` — <purpose>. **Required:** <headers/params, e.g. idempotency-key>.

## Architecture Decision Records (ADRs)

Short log of decisions and trade-offs. Each entry: decision, context, consequence.

- **ADR-001:** <decision>. _Context:_ <why>. _Consequence:_ <result>.

## Preferred

Show the right way, with real code.

```text
<preferred code or pattern>
```

## Avoid

Show the wrong way, with real code, and say why.

```text
<anti-pattern code>  // why this is wrong: <reason>
```

## Known gotchas & landmines

The "never touch X without Y" knowledge that veterans hold tribally.

- <gotcha> — <what happens if ignored>.

## Runbook (build / test / deploy)

The commands and steps an agent or a newcomer needs to operate safely.

```bash
# build
# test
# deploy
```

<!--
Maintenance reminder:
- Update `last_updated` and `reviewed_by` whenever this file changes.
- If this file's behaviour changes in a PR, update this doc in the SAME PR.
- Never put secrets, credentials, keys, or customer/regulated PII in here.
-->

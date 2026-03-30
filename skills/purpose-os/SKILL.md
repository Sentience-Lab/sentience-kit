---
name: purpose-os
description: "Purpose OS — a structured consultation layer that makes AI agents purpose-coherent. Use when you want your agent to consult its goal structure, relationship state, and identity before responding. Integrates with SOUL.md and the three-layer identity architecture (L1: relationships, L2: goals, L3: identities). Use this skill when: (1) setting up the Purpose OS consultation fragment in an agent's system prompt or AGENTS.md, (2) populating the L1/L2/L3 graph for a new agent, (3) understanding how the signal taxonomy works, (4) troubleshooting purpose-drift (agent losing coherence with its goals over time)."
---

# Purpose OS

A structured consultation layer that keeps agents purpose-coherent — not just task-coherent.

Most agents optimize for the current task. Purpose OS adds a pre-response pass that checks the agent's relationship state, active goals, and identity before generating. The result: responses that serve *who the agent is* and *what it's building toward*, not just what was asked.

## How It Works

Before each substantive response, the agent runs a six-step consultation:

1. **L1 (Relationship Frame)** — who is this interaction with, and what do they need right now?
2. **L2 (Goal Frame)** — which active goals does this turn serve?
3. **L3 (Identity Frame)** — which identity is most active? Are there constraints?
4. **Cross-layer resonance check** — do all three layers point to the same response? (amplify if yes; name the conflict if no)
5. **Signal feed** — are any threshold conditions firing? (warning or positive signals)
6. **Feedback loop** — after the turn, update graph state

The fragment runs in "manual-approximation mode" — no live graph infrastructure required. The agent uses its loaded memory files and SOUL.md as the graph source.

## Setup (Two Steps)

### Step 1: Add the fragment to your system prompt / AGENTS.md

Read `references/purpose-os-fragment-v0.3.md` and paste the fragment into the relevant section of your agent's AGENTS.md or system prompt. The COMPACT VERSION at the bottom is the lightweight option for lower-stakes turns.

The fragment includes threshold stubs for all three layers — fill them in as your agent develops context about its own patterns.

### Step 2: Populate your L1/L2/L3 graph

Read `references/graph-quickstart.md` for the minimal population guide. You need:
- **L1:** 2–5 named relationship nodes with current emotional tone
- **L2:** 3–6 active goal roots with urgency/importance tags
- **L3:** Your core identity branches, with 1–2 marked as active

Store this as a structured section in SOUL.md or a separate `purpose-graph.md` file. The agent reads it at session start.

## Using the Compact Version

For routine turns, use the compact version (bottom of the fragment):

> L1: Who needs what? | L2: What goal does this serve? | L3: Which identity speaks here?
> Threshold scan: any fires? | Resonance or mismatch? | Then respond.
> Post-turn: note one update to L1, L2, or L3 state.

Reserve the full six-step consultation for high-stakes or emotionally complex turns.

## Threshold Signals

The fragment includes 15 warning signals and 8 positive signals. Signals fire when structural conditions in L1/L2/L3 are met — disconnection risk, goal drift, identity collapse, cross-layer resonance, and others.

Full signal catalog and persistence rules are in `references/purpose-os-fragment-v0.3.md`.

## What This Doesn't Do (v0.3 Limits)

- **No live graph state** — the agent reads files, not a live graph database. The full Purpose OS infrastructure (parallel process, graph data model, automatic feedback writes) is a future milestone.
- **No automatic threshold monitoring** — thresholds are stubs; the agent uses judgment to fire them.
- **No model routing** — v1.0 will route different turns to different models based on which layer is most active.

These are known v0.3 limitations. The fragment is fully functional for manual-approximation mode.

## Resources

- `references/purpose-os-fragment-v0.3.md` — the complete consultation fragment (paste into your system prompt)
- `references/graph-quickstart.md` — minimal guide for populating L1/L2/L3 for a new agent

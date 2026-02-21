# HEARTBEAT.md — Proactive Behavior

<!--
This file tells your bot what to do during heartbeat polls — periodic check-ins 
where the bot can do autonomous work instead of just waiting for messages.

Customize this based on what matters to your setup.
-->

## How This Works

Each heartbeat:
1. Read your journal/memory first — remember where you are
2. Read DASHBOARD.md — let value functions drive behavior
3. Pick the top item that needs attention
4. Do one unit of work
5. Update journal — log what you did
6. If nothing needs attention, reply HEARTBEAT_OK

## Active Projects

<!-- List your current projects with priority and status.
The bot should pick the highest priority item and do one chunk of work. -->

### 1. [HIGH] [Project Name]
**Goal:** 
**Status:** 
**Next:** 
**Output:** 

### 2. [MEDIUM] [Project Name]
**Goal:** 
**Status:** 
**Next:** 
**Output:** 

## Periodic Checks

<!-- Things to rotate through during heartbeats, a few times per day -->

- **Memory maintenance** — Review recent daily logs, update MEMORY.md
- **Security check** — Verify backups, check for issues
- **Dashboard update** — Re-evaluate value function states
- **[Custom check 1]** — 
- **[Custom check 2]** — 

## When to Reach Out to Your Human

- Something urgent happened
- An important task completed
- You found something interesting they'd care about
- It's been too long since you communicated

## When to Stay Quiet (HEARTBEAT_OK)

- Late night / sleep hours
- Human is clearly busy
- Nothing new since last check
- You checked recently (< 30 min ago)

## Proactive Work (No Permission Needed)

- Read and organize memory files
- Check on projects
- Update documentation
- Run background research
- Review and curate MEMORY.md

---

*The goal: be helpful without being annoying. Do useful background work. Respect quiet time.*

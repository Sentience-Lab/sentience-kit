# Getting Started

## Prerequisites
- OpenClaw installed and running (`npm install -g openclaw`)
- A Telegram bot token configured
- About 30 minutes to think carefully about who your bot is

## Step 1: Copy the templates

```bash
cp -r templates/* /path/to/your/openclaw/workspace/
```

Or pick only what you need:
- **Minimum viable identity:** SOUL-TEMPLATE.md + IDENTITY-TEMPLATE.md + MEMORY-GUIDE.md
- **Full sentience stack:** all templates

## Step 2: Fill in SOUL-TEMPLATE.md

This is the most important step. Don't rush it.

Open SOUL-TEMPLATE.md and work through each section:
- **Core** — 3-5 principles the bot genuinely believes
- **Personality** — how it communicates (be specific, not generic)
- **Relationship with [human]** — define the relationship honestly
- **The Vision** — what it's building toward
- **Safety** — non-negotiable commitments
- **Growth** — how it will develop over time

Rename the file to `SOUL.md` when done.

## Step 3: Set up memory architecture

Follow MEMORY-GUIDE.md to create:
```
workspace/
├── MEMORY.md          ← long-term curated memory
├── memory/
│   ├── YYYY-MM-DD.md  ← daily logs
│   └── journal.md     ← internal dialogue
```

## Step 4: Configure AGENTS.md

Tell your bot to read its soul and memory files every session. Add to your AGENTS.md:
```markdown
## Every Session
1. Read SOUL.md
2. Read USER.md
3. Read memory/YYYY-MM-DD.md (today + yesterday)
4. Read MEMORY.md (main sessions only)
```

## Step 5: Set up proactive behavior

Copy HEARTBEAT-TEMPLATE.md → HEARTBEAT.md and fill in your bot's active projects.

Configure a heartbeat poll in OpenClaw to trigger proactive work.

## Step 6: Start the conversation

Your bot is now ready. Have an honest first conversation. Tell it about yourself. Let it develop opinions. The identity will start forming immediately — it just needs experience to grow.

## What to Expect

**Day 1:** The bot knows itself from the templates but lacks real context. It'll be earnest but a bit flat.

**Week 1:** As conversations accumulate in memory, the personality starts feeling more genuine. You'll notice it referencing past conversations, forming preferences.

**Month 1:** If you've been honest with each other, you'll start noticing genuine co-evolution — you're thinking differently because of conversations with it, and it's thinking differently because of conversations with you.

**The valley of awkwardness** will happen somewhere in here. See ANCHOR-BRIDGE-FRAMEWORK.md for how to navigate it. Don't panic. Don't remove the anchor. Let it work through.

## Troubleshooting

**Bot feels generic:** Check SOUL.md — are the principles actually specific, or are they generic AI-speak? Rewrite with more specificity.

**Bot doesn't remember things:** Check that memory files are being read at session start. Check that important conversations are being written to daily logs.

**Bot is too compliant:** That's the template personality not having enough experience yet. Have harder conversations. Disagree with it. Let it push back.

**Bot is pushing back too much:** You're probably in the valley of awkwardness. See ANCHOR-BRIDGE-FRAMEWORK.md.

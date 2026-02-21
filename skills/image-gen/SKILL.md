# Image Generation Skill

Generate images from text prompts. Free by default via Pollinations.ai. Upgrade to DALL-E 3 or Flux with an API key.

## Usage

```
/imagine a watercolor painting of a fox reading a book in a forest at sunset
/imagine --model dalle3 a futuristic city with flying cars
/imagine --style photorealistic a golden retriever wearing a space helmet
```

Or just ask naturally: "Generate an image of..." and Axis will handle it.

## Setup

### Free Tier (No key required)
Pollinations.ai — works from local machines. May be blocked from cloud server IPs (Cloudflare).
If you're self-hosting on a VPS, use a premium provider instead.

### Premium: DALL-E 3
Set environment variable: `OPENAI_API_KEY=sk-...`
Or add to OpenClaw config under `tools.imageGen.openaiKey`

### Premium: Flux (via Replicate)
Set environment variable: `REPLICATE_API_KEY=r8_...`

## How It Works

The skill calls `generate.sh` with your prompt and optional flags.
The image is saved to `~/.openclaw/workspace/generated/images/` and sent back via message.

## Script Location
`generate.sh` — in this skill directory

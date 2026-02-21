# App Deployment Skill

Deploy web apps and static sites from the workspace. Supports Vercel (frontend/full-stack), Netlify (static/JAMstack), and Coolify (self-hosted anything).

## Usage

```
/deploy                          # Auto-detect project type and deploy
/deploy --platform vercel        # Force Vercel
/deploy --platform netlify       # Force Netlify
/deploy --dir ./my-app           # Deploy specific directory
/deploy --preview                # Deploy to preview URL (not production)
```

Or naturally: "Deploy the app in my-app/ to Vercel" and Axis handles it.

## Setup

### Vercel
1. Create account at vercel.com
2. Get API token: vercel.com/account/tokens
3. Set: `export VERCEL_TOKEN=your_token`

### Netlify
1. Create account at netlify.com
2. Get API token: app.netlify.com/user/applications
3. Set: `export NETLIFY_TOKEN=your_token`

### Coolify (self-hosted)
Already configured if you're running OpenClaw on Coolify.
Set: `export COOLIFY_URL=https://your-coolify-instance` and `export COOLIFY_TOKEN=your_token`

## How It Works

The skill detects your project type (package.json → Node/React, index.html → static, etc.)
and routes to the appropriate platform. Returns a live URL on success.

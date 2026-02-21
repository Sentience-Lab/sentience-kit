#!/usr/bin/env python3
"""
App Deployment Script
Supports: Vercel, Netlify, Coolify
Usage: python3 deploy.py [--dir PATH] [--platform vercel|netlify|coolify] [--preview]
"""
import os
import sys
import json
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path

def detect_project(directory):
    d = Path(directory)
    if (d / "package.json").exists():
        pkg = json.loads((d / "package.json").read_text())
        framework = "nextjs" if "next" in pkg.get("dependencies", {}) else "node"
        return framework
    if (d / "index.html").exists():
        return "static"
    if (d / "requirements.txt").exists() or (d / "pyproject.toml").exists():
        return "python"
    return "unknown"

def deploy_vercel(directory, preview=False):
    token = os.environ.get("VERCEL_TOKEN")
    if not token:
        print("Error: VERCEL_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    # Use Vercel CLI if available, fall back to API
    vercel_bin = subprocess.run(["which", "vercel"], capture_output=True, text=True).stdout.strip()
    if not vercel_bin:
        # Try installing vercel CLI
        print("Installing Vercel CLI...")
        subprocess.run(["npm", "install", "-g", "vercel"], check=True, capture_output=True)
        vercel_bin = "vercel"

    cmd = [vercel_bin, "--token", token, "--yes"]
    if not preview:
        cmd.append("--prod")
    
    result = subprocess.run(cmd, cwd=directory, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Vercel error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    # Extract URL from output
    for line in result.stdout.split("\n"):
        if line.startswith("https://"):
            return line.strip()
    return result.stdout.strip()

def deploy_netlify(directory, preview=False):
    token = os.environ.get("NETLIFY_TOKEN")
    if not token:
        print("Error: NETLIFY_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    netlify_bin = subprocess.run(["which", "netlify"], capture_output=True, text=True).stdout.strip()
    if not netlify_bin:
        print("Installing Netlify CLI...")
        subprocess.run(["npm", "install", "-g", "netlify-cli"], check=True, capture_output=True)
        netlify_bin = "netlify"
    
    cmd = [netlify_bin, "deploy", "--auth", token, "--dir", directory]
    if not preview:
        cmd.append("--prod")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Netlify error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    for line in result.stdout.split("\n"):
        if "Website URL" in line or "Live URL" in line:
            return line.split(":", 1)[-1].strip()
    return result.stdout.strip()

def deploy_coolify(directory, preview=False):
    base_url = os.environ.get("COOLIFY_URL")
    token = os.environ.get("COOLIFY_TOKEN")
    
    if not base_url or not token:
        print("Error: COOLIFY_URL and COOLIFY_TOKEN must be set", file=sys.stderr)
        sys.exit(1)
    
    # Coolify deployment via webhook trigger
    # The app must already be configured in Coolify
    app_id = os.environ.get("COOLIFY_APP_ID")
    if not app_id:
        print("Error: COOLIFY_APP_ID must be set (find in Coolify app settings)", file=sys.stderr)
        sys.exit(1)
    
    req = urllib.request.Request(
        f"{base_url}/api/v1/applications/{app_id}/deploy",
        method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
        return data.get("url", "Deploy triggered — check Coolify dashboard for URL")

def main():
    args = sys.argv[1:]
    directory = "."
    platform = None
    preview = False
    
    i = 0
    while i < len(args):
        if args[i] == "--dir" and i + 1 < len(args):
            directory = args[i + 1]
            i += 2
        elif args[i] == "--platform" and i + 1 < len(args):
            platform = args[i + 1]
            i += 2
        elif args[i] == "--preview":
            preview = True
            i += 1
        else:
            i += 1
    
    directory = str(Path(directory).resolve())
    
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} not found", file=sys.stderr)
        sys.exit(1)
    
    # Auto-detect platform if not specified
    if not platform:
        project_type = detect_project(directory)
        print(f"Detected project type: {project_type}")
        
        if os.environ.get("VERCEL_TOKEN"):
            platform = "vercel"
        elif os.environ.get("NETLIFY_TOKEN"):
            platform = "netlify"
        elif os.environ.get("COOLIFY_TOKEN"):
            platform = "coolify"
        else:
            print("Error: No deployment platform configured. Set VERCEL_TOKEN, NETLIFY_TOKEN, or COOLIFY_TOKEN.", file=sys.stderr)
            sys.exit(1)
    
    print(f"Deploying {directory} to {platform}{'(preview)' if preview else '(production)'}...")
    
    if platform == "vercel":
        url = deploy_vercel(directory, preview)
    elif platform == "netlify":
        url = deploy_netlify(directory, preview)
    elif platform == "coolify":
        url = deploy_coolify(directory, preview)
    else:
        print(f"Error: Unknown platform '{platform}'", file=sys.stderr)
        sys.exit(1)
    
    print(f"Deployed: {url}")
    return url

if __name__ == "__main__":
    main()

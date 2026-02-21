#!/bin/bash
# Image Generation Script
# Usage: ./generate.sh "prompt" [--model pollinations|dalle3|flux] [--size 1024x1024]
# Outputs: path to saved image file

set -e

PROMPT="$1"
MODEL="${2:-pollinations}"
SIZE="${3:-1024x1024}"
OUTPUT_DIR="${HOME}/.openclaw/workspace/generated/images"
mkdir -p "$OUTPUT_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FILENAME="${OUTPUT_DIR}/img_${TIMESTAMP}.png"

if [ -z "$PROMPT" ]; then
  echo "Error: No prompt provided" >&2
  exit 1
fi

URL_ENCODED_PROMPT=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$PROMPT")

case "$MODEL" in
  pollinations)
    # Free, no key required — https://pollinations.ai
    IMAGE_URL="https://image.pollinations.ai/prompt/${URL_ENCODED_PROMPT}?width=1024&height=1024&nologo=true&enhance=true"
    echo "Generating via Pollinations.ai..." >&2
    curl -sL "$IMAGE_URL" -o "$FILENAME"
    ;;

  dalle3)
    # Requires OPENAI_API_KEY
    if [ -z "$OPENAI_API_KEY" ]; then
      echo "Error: OPENAI_API_KEY not set. Export it or use --model pollinations." >&2
      exit 1
    fi
    RESPONSE=$(curl -s -X POST "https://api.openai.com/v1/images/generations" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{\"model\":\"dall-e-3\",\"prompt\":\"$PROMPT\",\"n\":1,\"size\":\"$SIZE\",\"quality\":\"hd\"}")
    IMAGE_URL=$(echo "$RESPONSE" | python3 -c "import json,sys; print(json.load(sys.stdin)['data'][0]['url'])")
    curl -sL "$IMAGE_URL" -o "$FILENAME"
    ;;

  flux)
    # Requires REPLICATE_API_KEY
    if [ -z "$REPLICATE_API_KEY" ]; then
      echo "Error: REPLICATE_API_KEY not set." >&2
      exit 1
    fi
    # Use Flux Schnell (fast, high quality)
    PREDICTION=$(curl -s -X POST "https://api.replicate.com/v1/models/black-forest-labs/flux-schnell/predictions" \
      -H "Authorization: Bearer $REPLICATE_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{\"input\":{\"prompt\":\"$PROMPT\",\"num_outputs\":1}}")
    PREDICTION_ID=$(echo "$PREDICTION" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")
    # Poll for completion
    for i in $(seq 1 30); do
      sleep 2
      RESULT=$(curl -s "https://api.replicate.com/v1/predictions/${PREDICTION_ID}" \
        -H "Authorization: Bearer $REPLICATE_API_KEY")
      STATUS=$(echo "$RESULT" | python3 -c "import json,sys; print(json.load(sys.stdin)['status'])")
      if [ "$STATUS" = "succeeded" ]; then
        IMAGE_URL=$(echo "$RESULT" | python3 -c "import json,sys; print(json.load(sys.stdin)['output'][0])")
        curl -sL "$IMAGE_URL" -o "$FILENAME"
        break
      elif [ "$STATUS" = "failed" ]; then
        echo "Error: Replicate prediction failed" >&2
        exit 1
      fi
    done
    ;;

  *)
    echo "Error: Unknown model '$MODEL'. Use: pollinations, dalle3, or flux" >&2
    exit 1
    ;;
esac

# Verify the file was created and has content
if [ -f "$FILENAME" ] && [ -s "$FILENAME" ]; then
  echo "$FILENAME"
else
  echo "Error: Image generation failed or produced empty file" >&2
  exit 1
fi

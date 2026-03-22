#!/bin/bash
# Quick word count check for articles under 8000
cd /data/.openclaw/workspace/ai-tools-hub/articles
for f in *.html; do
  words=$(sed 's/<[^>]*>//g' "$f" 2>/dev/null | wc -w)
  if [ "$words" -lt 8000 ]; then
    echo "$words $f"
  fi
done | sort -n | head -10

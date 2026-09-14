#!/usr/bin/env bash
set -euo pipefail
[ "$#" -eq 3 ] || { echo "Usage: $0 <collection> <sector> <prompt-slug>"; exit 1; }
target="prompts/$1/$2/$3.md"
[ -d "prompts/$1/$2" ] || { echo "Unknown sector"; exit 1; }
[ ! -e "$target" ] || { echo "Already exists"; exit 1; }
cp templates/prompt-template.md "$target"
echo "Created $target"

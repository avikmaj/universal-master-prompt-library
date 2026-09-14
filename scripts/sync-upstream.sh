#!/usr/bin/env bash
set -euo pipefail
echo "Review licenses and local changes before syncing. This command replaces the pinned upstream snapshot."
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
git clone --depth 1 https://github.com/aj-geddes/useful-ai-prompts.git "$tmp/source"
rm -rf upstream/aj-geddes-useful-ai-prompts/prompts
cp -R "$tmp/source/prompts" upstream/aj-geddes-useful-ai-prompts/
cp "$tmp/source/LICENSE" "$tmp/source/PROMPT-INDEX.json" "$tmp/source/README.md" upstream/aj-geddes-useful-ai-prompts/
echo "Update THIRD_PARTY_NOTICES.md with the new commit, validate, review diff and commit."

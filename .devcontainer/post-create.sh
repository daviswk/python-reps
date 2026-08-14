#!/usr/bin/env bash
set -uo pipefail

curl -LsSf https://astral.sh/uv/install.sh | sh

export PATH="$HOME/go/bin:$PATH"
if command -v go >/dev/null 2>&1; then
  go install github.com/bootdotdev/bootdev@latest \
    || echo "WARN: bootdev install failed; run manually: go install github.com/bootdotdev/bootdev@latest"
else
  echo "WARN: go not found; the devcontainer Go feature may still be provisioning."
fi

{
  echo ''
  echo '# python-mastery additions'
  echo 'export PATH="$HOME/go/bin:$HOME/.local/bin:$PATH"'
  echo "alias today='uv run python tools/plan.py'"
  echo "alias plan='uv run python tools/plan.py'"
} >> "$HOME/.bashrc"

echo "post-create complete: uv installed, bootdev attempted, aliases (today/plan) added."

#!/bin/bash
set -e

if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

uv sync --all-extras
source .venv/bin/activate

# Install pre-commit hooks
if [ ! -f ".git/hooks/pre-commit" ]; then
    pre-commit install
fi

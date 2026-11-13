#!/usr/bin/env bash
# Rebuild every data figure into ../figures (Times fonts via style.py).
set -euo pipefail
cd "$(dirname "$0")"
for f in fig_collision fig_tradeoff fig_controlled fig_controls fig_gallery; do python3 "$f.py"; done

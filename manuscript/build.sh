#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "$0")/.." && pwd)"
out="$(realpath -m -- "$1")"
mkdir -p -- "$out"
export SOURCE_DATE_EPOCH=1794182400 FORCE_SOURCE_DATE=1
export TEXINPUTS="$root/manuscript:" BIBINPUTS="$root/manuscript:" BSTINPUTS="$root/manuscript:"
export TEXMFVAR="$out/texmf-var" TEXMFCACHE="$out/texmf-cache"
for document in paper supplement; do
  dir="$root/manuscript"
  if [[ "$document" == supplement ]]; then dir="$root/supplement"; fi
  (
    cd -- "$dir"
    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
      -outdir="$out" "$document.tex"
  )
done

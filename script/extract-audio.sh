#!/usr/bin/env bash
set -euo pipefail

input="${1:-docs/4.1.2 Parte 3 Semental, destete, transporte.MP4}"
output="${2:-docs/audio/4.1.2 Parte 3 Semental, destete, transporte.mp3}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "Error: ffmpeg no esta instalado o no esta en PATH." >&2
  exit 1
fi

if [[ ! -f "$input" ]]; then
  echo "Error: no existe el video de entrada: $input" >&2
  exit 1
fi

mkdir -p "$(dirname "$output")"

ffmpeg \
  -hide_banner \
  -y \
  -i "$input" \
  -vn \
  -map 0:a:0 \
  -codec:a libmp3lame \
  -q:a 2 \
  "$output"

echo "Audio extraido: $output"

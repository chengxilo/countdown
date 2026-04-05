import os
import sys
from datetime import date
from pathlib import Path

_death_raw = os.getenv("DEATH_DATE")
if not _death_raw:
    sys.exit("Error: death_date input is required. Set it in your workflow.")

DEATH_DATE  = date.fromisoformat(_death_raw)
THEME       = os.getenv("THEME", "default")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "assets/life-countdown.svg")

THEMES = {
    "default": {
        "bg": "#0d1117", "border": "#30363d",
        "grad_start": "#4FC3F7", "grad_end": "#FF6B6B",
        "label": "#8b949e",
    },
    "tokyo-night": {
        "bg": "#1a1b2e", "border": "#414868",
        "grad_start": "#7aa2f7", "grad_end": "#bb9af7",
        "label": "#565f89",
    },
    "react": {
        "bg": "#20232a", "border": "#282c34",
        "grad_start": "#61dafb", "grad_end": "#21a1c4",
        "label": "#5c6370",
    },
    "react-dark": {
        "bg": "#0d1117", "border": "#20232a",
        "grad_start": "#61dafb", "grad_end": "#0070f3",
        "label": "#4a5568",
    },
    "dracula": {
        "bg": "#282a36", "border": "#44475a",
        "grad_start": "#bd93f9", "grad_end": "#ff79c6",
        "label": "#6272a4",
    },
    "nord": {
        "bg": "#2e3440", "border": "#3b4252",
        "grad_start": "#88c0d0", "grad_end": "#81a1c1",
        "label": "#4c566a",
    },
    "github-dark": {
        "bg": "#161b22", "border": "#30363d",
        "grad_start": "#58a6ff", "grad_end": "#bc8cff",
        "label": "#8b949e",
    },
}

t = THEMES.get(THEME, THEMES["default"])
days_remaining = (DEATH_DATE - date.today()).days

SVG = f"""\
<svg width="400" height="80" viewBox="0 0 400 80" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['grad_start']}"/>
      <stop offset="100%" stop-color="{t['grad_end']}"/>
    </linearGradient>
    <linearGradient id="lg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{t['grad_start']}" stop-opacity="0"/>
      <stop offset="50%"  stop-color="{t['grad_start']}" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{t['grad_end']}"   stop-opacity="0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect fill="{t['bg']}" stroke="{t['border']}" x="1" y="1" width="398" height="78" rx="10" stroke-width="1"/>

  <text filter="url(#glow)" fill="url(#g)" x="200" y="42" font-size="36" font-weight="700"
        text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" letter-spacing="-1">{days_remaining:,}</text>

  <line x1="110" y1="54" x2="290" y2="54" stroke="url(#lg)" stroke-width="1"/>

  <text fill="{t['label']}" x="200" y="70" font-size="11" text-anchor="middle"
        font-family="'Segoe UI', system-ui, sans-serif" letter-spacing="2">DAYS REMAINING</text>
</svg>"""

out = Path(OUTPUT_PATH)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(SVG, encoding="utf-8")
print(f"Theme: {THEME} | Days remaining: {days_remaining:,} | Output: {OUTPUT_PATH}")

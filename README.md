# ⏳ Life Countdown

A GitHub Action that generates a beautifully themed SVG showing how many days you have left — for your profile README.

## Usage

**1. Add the workflow** to your profile repo (`.github/workflows/life-countdown.yml`):

```yaml
name: Life Countdown

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - uses: actions/checkout@v4

      - uses: chengxilo/life-countdown@main
        with:
          death_date: '2084-08-10'
          theme: 'tokyo-night'
          output_path: 'assets/life-countdown.svg'

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add assets/life-countdown.svg
          git diff --staged --quiet || git commit -m "chore: update life countdown"
          git push
```

**2. Embed the SVG** in your `README.md`:

```html
<img src="assets/life-countdown.svg" alt="Life Countdown" width="400"/>
```

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `death_date` | yes | — | Target end-of-life date (`YYYY-MM-DD`) |
| `theme` | no | `default` | Visual theme (see below) |
| `output_path` | no | `assets/life-countdown.svg` | Output path for the SVG |

## Themes

| Name | Preview colors |
|---|---|
| `default` | cyan → red |
| `tokyo-night` | blue → purple |
| `react` | cyan → teal |
| `react-dark` | cyan → blue |
| `dracula` | purple → pink |
| `nord` | ice blue → slate |
| `github-dark` | blue → violet |

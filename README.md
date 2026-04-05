# ⏳ Countdown

A GitHub Action that generates a themed countdown SVG for your GitHub profile README. Count down to anything — retirement, graduation, a trip, or the end of life.

## Usage

**1. Add the workflow** to your repo (`.github/workflows/countdown.yml`):

```yaml
name: Countdown

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

      - uses: chengxilo/countdown@main
        with:
          date: '2077-04-01'
          label: "2077 April Fools' day"
          theme: 'tokyo-night'
          output_path: 'assets/countdown.svg'

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add assets/countdown.svg
          git diff --staged --quiet || git commit -m "chore: update countdown"
          git push
```

**2. Embed the SVG** in your `README.md`:

```html
<img src="assets/countdown.svg" alt="Countdown" width="400"/>
```

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `date` | yes | — | Target date (`YYYY-MM-DD`) |
| `label` | no | `DAYS REMAINING` | Label text below the number |
| `theme` | no | `default` | Visual theme (see below) |
| `output_path` | no | `assets/countdown.svg` | Output path for the SVG |

## Themes

| Name | Preview |
|---|---|
| `default` | ![default](assets/themes/default.svg) |
| `tokyo-night` | ![tokyo-night](assets/themes/tokyo-night.svg) |
| `react` | ![react](assets/themes/react.svg) |
| `react-dark` | ![react-dark](assets/themes/react-dark.svg) |
| `dracula` | ![dracula](assets/themes/dracula.svg) |
| `nord` | ![nord](assets/themes/nord.svg) |
| `github-dark` | ![github-dark](assets/themes/github-dark.svg) |
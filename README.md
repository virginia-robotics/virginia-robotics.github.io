# Virginia Robotics Symposium

Website for the Virginia Robotics Symposium (VRS).

## Repository layout

| Path | What it is |
| --- | --- |
| `VRS2026/` | The current site — built with [Hugo](https://gohugo.io/) + Tailwind CSS. Reusable theme in `themes/vrs/`; content in `content/`, `hugo.toml`, and `data/`. |
| `VRS2025/` | The previous (2025) site — a Jekyll project, kept as an archive and served at `/2025/`. |
| `docs/` | The built site that GitHub Pages publishes (Pages serves the `main` branch `/docs` folder). Generated — see below. |
| `planning/` | Design spec and implementation plan (not published). |

## Build & publish

The published site lives in `docs/`. To regenerate it, run this **from inside the `VRS2026/` folder**:

```bash
hugo -d ../docs --cleanDestinationDir
```

This builds the Hugo site (compiling Tailwind CSS through Hugo's asset pipeline) and writes the output to the repo-root `docs/` folder. Commit `docs/` and push — GitHub Pages serves it.

> **First time only** — install the Tailwind build dependencies (requires [Node.js](https://nodejs.org/)), from inside `VRS2026/`:
> ```bash
> npm install
> ```

A `.nojekyll` file is included in the output so GitHub Pages serves the Hugo build as-is (without running Jekyll over it).

## Local preview

From inside `VRS2026/`:

```bash
hugo server
```

Then open <http://localhost:1313/>. Changes reload live.

## Editing content

All event-specific content lives in `VRS2026/` — the theme has no hardcoded copy:

| To change… | Edit… |
| --- | --- |
| Date, host, venue, colors, links, map, hero image, hero credit | `hugo.toml` |
| Section copy (About, registration text, sponsor CTA, etc.) | `content/_index.md` |
| Speakers, schedule, organizers, institutions, sponsors | `data/*.yml` |
| Images | `static/img/` |

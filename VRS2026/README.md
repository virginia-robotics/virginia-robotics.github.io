# Virginia Robotics Symposium

Website for the Virginia Robotics Symposium (VRS): <https://virginia-robotics.github.io/>

## Repository layout

| Path | What it is |
| --- | --- |
| `VRS2026/` | The current site — built with [Hugo](https://gohugo.io/) + Tailwind CSS. Reusable theme in `themes/vrs/`; content in `content/`, `hugo.toml`, and `data/`. |
| `VRS2026/static/2025/` | The previous (2025) site, kept as plain static HTML and served at `/2025/`. Edit the HTML directly. (The original Jekyll source is preserved at the git tag `vrs2025-jekyll-source`; it is no longer used.) |
| `VRS2026/tools/` | Small Python helpers: `make-social-card.py` (link-preview image) and `shrink-portraits.py` (downsize photo originals). Need Pillow: `pip install pillow`. |
| `docs/` | The built site that GitHub Pages publishes (Pages serves the `main` branch `/docs` folder). Generated — see below. |
| `.github/workflows/hugo.yml` | Optional GitHub Actions build/deploy. See "Automated deploys". |

## Requirements

- **Hugo extended**, version 0.169.0 or newer (`hugo version` must say `+extended`).
- **Tailwind CSS CLI v4**, which Hugo runs during the build. Either install Node.js 20+ and run `npm install` inside `VRS2026/` (uses `package.json`), **or** put the standalone binary on your `PATH` as `tailwindcss` from <https://github.com/tailwindlabs/tailwindcss/releases> (no Node needed).

## Build & publish

The published site lives in `docs/`. To regenerate it, run this **from inside the `VRS2026/` folder**:

```bash
hugo --minify --gc -d ../docs --cleanDestinationDir
```

This builds the Hugo site (compiling Tailwind CSS through Hugo's asset pipeline), resizes images, and writes the output to the repo-root `docs/` folder. Commit `docs/` and push — GitHub Pages serves it.

A `.nojekyll` file is included in the output so GitHub Pages serves the Hugo build as-is (without running Jekyll over it).

### Automated deploys (optional)

`.github/workflows/hugo.yml` builds the site on every push with a pinned Hugo version. To let it deploy as well, go to the repository's **Settings → Pages** and set **Source** to **GitHub Actions**. After that, `docs/` can be deleted from the repo and the manual build step above is no longer needed. Until the switch is made, the workflow only verifies that the site builds.

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
| Date, times, host, venue, address, colors, links, map, hero image, hero credit, description | `hugo.toml` |
| Section copy (About, registration text, sponsor CTA, parking, etc.) | `content/_index.md` |
| Speakers, schedule, organizers, institutions, sponsors, posters | `data/*.yml` |
| Portraits (speakers, organizers) | `assets/img/people/` — Hugo crops these to square and converts to WebP. Keep originals at or below 800 px (`python3 tools/shrink-portraits.py assets/img/people/*.jpg`). Reference as `img/people/name.jpg`. |
| Logos (nav, institutions, sponsors) | `assets/img/logos/` and `assets/img/participants/` — Hugo resizes raster logos to display size; SVGs are served as-is. Reference as `img/logos/logo.png` (no leading slash). |
| Favicons, fonts, other files served verbatim | `static/` — reference with a leading slash, e.g. `/img/favicons/favicon.ico` |
| Link-preview image (what Slack, LinkedIn, iMessage show when the URL is shared) | Regenerate `static/img/social-card.jpg` with `python3 tools/make-social-card.py` after changing the date, venue, or hero image. |

### What the page head does for you

`themes/vrs/layouts/_partials/head.html` emits, from `hugo.toml` alone: the title and meta description, a canonical URL, Open Graph / Twitter card tags, favicons and the web manifest, preloads for the hero image and font, and (home page only) a schema.org `Event` block for Google's event search results. Keep `eventStart`, `eventEnd`, and `[params.address]` in `hugo.toml` current each year.

Fonts are self-hosted (`static/fonts/`, Inter variable font, Latin subsets) so the page makes no requests to Google Fonts.

## Next year

1. Copy `VRS2026/` to `VRS2027/` (or edit in place) and update `hugo.toml`, `content/_index.md`, and `data/*.yml`.
2. Export the finished 2026 home page as static HTML into `static/2026/` the way `static/2025/` is kept, and point `archiveURL` / `archiveLabel` in `hugo.toml` at it.

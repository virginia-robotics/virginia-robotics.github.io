# Virginia Robotics Symposium

Website for the Virginia Robotics Symposium (VRS).

## Repository layout

| Path | What it is |
| --- | --- |
| `VRS2026/` | The current site — built with [Hugo](https://gohugo.io/) + Tailwind CSS. Reusable theme in `themes/vrs/`; content in `content/`, `hugo.toml`, and `data/`. |
| `VRS2026/static/2025/` | The 2025 site, kept as plain static HTML and served at `/2025/`. (The original Jekyll source is in git history under the tag `vrs2025-jekyll-source`.) |
| `docs/` | The built site that GitHub Pages publishes (Pages serves the `main` branch `/docs` folder). Generated — see below. |
| `planning/` | Design spec and implementation plan (not published). |

## Build & publish

The published site lives in `docs/`. To regenerate it, run this **from inside the `VRS2026/` folder**:

```bash
hugo -d ../docs --cleanDestinationDir
```

This builds the Hugo site (compiling Tailwind CSS through Hugo's asset pipeline) and writes the output to the repo-root `docs/` folder. Commit `docs/` and push — GitHub Pages serves it.

A GitHub Actions workflow (`.github/workflows/hugo.yml`) also builds the site on every push and pull request as a check. It can take over deployment too (so `docs/` no longer needs to be committed); the steps to switch are in the comment at the top of that file.

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
| Portraits (speakers, organizers) | `assets/img/people/` — Hugo crops these to square and converts to WebP, so drop in the full-size original and reference it as `img/people/name.jpg` |
| Logos, favicons, other images | `static/img/` — served as-is; reference with a leading slash, e.g. `/img/logos/logo.png` |

## After the symposium

Three settings in `VRS2026/hugo.toml` control the "event is over" state; nothing else needs to change:

1. `registerURL = ''` and `posterURL = ''` hide the Register / poster sign-up buttons and show the "closed" text from `content/_index.md`.
2. `eventPast = true` puts the `pastNote` paragraph from `content/_index.md` at the top of About and drops the free-ticket offer from the structured data.
3. Rewrite `description` in past tense (keep it under 160 characters).

## Starting the next year

1. Archive the finished year first: copy the built `docs/` site into `VRS2026/static/<year>/` (everything except `2025/`, `sitemap.xml`, `robots.txt` and `404.html`), then in that copy's `index.html` make the asset paths start with `/<year>/`, keep the year-specific `<title>`, canonical and `og:*` tags, and add a nav/footer link to `/` labelled "Current Symposium" (see `static/2025/index.html` for the pattern). Render its link-preview card with `tools/make-social-card.py --line2 "<date>" --line3 "<venue>" --out static/<year>/assets/img/social-card.jpg`.
2. Add the archived year to the sitemap: in `hugo.toml` set `archiveURL` / `archiveLastmod` (or add a second pair if the template is extended), and link it from the footer.
3. Then update the root site for the new year: `title`, `shortName`, `dateline`, `timeRange`, `eventStart`/`eventEnd`, `venue`, `location`, `[params.address]`, `description` (future tense), `seoTitle`, `eventPast = false`, `registerURL`, `posterURL`, the hero image, and `data/*.yml`. Regenerate `static/img/social-card.jpg` with `tools/make-social-card.py`.

Keep the root (`/`) as the current or upcoming symposium and each past year under `/<year>/`: that is what keeps the main page ranking for "Virginia Robotics Symposium" while the archives rank for their own year.

## Search Console

The site is verified in Google Search Console through the `googleSiteVerification` meta tag in `hugo.toml` (emitted on every page). Use Search Console → Sitemaps to submit `https://virginia-robotics.github.io/sitemap.xml` after large changes, and the Pages report to see what Google has indexed.

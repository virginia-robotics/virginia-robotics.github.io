# Virginia Robotics Symposium

Website for the Virginia Robotics Symposium (VRS).

## Repository layout

| Path | What it is |
| --- | --- |
| `VRS2027/` | The current site — built with [Hugo](https://gohugo.io/) + Tailwind CSS. Reusable theme in `themes/vrs/`; content in `content/`, `hugo.toml`, and `data/`. Also carries the archived sites as static files (`static/2026/`, `static/2025/`). |
| `VRS2026/` | The 2026 site (Hugo, same theme), kept as an archive and served at `/2026/`. Its build output is checked into `VRS2027/static/2026/`. |
| `VRS2027/static/2025/` | The 2025 site, kept as plain static HTML and served at `/2025/`. (The original Jekyll source is in `vrs2025-jekyll-source/` and in git history.) |
| `docs/` | The built site that GitHub Pages publishes (Pages serves the `main` branch `/docs` folder). Generated — see below. |
| `planning/` | Design spec and implementation plan (not published). |

## Build & publish

The published site lives in `docs/`. To regenerate it, run this **from inside the `VRS2027/` folder**:

```bash
hugo -d ../docs --cleanDestinationDir
```

This builds the Hugo site (compiling Tailwind CSS through Hugo's asset pipeline) and writes the output to the repo-root `docs/` folder. Commit `docs/` and push — GitHub Pages serves it.

A GitHub Actions workflow (`.github/workflows/hugo.yml`) also builds the site on every push and pull request as a check. It can take over deployment too (so `docs/` no longer needs to be committed); the steps to switch are in the comment at the top of that file.

> **First time only** — install the Tailwind build dependencies (requires [Node.js](https://nodejs.org/)), from inside `VRS2027/`:
> ```bash
> npm install
> ```
> If `hugo server` later complains that `tailwindcss` "is not a Node.js script", OneDrive has flattened the symlinks in `node_modules/.bin` — run `npm ci` to restore them.

### Updating the archived 2026 site

The 2026 site is served from `VRS2027/static/2026/`. If it ever needs a change, edit `VRS2026/` (its `baseURL` is already set to `/2026/`) and rebuild it into that folder, then rebuild the main site as above:

```bash
cd VRS2026 && hugo -d ../VRS2027/static/2026 --cleanDestinationDir
```

A `.nojekyll` file is included in the output so GitHub Pages serves the Hugo build as-is (without running Jekyll over it).

## Local preview

From inside `VRS2027/`:

```bash
hugo server
```

Then open <http://localhost:1313/>. Changes reload live.

## Editing content

All event-specific content lives in `VRS2027/` — the theme has no hardcoded copy:

| To change… | Edit… |
| --- | --- |
| Date, host, venue, colors, links, map, hero image, hero credit | `hugo.toml` |
| Section copy (About, registration text, sponsor CTA, etc.) | `content/_index.md` |
| Speakers, schedule, organizers, institutions, sponsors | `data/*.yml` |
| Portraits (speakers, organizers) | `assets/img/people/` — Hugo crops these to square and converts to WebP, so drop in the full-size original and reference it as `img/people/name.jpg` |
| Logos, favicons, other images | `static/img/` — served as-is; reference with a leading slash, e.g. `/img/logos/logo.png` |

## After the symposium

Three settings in `VRS2027/hugo.toml` control the "event is over" state; nothing else needs to change:

1. `registerURL = ''` and `posterURL = ''` hide the Register / poster sign-up buttons and show the "closed" text from `content/_index.md` (`registration.pending`, `poster.closed`); `heroNote` in `content/_index.md` is shown in the hero in place of the Register button.
2. `eventPast = true` puts the `pastNote` paragraph from `content/_index.md` at the top of About and drops the free-ticket offer from the structured data.
3. Rewrite `description` in past tense (keep it under 160 characters).

## Starting the next year

Each year is its own Hugo project (`VRS<year>/`) sharing the `vrs` theme; the finished year is built into the new year's `static/<year>/` folder and served at `/<year>/`.

1. Copy the current project: `rsync -a --exclude node_modules --exclude public --exclude resources --exclude hugo_stats.json --exclude 'static/20*' VRS2027/ VRS2028/`, then `npm install` inside the copy. Move the archive folders along: `git mv VRS2027/static/2025 VRS2028/static/2025` and so on.
2. Archive the finished year: in `VRS2027/hugo.toml` set `baseURL = 'https://virginia-robotics.github.io/2027/'`, apply the "After the symposium" settings above, and build it into the new project: `cd VRS2027 && hugo -d ../VRS2028/static/2027 --cleanDestinationDir`. The theme keeps every asset path relative to `baseURL`, so the archive works under its sub-path. Regenerate its link-preview card with `tools/make-social-card.py` if the hero image changed.
3. In the new project update `hugo.toml` (`title`, `shortName`, `dateline`, `timeRange`, `eventStart`/`eventEnd`, `venue`, `location`, `[params.address]`, `description`, `seoTitle`, `eventPast = false`, `registerURL`, `posterURL`, `heroImage`, `archiveURL`/`archiveLabel`/`archiveLastmod`, `[params.colors]` for the host), `content/_index.md`, and `data/*.yml`. Hide sections that are not ready yet with `hiddenSections`. Regenerate `static/img/social-card.jpg` with `tools/make-social-card.py` and set `socialImage`.
4. Point `.github/workflows/hugo.yml` and the build commands in this README at the new folder, and add the new folder to `.gitignore`'s Hugo-artifact patterns.

Keep the root (`/`) as the current or upcoming symposium and each past year under `/<year>/`: that is what keeps the main page ranking for "Virginia Robotics Symposium" while the archives rank for their own year.

## Search Console

The site is verified in Google Search Console through the `googleSiteVerification` meta tag in `hugo.toml` (emitted on every page). Use Search Console → Sitemaps to submit `https://virginia-robotics.github.io/sitemap.xml` after large changes, and the Pages report to see what Google has indexed.

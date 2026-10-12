# Rebolting Hearts — Website

Static website (plain HTML/CSS/JS, no build step) for Rebolting Hearts, a non-profit
creating visibility, workshops, and support for women rebolting and bolting climbing
routes across Europe and Morocco.

## Structure

- `index.html` — home / about the organisation
- `team.html` — team
- `sponsors.html` — sponsors + how to become one
- `events.html` — upcoming workshops/events
- `events/morocco.html` — dedicated page for the first workshop (Morocco, April)
- `join.html` — join the group (links to sign-up form)
- `css/style.css` — shared styles
- `js/main.js` — mobile nav toggle

## Running locally

No build step needed. Open `index.html` directly in a browser, or serve the folder:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000`.

## Content to fill in before launch

The site is fully built but uses placeholder content in a few places — search for
`fill-note` boxes on each page, or check this list:

- [ ] **Join form** — `join.html` has a button pointing to `FORM_URL_PLACEHOLDER`.
      Replace with your real Google Form / Typeform URL (also used from the homepage,
      events page, and Morocco workshop page via `join.html`).
- [ ] **Team** (`team.html`) — replace placeholder names, roles, bios, and photos.
- [ ] **Sponsors** (`sponsors.html`, `index.html`) — replace placeholder logos with
      real sponsor logos (drop image files into `images/`).
- [ ] **Morocco workshop** (`events/morocco.html`) — confirm exact dates, crag/location,
      cost, group size, and language.
- [ ] **Contact email** — `contact@reboltinghearts.org` is a placeholder throughout;
      replace with your real inbox.
- [ ] **Photos** — replace the `[ Replace with a photo ]` hero placeholder and team
      photo placeholders with real images in `images/`.

## Deploying

Any static host works (GitHub Pages, Netlify, Vercel). For GitHub Pages: push to
GitHub, then enable Pages on the `main` branch in the repo settings.

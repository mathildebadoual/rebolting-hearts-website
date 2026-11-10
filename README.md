# Rebolting Hearts — Website

Static website (plain HTML/CSS/JS, no build step) for Rebolting Hearts, a non-profit
creating visibility, workshops, and support for women rebolting and bolting climbing
routes across Europe and Morocco.

## Structure

- `index.html` — home / about the organisation
- `team.html` — team
- `sponsors.html` — sponsors + how to become one
- `events.html` — upcoming workshops/events
- `events/morocco.html` — dedicated page for the first workshop, at the Gagou crag
- `join.html` — join the group: two paths, become a member or become a sponsor
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

- [ ] **Join forms** — `join.html`'s "Become a member" button now links to the real
      volunteer Google Form. The "Become a sponsor" button still points to a placeholder
      (`FORM_URL_PLACEHOLDER_SPONSOR`) — replace once a sponsor-intake form exists.
      Sponsor CTAs on `sponsors.html` link to `join.html#sponsor`.
- [ ] **Team** (`team.html`) — replace placeholder names, roles, bios, and photos.
- [ ] **Sponsors** (`sponsors.html`, `index.html`) — logos for Greenspits, Fixe Climbing,
      and FFME 04 are in `images/sponsors/` (pulled from their official sites / Wikimedia
      Commons — see Photo credits). **Confirm with each sponsor that displaying their logo
      is OK**, and ask them for a direct logo file if they'd rather you use that. One slot
      is still a generic placeholder.
- [ ] **Morocco workshop** (`events/morocco.html`) — now has real crag info (Gagou: access,
      rock, sectors, grades) sourced from the *Climbing at Gagou* topo guide (CAF Casablanca
      / Escalade Club de l'Isère, 2017). **Still needs resolving:** the guide flags a kestrel
      nesting closure from late March to early July, which overlaps the planned April date —
      pick a new date (guide recommends autumn/winter) before this goes public. Also still
      TBD: exact dates, group size, cost, language. No free-license photo of Gagou itself
      exists online — the hero photo is a generic Moroccan canyon stand-in, clearly labelled;
      swap in real on-site photos once the team has them.
- [ ] **Contact email** — `reboltinghearts@hotmail.com` is a placeholder throughout;
      replace with your real inbox.
- [ ] **Photos** — `images/*.jpg` are free-license stock photos used as stand-ins (see
      Photo credits below). Replace with real photos of the team, workshops, and events
      once available — team member photos especially, since stock photos shouldn't be
      attached to real people's names.

## Photo credits

All photos on the site are the team's own. Web-sized copies live in `images/photos/`
(page banners) and `images/team/` (member polaroids); the full-size originals are kept in
`images/`.

- `alpine-slab-lake.jpg`, `alpine-crack.jpg` — Alpine Hearts 2024, photos by Thibaut Lampe
- all other photos — shared by the team

The old Unsplash/Pexels placeholders (`hero-climber.jpg`, `woman-climbing.jpg`,
`harness-gear.jpg`, `chalk-hands.jpg`, `morocco-gorge.jpg`, `group-climbers.jpg`) are no
longer used by any page.

Sponsor/partner logos in `images/sponsors/`, pulled from official sources (trademarks of
their respective owners, used here to identify them as sponsors/partners):

- `greenspits.png` — from [greenspits.com](https://greenspits.com/fr/)
- `fixeclimbing.svg` — from [fixeclimbing.com](https://www.fixeclimbing.com/fr)
- `ffme.jpg` — official FFME logo via [Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/a/a3/FFME_LOGO_2017.jpg) (rotated to landscape), representing FFME 04

## Deploying

Any static host works (GitHub Pages, Netlify, Vercel). For GitHub Pages: push to
GitHub, then enable Pages on the `main` branch in the repo settings.

## Ulule campaign

The Ulule buttons link to the public campaign URL,
https://www.ulule.com/rebolting-hearts-workshops-for-women/ — it only resolves once the
campaign is published. Don't put the private `/preview?token=...` link on the site.

## French version (`fr/`)

The French pages in `fr/` are generated — don't edit them by hand.

1. Edit the English pages as usual.
2. Add or update the French text in `i18n/fr.py` (English sentence → French sentence).
3. Run `python3 i18n/build_fr.py`. It rebuilds every page in `fr/` and lists any English
   text that still has no translation.

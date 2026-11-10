#!/usr/bin/env python3
"""Generate the French site in fr/ from the English pages + i18n/fr.py.

Usage (from the repo root):  python3 i18n/build_fr.py

- Translates visible text and alt / aria-label / title / meta-description attributes.
- Rewrites asset paths (images/, css/) so they work one folder deeper.
- Switches <html lang>, the EN/FR toggle, and lists any English text left untranslated.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "i18n"))
from fr import FR  # noqa: E402

PAGES = ["index.html", "team.html", "sponsors.html", "events.html", "join.html", "events/morocco.html"]

# Text that is the same in both languages (names, brands, symbols) — not reported as missing.
SAME = {
    "Rebolting Hearts", "Marilyne", "Kaotar", "Hind", "Alma Esteban", "Caroline", "Cynthia-Lane",
    "Mathilde", "Nina Caprez", "Greenspits", "Fixe Climbing", "FFME 04",
    "FFME — Fédération Française de la Montagne et de l'Escalade", "@rebolting.hearts",
    "reboltinghearts@hotmail.com", "cafmaroc.ffcam.fr", "EN", "FR", "— Cynthia-Lane", "— Hind",
    "— Mathilde", "— Caroline",
}

TOKEN = re.compile(r"(<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->|<[^>]+>)", re.S | re.I)
ATTR = re.compile(r'\b(alt|aria-label|title|content)="([^"]*)"')
URL = re.compile(r'\b(src|href)="([^"]*)"')


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def translate_text(chunk, missing):
    key = norm(html.unescape(chunk))
    if not key:
        return chunk
    if key in FR:
        lead = chunk[: len(chunk) - len(chunk.lstrip())]
        trail = chunk[len(chunk.rstrip()):]
        return lead + html.escape(FR[key], quote=False) + trail
    if re.search(r"[A-Za-z]{2}", key) and key not in SAME:
        missing.add(key)
    return chunk


def fix_url(url, depth):
    if re.match(r"^(https?:|mailto:|#|data:)", url) or url.endswith(".html") or ".html#" in url or ".html?" in url:
        return url  # pages keep the same relative layout inside fr/
    return "../" + url  # assets live one level up


def translate_tag(tag, depth, missing):
    if tag.startswith("<meta") and 'name="description"' not in tag:
        pass
    else:
        def sub_attr(m):
            name, val = m.group(1), m.group(2)
            key = norm(html.unescape(val))
            if name == "content" and not tag.startswith("<meta"):
                return m.group(0)
            if key in FR:
                return f'{name}="{html.escape(FR[key], quote=True)}"'
            if name in ("alt", "aria-label", "title") and re.search(r"[A-Za-z]{2}", key) and key not in SAME:
                missing.add(f"[{name}] {key}")
            return m.group(0)
        tag = ATTR.sub(sub_attr, tag)
    if 'rel="alternate"' not in tag:
        tag = URL.sub(lambda m: f'{m.group(1)}="{fix_url(m.group(2), depth)}"', tag)
    return tag


def build(page):
    src = (ROOT / page).read_text()
    depth = page.count("/")
    name = page.split("/")[-1]
    missing = set()

    # EN/FR toggle for the French page
    up = "../" * (depth + 1)
    src = re.sub(
        r'<div class="lang-switch".*?</div>',
        f'<div class="lang-switch" aria-label="Langue">\n'
        f'      <a href="{up}{page}" lang="en" hreflang="en">EN</a>\n'
        f'      <a href="{name}" lang="fr" aria-current="true">FR</a>\n'
        f'    </div>',
        src, count=1, flags=re.S,
    )
    src = src.replace('<html lang="en">', '<html lang="fr">', 1)

    out = []
    for part in TOKEN.split(src):
        if not part:
            continue
        if part.startswith("<script") or part.startswith("<style") or part.startswith("<!--"):
            out.append(part)
        elif part.startswith("<"):
            if 'class="lang-switch"' in part or (part.startswith("<a ") and 'lang="' in part):
                out.append(part)  # toggle links are already correct
            else:
                out.append(translate_tag(part, depth, missing))
        else:
            out.append(translate_text(part, missing))
    result = "".join(out)

    dest = ROOT / "fr" / page
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(result)
    return missing


if __name__ == "__main__":
    all_missing = {}
    for page in PAGES:
        for m in build(page):
            all_missing.setdefault(m, []).append(page)
    print(f"Built {len(PAGES)} French pages in fr/")
    if all_missing:
        print(f"\n{len(all_missing)} text(s) without a French translation (add them to i18n/fr.py):")
        for k, pages in sorted(all_missing.items()):
            print(f"  - {k}   ({', '.join(pages)})")

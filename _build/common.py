"""Shared layout for the generated subpages (DE + EN). Run: python3 _build/build_pages.py
Jekyll ignores folders starting with "_", so this code is not published."""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://larsomatic.org/auftragspilot/"
APP = "https://auftragspilot-crm.vercel.app"
MCP = APP + "/api/mcp"
MCP_START = APP + "/api/mcp/start"
CALL = "https://cal.com/lars-timmermann-n7d0gl/auftragspilot-demo-gespraech"
DEMO = APP + "/a/demo/larsomatic-demo"
DEMO_EN = DEMO + "?lang=en"
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' "
           "height='100' rx='10' fill='%231F5C4C'/%3E%3Ctext x='50' y='68' font-family='monospace' font-weight='700' "
           "font-size='42' fill='%23EFF1EC' text-anchor='middle'%3EAP%3C/text%3E%3C/svg%3E")

E = html.escape

NAV = {
    "de": [("agenten/", "KI-Agenten"), ("anwendungsfaelle/", "Anwendungsfälle"), ("vergleich/", "Vergleich"), ("blog/", "Blog")],
    "en": [("en/agents/", "AI agents"), ("en/use-cases/", "Use cases"), ("en/compare/", "Compare"), ("en/blog/", "Blog")],
}
FOOT = {
    "de": [("sicherheit/", "Sicherheit"), ("limits/", "Limits"), ("changelog/", "Changelog"), ("branchen/", "Branchen"),
           ("verlust-check/", "Verlust-Check"), ("datenschutz/", "Datenschutz"), ("impressum/", "Impressum"), ("llms.txt", "Für KI-Agenten (Text)")],
    "en": [("en/security/", "Security"), ("en/limits/", "Limits"), ("en/changelog/", "Changelog"), ("en/industries/", "Industries"),
           ("en/loss-check/", "Loss check"), ("en/privacy/", "Privacy"), ("impressum/", "Legal notice"), ("llms.txt", "For AI agents (text)")],
}
HOME = {"de": "", "en": "en/"}
T = {
    "de": {"login": "Anmelden (App)", "signup": "Konto erstellen", "other": "English", "home": "Startseite",
           "demo": "Demo testen", "call": "Kostenloses Gespräch buchen", "copy": "Kopieren", "copied": "Kopiert ✓",
           "tag": "Auftragspilot. Vom Lead zum Auftrag.", "by": "Ein Produkt der Larsomatic OÜ.",
           "applabel": "Die App ist der geschützte Bereich für Kunden: Zugang nur mit Konto."},
    "en": {"login": "Log in (app)", "signup": "Create account", "other": "Deutsch", "home": "Home",
           "demo": "Try the demo", "call": "Book a free call", "copy": "Copy", "copied": "Copied ✓",
           "tag": "Auftragspilot. From lead to job.", "by": "A product of Larsomatic OÜ.",
           "applabel": "The app is the protected area for customers: access only with an account."},
}

PAGES = []  # (path, alt_path) for the sitemap


def rel(path: str) -> str:
    """prefix from a page folder back to the site root (relative links work locally and on GitHub Pages)"""
    depth = path.strip("/").count("/") + 1 if path.strip("/") else 0
    return "../" * depth


def copybox(text: str, lang: str) -> str:
    return (f'<div class="copy"><code>{E(text)}</code><button class="btn btn--ghost" type="button" data-copy '
            f'data-done="{T[lang]["copied"]}">{T[lang]["copy"]}</button></div>')


def page(lang: str, path: str, alt: str, title: str, desc: str, body: str, wide: bool = False, current: str = "") -> None:
    r = rel(path)
    t = T[lang]
    nav = "".join(f'<a href="{r}{h}"{" aria-current=\"page\"" if h == current else ""}>{E(l)}</a>' for h, l in NAV[lang])
    foot = "".join(f'<a href="{r}{h}">{E(l)}</a>' for h, l in FOOT[lang])
    other = "en" if lang == "de" else "de"
    doc = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)} · Auftragspilot</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{BASE}{path}">
<link rel="alternate" hreflang="{lang}" href="{BASE}{path}">
<link rel="alternate" hreflang="{other}" href="{BASE}{alt}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{BASE}assets/og-{'de' if lang == 'de' else 'en'}.png">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{r}assets/fonts/space-grotesk-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/ibm-plex-sans-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/fonts.css">
<link rel="stylesheet" href="{r}assets/pages.css">
</head>
<body>
<header class="nav"><div class="nav__in">
<a class="nav__brand" href="{r}{HOME[lang]}" aria-label="{t['home']}"><img src="{r}assets/auftragspilot-logo.png" alt="Auftragspilot" width="640" height="184"></a>
<nav class="nav__links" aria-label="Navigation">{nav}</nav>
<div class="nav__app" title="{E(t['applabel'])}"><a href="{r}{alt}" hreflang="{other}">{t['other']}</a><a href="{APP}/a/login">{t['login']}</a><a class="btn btn--ghost" href="{APP}/a/start">{t['signup']}</a></div>
</div></header>
<main class="wrap{' wrap--wide' if wide else ''}">
{body}
</main>
<footer class="foot"><div class="foot__in">{foot}<span class="sp"></span><span>{t['tag']} {t['by']}</span><span>{E(t['applabel'])}</span></div></footer>
<script>
document.querySelectorAll("[data-copy]").forEach(function(b){{b.addEventListener("click",function(){{var c=b.parentElement.querySelector("code");if(navigator.clipboard&&c)navigator.clipboard.writeText(c.innerText).then(function(){{b.textContent=b.dataset.done}})}})}});
</script>
</body>
</html>
"""
    out = os.path.join(ROOT, path, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append((path, alt, lang))


def cta(lang: str, demo_first: bool = True) -> str:
    if lang == "de":
        return f"""<section class="cta"><p class="kicker">Nächster Schritt</p><h2>Selbst testen oder machen lassen.</h2>
<p>Schreib dem Demo-Agenten deiner Branche auf WhatsApp und erlebe, wie schnell ein Lead eine Antwort bekommt. Oder buch ein kostenloses Gespräch, dann richten wir alles für dich ein.</p>
<div class="btns"><a class="btn" href="{DEMO}">{T[lang]['demo']}</a><a class="btn btn--ghost" href="{CALL}">{T[lang]['call']}</a></div></section>"""
    return f"""<section class="cta"><p class="kicker">Next step</p><h2>Try it yourself or let us do it.</h2>
<p>Message the demo agent for your industry on WhatsApp and see how fast a lead gets an answer. Or book a free call and we set everything up for you.</p>
<div class="btns"><a class="btn" href="{DEMO_EN}">{T[lang]['demo']}</a><a class="btn btn--ghost" href="{CALL}">{T[lang]['call']}</a></div></section>"""


def ul(items) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items) -> str:
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows) -> str:
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def faq(items) -> str:
    return "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in items)


def sitemap() -> None:
    urls = ['  <url><loc>https://larsomatic.org/auftragspilot/</loc></url>',
            '  <url><loc>https://larsomatic.org/auftragspilot/en/</loc></url>',
            '  <url><loc>https://larsomatic.org/auftragspilot/de/</loc></url>',
            '  <url><loc>https://larsomatic.org/auftragspilot/verlust-check/</loc></url>',
            '  <url><loc>https://larsomatic.org/auftragspilot/en/loss-check/</loc></url>',
            '  <url><loc>https://larsomatic.org/auftragspilot/impressum/</loc></url>',
            '  <url><loc>https://larsomatic.org/auftragspilot/datenschutz/</loc></url>']
    for path, alt, lang in PAGES:
        other = "en" if lang == "de" else "de"
        urls.append(f'  <url><loc>{BASE}{path}</loc><xhtml:link rel="alternate" hreflang="{lang}" href="{BASE}{path}"/>'
                    f'<xhtml:link rel="alternate" hreflang="{other}" href="{BASE}{alt}"/></url>')
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")

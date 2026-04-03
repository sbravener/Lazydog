
#!/usr/bin/env python3
"""Simple helper to add a new blog post to this static site.

Usage:
  python tools/add_blog_post.py     --title "My Blog Title"     --category "Security"     --audience "All Industries"     --excerpt "One sentence summary."     --source-file my-article.html
"""

from pathlib import Path
import argparse
import re
import html
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
SITEMAP = ROOT / "sitemap.xml"
BLOG_INDEX = BLOG / "index.html"


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "new-post"


def load_text(source: Path) -> str:
    soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
    card = soup.select_one(".card") or soup.body
    paragraphs = [p.get_text(" ", strip=True) for p in card.select("p") if p.get_text(strip=True)]
    if not paragraphs:
        raise SystemExit("No paragraph content found in source file.")
    return "

".join(paragraphs)


def post_template(title: str, excerpt: str, body: str) -> str:
    paras = "
".join(f"<p>{html.escape(p)}</p>" for p in body.split("

") if p.strip())
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{html.escape(title)} | Lazy Dog Computing</title>
<meta name="description" content="{html.escape(excerpt)}"/>
<link rel="stylesheet" href="../assets/css/styles.css"/>
</head>
<body>
<header class="topbar">
  <div class="container nav">
    <a class="brand" href="../index.html"><div class="logo" aria-hidden="true"></div><div class="brand-text"><h1>Lazy Dog Computing</h1><p>Simple, secure, reliable IT for local businesses</p></div></a>
    <nav class="navlinks"><a href="../index.html">Home</a><a href="../services.html">Services</a><a href="../manufacturing.html">Manufacturing</a><a href="../verticals/legal.html">Legal</a><a href="../verticals/financial.html">Financial</a><a href="../verticals/medical.html">Medical</a><a href="index.html">Blog</a><a href="../contact.html">Contact</a></nav>
  </div>
</header>
<main>
  <section class="page-hero"><div class="container"><span class="eyebrow">Business Technology Blog</span><h2>{html.escape(title)}</h2><p class="section-copy">{html.escape(excerpt)}</p></div></section>
  <section><div class="container"><article class="article-wrap">{paras}</article></div></section>
</main>
<footer class="footer"><div class="container footer-grid"><div><h3>Lazy Dog Computing</h3><p class="muted">Simple, secure, reliable IT for local businesses with a Microsoft 365, security, backup, and compliance focus.</p></div><div><h3>Quick Links</h3><p><a href="../services.html">Managed IT Services</a><br/><a href="index.html">Business Technology Blog</a><br/><a href="../contact.html">Contact Us</a></p><p class="muted">205 Fairway Dr.<br/>Lexington, NC 27292<br/>336-313-9727</p></div></div></footer>
<script src="../assets/js/main.js"></script>
</body>
</html>"""


def add_to_blog_index(title: str, href: str, category: str, audience: str, excerpt: str):
    html_text = BLOG_INDEX.read_text(encoding="utf-8")
    if f'>{title}<' in html_text:
        print("Blog index already contains this title. Skipping index insert.")
        return
    card = f'<article class="blog-card"><span class="tag">{html.escape(category)}</span><span class="tag">{html.escape(audience)}</span><h3><a href="{href}">{html.escape(title)}</a></h3><p>{html.escape(excerpt)}</p></article>'
    marker = '<div class="blog-grid">'
    html_text = html_text.replace(marker, marker + card, 1)
    BLOG_INDEX.write_text(html_text, encoding="utf-8")


def add_to_sitemap(href: str):
    xml = SITEMAP.read_text(encoding="utf-8")
    loc = f'<url><loc>https://www.lazydogcomputing.com/blog/{href}</loc></url>'
    if loc in xml:
        print("Sitemap already contains this URL. Skipping sitemap insert.")
        return
    xml = xml.replace('</urlset>', f'  {loc}
</urlset>')
    SITEMAP.write_text(xml, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--category', default='Business Technology')
    parser.add_argument('--audience', default='All Industries')
    parser.add_argument('--excerpt', required=True)
    parser.add_argument('--source-file', required=True)
    args = parser.parse_args()

    slug = slugify(args.title) + '.html'
    target = BLOG / slug
    body = load_text(Path(args.source_file))
    if not target.exists():
        target.write_text(post_template(args.title, args.excerpt, body), encoding='utf-8')
        print(f'Created {target}')
    else:
        print(f'{target.name} already exists. Skipping page creation.')
    add_to_blog_index(args.title, slug, args.category, args.audience, args.excerpt)
    add_to_sitemap(slug)
    print('Done.')


if __name__ == '__main__':
    main()

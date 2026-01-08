#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from html import escape

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light dark;
      --pad: 16px;
      --maxw: 1100px;
      --border: rgba(127,127,127,.35);
    }}
    body {{
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Arial, sans-serif;
      line-height: 1.4;
    }}
    header {{
      padding: var(--pad);
      border-bottom: 1px solid var(--border);
    }}
    header .wrap {{
      max-width: var(--maxw);
      margin: 0 auto;
      display: flex;
      gap: 12px;
      align-items: baseline;
      justify-content: space-between;
      flex-wrap: wrap;
    }}
    main {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: var(--pad);
    }}
    .viewer {{
      width: 100%;
      height: min(85vh, 1000px);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      background: rgba(127,127,127,.08);
    }}
    .meta {{
      opacity: .8;
      font-size: .95rem;
    }}
    a {{
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .btn {{
      display: inline-block;
      padding: 8px 12px;
      border: 1px solid var(--border);
      border-radius: 8px;
    }}
  </style>
</head>
<body>
<header>
  <div class="wrap">
    <div>
      <div><strong>{title}</strong></div>
      <div class="meta">Auto-built from LaTeX on each push.</div>
    </div>
    <div>
      <a class="btn" href="{pdf_href}" download>Download PDF</a>
    </div>
  </div>
</header>

<main>
  <object class="viewer" data="{pdf_href}" type="application/pdf">
    <p>
      Your browser can’t embed PDFs here.
      <a href="{pdf_href}">Open the PDF</a>.
    </p>
  </object>
</main>
</body>
</html>
"""

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Output HTML path (e.g. dist/index.html)")
    ap.add_argument("--pdf", required=True, help="PDF href relative to the HTML (e.g. document.pdf)")
    ap.add_argument("--title", default="Document", help="Page title")
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    html = HTML.format(
        title=escape(args.title),
        pdf_href=escape(args.pdf),
    )
    out.write_text(html, encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())


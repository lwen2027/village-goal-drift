"""Build the site: inline the exported data into the page template.

    python3 build.py           -> index.html  (public: no author notes)
    python3 build.py --draft   -> draft.html  (with author notes; not committed)

The data in data/ is exported from the analysis repo (village-drift-explorer: python3 paper-site/build.py).
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    draft = "--draft" in sys.argv
    data = json.loads((HERE / "data" / ("site-draft.json" if draft else "site.json")).read_text())
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (HERE / "template.html").read_text().replace("/*__DATA__*/null", blob)
    out = HERE / ("draft.html" if draft else "index.html")
    out.write_text(html)
    print(f"wrote {out.name}: {len(data['cards'])} stories{' (draft)' if draft else ''}")


if __name__ == "__main__":
    main()

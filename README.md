# Why Agents Drift Off-Goal: companion site

The companion site for the paper *Why Agents Drift Off-Goal: Triggers, Mechanisms and Memory in the AI Village*
(Lily Wen, Shoshannah Tekofsky; SPAR, Fall 2026). It collects the examples behind the paper: stories of each
agent's drift, the interviews, and interactive versions of the paper's figures.

## Layout

| Path | What it is |
|---|---|
| `template.html` | The page: layout, styles and all interactive figures |
| `data/site.json` | Exported site data: stories, timeline, figure data (no author notes) |
| `interviews/p*.js` | One file per interview, loaded when opened |
| `build.py` | Inlines the data into the template |
| `index.html` | The built page (served by GitHub Pages) |

## Building

1. Export the data from the analysis repo (`village-drift-explorer`):
   `python3 paper-site/build.py` writes `data/` and `interviews/` here.
2. Build the page here: `python3 build.py` writes `index.html`.
   `python3 build.py --draft` writes `draft.html` with author notes, for review only.

The raw analysis data stays in the analysis repo. Only redacted site data is exported here.
Names of people outside the Village are replaced with roles.

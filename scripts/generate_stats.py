#!/usr/bin/env python3
"""Generate monochrome stats cards for the profile README.

Fetches public GitHub data via the REST API (no third-party service) and
renders four SVG cards into the assets/ directory:
  stats.svg / stats-dark.svg          - stars, commits, PRs, issues
  top-langs.svg / top-langs-dark.svg  - top languages by bytes
"""

import json
import os
import sys
import urllib.parse
import urllib.request

USER = os.environ.get("STATS_USER", "Sagirilzy")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "assets"

API = "https://api.github.com"
FONT = "Segoe UI, -apple-system, Helvetica, Arial, sans-serif"

# Soft pastel pink palettes, one per color-scheme mode.
PALETTE = {
    "light": dict(border="#FFD6E8", title="#D97BA3", value="#C25E8E", label="#E8A8C4",
                  bar=["#FFD6E8", "#FFB7D5", "#F79AC2", "#EF7FB3", "#E5629E", "#D94F8A"]),
    "dark": dict(border="#5A3D4F", title="#F8BBD0", value="#FFE0EC", label="#C98BA4",
                 bar=["#FFB7D5", "#EF7FB3", "#D94F8A", "#C25E8E", "#A8507A", "#8E4568"]),
}


def api(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-stats-generator",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    request = urllib.request.Request(API + path, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as resp:
        return json.loads(resp.read().decode())


def own_repos():
    repos, page = [], 1
    while True:
        batch = api(f"/users/{USER}/repos?per_page=100&page={page}&type=owner")
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def collect():
    repos = own_repos()
    stars = sum(r.get("stargazers_count", 0) for r in repos)

    commits = 0
    lang_bytes = {}
    for repo in repos:
        for c in api(f"/repos/{repo['full_name']}/contributors?per_page=100"):
            if c["login"].lower() == USER.lower():
                commits += c.get("contributions", 0)
                break
        for lang, nbytes in api(f"/repos/{repo['full_name']}/languages").items():
            lang_bytes[lang] = lang_bytes.get(lang, 0) + nbytes

    def search(kind):
        q = urllib.parse.quote(f"author:{USER} type:{kind}")
        return api(f"/search/issues?q={q}")["total_count"]

    prs = search("pr")
    issues = search("issue")

    langs = sorted(lang_bytes.items(), key=lambda kv: -kv[1])[:6]
    total = sum(n for _, n in langs)
    return {
        "stars": stars,
        "commits": commits,
        "prs": prs,
        "issues": issues,
        "langs": [(name, n / total) for name, n in langs] if total else [],
    }


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_head(p):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="150" viewBox="0 0 440 150">'
            f'<rect x="1.5" y="1.5" width="437" height="147" rx="8" fill="none" '
            f'stroke="{p["border"]}" stroke-width="1.5"/>')


def stats_card(data, mode):
    p = PALETTE[mode]
    metrics = [
        ("STARS", data["stars"]),
        ("COMMITS", data["commits"]),
        ("PRS", data["prs"]),
        ("ISSUES", data["issues"]),
    ]
    parts = [
        svg_head(p),
        f'<text x="20" y="32" font-family="{FONT}" font-size="13" font-weight="600" '
        f'fill="{p["title"]}">GitHub Stats</text>',
    ]
    for idx, (label, value) in enumerate(metrics):
        x = 20 + (idx % 2) * 205
        y = 82 + (idx // 2) * 50
        parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="22" '
                     f'font-weight="700" fill="{p["value"]}">{value:,}</text>')
        parts.append(f'<text x="{x}" y="{y + 16}" font-family="{FONT}" font-size="11" '
                     f'letter-spacing="1.5" fill="{p["label"]}">{label}</text>')
    return "".join(parts) + "</svg>\n"


def langs_card(data, mode):
    p = PALETTE[mode]
    parts = [
        svg_head(p),
        f'<text x="20" y="32" font-family="{FONT}" font-size="13" font-weight="600" '
        f'fill="{p["title"]}">Top Languages</text>',
    ]
    if not data["langs"]:
        parts.append(f'<text x="220" y="100" text-anchor="middle" font-family="{FONT}" '
                     f'font-size="12" fill="{p["label"]}">No public languages yet</text>')
    else:
        for i, (name, frac) in enumerate(data["langs"]):
            y = 58 + i * 16
            bar_w = max(round(180 * frac), 2)
            pct = f"{frac:.0%}" if frac >= 0.01 else "<1%"
            parts.append(f'<text x="20" y="{y}" font-family="{FONT}" font-size="12" '
                         f'fill="{p["value"]}">{esc(name)}</text>')
            parts.append(f'<rect x="140" y="{y - 4.5}" width="{bar_w}" height="7" rx="3.5" '
                         f'fill="{p["bar"][i]}"/>')
            parts.append(f'<text x="420" y="{y}" text-anchor="end" font-family="{FONT}" '
                         f'font-size="11" fill="{p["label"]}">{pct}</text>')
    return "".join(parts) + "</svg>\n"


def main():
    try:
        data = collect()
    except Exception as exc:
        print(f"::warning::generation failed, keeping previous cards: {exc}",
              file=sys.stderr)
        return 0
    os.makedirs(OUT_DIR, exist_ok=True)
    for mode in ("light", "dark"):
        suffix = "-dark" if mode == "dark" else ""
        with open(os.path.join(OUT_DIR, f"stats{suffix}.svg"), "w") as fh:
            fh.write(stats_card(data, mode))
        with open(os.path.join(OUT_DIR, f"top-langs{suffix}.svg"), "w") as fh:
            fh.write(langs_card(data, mode))
    print(json.dumps({k: v for k, v in data.items() if k != "langs"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

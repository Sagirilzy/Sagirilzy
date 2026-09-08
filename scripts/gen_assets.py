#!/usr/bin/env python3
"""Generate jirai-kei (地雷系) assets for the profile README.

Style: black x hot pink, yami kawaii — lace trim, chains with heart
charms, big bows, teddy bear, falling hearts/crosses/sparkles.

Outputs (into assets/):
  hero.svg     - animated jirai-kei banner with the artwork card
  divider.svg  - jirai-kei divider (pink line, hearts, crosses)
  mutsumi.svg  - (unused fallback) vector chibi
"""

import base64
import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"

PINK = "#FF5BAE"
PINK_L = "#FF8FC9"
PINK_PALE = "#FF9EC9"
PINK_D = "#E0439A"
DARK = "#1A1220"
DARKER = "#120D18"

# ---------------------------------------------------------------- chibi
# (unused fallback, kept in case artwork.png is removed)

H = "#8CCBA6"
HH = "#A8E0C0"
S = "#FFE8D1"
SS = "#F6CFAE"
EYE = "#7CC79A"
PUPIL = "#2E6B4A"
BLUSH = "#FFC9DE"
MOUTH = "#E58CA5"
DR = "#40344A"
PU = "#6C4E8E"
WH = "#FFFFFF"
WOOD = "#B98A5E"
WOODD = "#8A5A3C"

W, HHG = 200, 240


def el(cx, cy, rx, ry, fill, **kw):
    opts = "".join(f' {k}="{v}"' for k, v in kw.items())
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"{opts}/>'


def ci(cx, cy, r, fill, **kw):
    opts = "".join(f' {k}="{v}"' for k, v in kw.items())
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{opts}/>'


def chibi_inner():
    p = []
    p.append(f'<path d="M100,24 C132,24 152,50 152,82 L152,204 C152,216 142,222 132,222 '
             f'L68,222 C58,222 48,216 48,204 L48,82 C48,50 68,24 100,24 Z" fill="{H}"/>')
    for x0, x1 in ((70, 66), (88, 92), (112, 108), (130, 134)):
        p.append(f'<path d="M{x0},120 Q{x1},170 {x0},214" stroke="{H}" stroke-width="3" '
                 f'fill="none" opacity="0.45"/>')
    p.append(el(100, 62, 46, 44, HH))
    p.append(el(100, 78, 36, 33, S))
    p.append(ci(62, 82, 4.5, SS))
    p.append(ci(138, 82, 4.5, SS))
    p.append(f'<path d="M64,54 Q56,84 64,120 L78,118 Q72,82 78,54 Z" fill="{HH}"/>')
    p.append(f'<path d="M136,54 Q144,84 136,120 L122,118 Q128,82 122,54 Z" fill="{HH}"/>')
    p.append(f'<rect x="62" y="38" width="76" height="20" fill="{HH}"/>')
    p.append(ci(72, 56, 15, HH))
    p.append(ci(100, 54, 17, HH))
    p.append(ci(128, 56, 15, HH))
    for ex in (84, 116):
        p.append(el(ex, 82, 8.5, 11, EYE))
        p.append(el(ex + 0.5, 84, 4, 6, PUPIL))
        p.append(ci(ex - 2.5, 77, 2.2, WH))
        p.append(ci(ex + 3, 87, 1.2, WH, opacity="0.8"))
        p.append(f'<path d="M{ex - 9},73 Q{ex},69 {ex + 9},73" stroke="{PUPIL}" '
                 f'stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    p.append(el(72, 95, 4.5, 2.2, BLUSH, opacity="0.55"))
    p.append(el(128, 95, 4.5, 2.2, BLUSH, opacity="0.55"))
    p.append(f'<path d="M97,99 Q100,101.5 103,99" stroke="{MOUTH}" stroke-width="1.6" '
             f'fill="none" stroke-linecap="round"/>')
    p.append(f'<rect x="95" y="106" width="10" height="9" rx="4" fill="{S}"/>')
    p.append(f'<rect x="70" y="128" width="9" height="22" rx="4.5" fill="{DR}"/>')
    p.append(f'<rect x="121" y="128" width="9" height="22" rx="4.5" fill="{DR}"/>')
    p.append(ci(74.5, 153, 4.5, S))
    p.append(ci(125.5, 153, 4.5, S))
    p.append(f'<path d="M82,130 Q100,117 118,130 L116,158 L84,158 Z" fill="{DR}"/>')
    p.append(f'<path d="M94,119 L100,127 L106,119 Z" fill="{WH}"/>')
    p.append(f'<path d="M82,156 L118,156 L126,192 Q100,198 74,192 Z" fill="{DR}"/>')
    p.append(f'<path d="M74,192 Q100,198 126,192 L125,186 Q100,192 75,186 Z" fill="{PU}"/>')
    p.append(f'<rect x="93" y="193" width="5" height="13" rx="2.5" fill="{S}"/>')
    p.append(f'<rect x="102" y="193" width="5" height="13" rx="2.5" fill="{S}"/>')
    p.append(el(95, 208, 6.5, 3.5, DR))
    p.append(el(105, 208, 6.5, 3.5, DR))
    p.append(f'<path d="M88,132 L134,158" stroke="{PU}" stroke-width="3" fill="none" '
             f'opacity="0.8"/>')
    p.append(f'<g transform="rotate(-28 142 150)">'
             f'<rect x="137" y="92" width="8" height="62" rx="4" fill="{WOOD}" stroke="{WOODD}" stroke-width="1.5"/>'
             f'<rect x="133" y="82" width="16" height="14" rx="3" fill="{WOODD}"/>'
             f'<line x1="141" y1="96" x2="141" y2="150" stroke="#5C4033" stroke-width="0.8"/>'
             f'<line x1="144" y1="96" x2="144" y2="150" stroke="#5C4033" stroke-width="0.8"/>'
             f'</g>')
    p.append(f'<path d="M136,150 C152,148 160,162 155,177 C150,190 132,192 128,178 '
             f'C125,166 128,152 136,150 Z" fill="{WOOD}" stroke="{WOODD}" stroke-width="1.5"/>')
    p.append(ci(142, 169, 4.5, WOODD))
    p.append(ci(133, 150, 5, S))
    return "".join(p)


def mutsumi_svg():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{HHG}" '
            f'viewBox="0 0 {W} {HHG}">{chibi_inner()}</svg>\n')


# ------------------------------------------------------------ jirai hero

HEART = ("M0,3.5 C-2.5,1 -5.5,1.5 -5.5,4 C-5.5,6.5 -2.5,8.5 0,10 "
         "C2.5,8.5 5.5,6.5 5.5,4 C5.5,1.5 2.5,1 0,3.5 Z")
CROSS = "M0,-5 L5,5 M5,-5 L0,5"
SPARK = ("M0,-7 L1.8,-2 L7,0 L1.8,2 L0,7 L-1.8,2 L-7,0 L-1.8,-2 Z")

# falling items: (x, y, delay, duration, size, color)
FALL_HEARTS = [
    (120, 20, 0.3, 9, 1.0, PINK), (300, 40, 2.1, 11, 0.7, PINK_L),
    (410, 10, 1.2, 10, 1.2, PINK), (470, 60, 3.3, 9, 0.8, PINK_L),
    (540, 15, 0.8, 12, 1.0, PINK), (600, 55, 2.7, 10, 0.7, PINK_PALE),
    (660, 25, 1.7, 11, 1.1, PINK), (200, 80, 4.1, 9, 0.9, PINK_L),
    (380, 90, 5.2, 12, 0.6, PINK), (510, 100, 3.8, 10, 1.0, PINK),
    (640, 110, 2.4, 9, 0.8, PINK_L), (150, 130, 5.8, 11, 0.7, PINK_PALE),
]
FALL_CROSSES = [
    (270, 50, 1.9, 12, 0.8, PINK_PALE), (450, 120, 4.6, 10, 0.9, PINK_PALE),
    (580, 85, 0.5, 13, 0.7, PINK_PALE), (700, 60, 2.9, 11, 0.8, PINK_PALE),
    (330, 130, 5.5, 10, 0.7, PINK_PALE),
]
SPARKS = [(100, 60), (250, 100), (420, 140), (560, 130), (690, 150), (180, 20)]


def fall_item(shape, x, y, delay, dur, size, color, stroke_w=None):
    fill = f'fill="{color}"'
    if shape == CROSS:
        fill = f'stroke="{color}" stroke-width="{stroke_w or 2}" fill="none" stroke-linecap="round"'
    return (f'<g transform="translate({x},{y}) scale({size})">'
            f'<g class="fall" style="animation-delay:{delay}s;animation-duration:{dur}s">'
            f'<path d="{shape}" {fill}/></g></g>')


def spark_item(x, y, delay):
    return (f'<g class="tw" style="animation-delay:{delay}s" transform="translate({x},{y})">'
            f'<path d="{SPARK}" fill="{PINK_PALE}"/></g>')


def chain(x, n=8):
    links = [f'<ellipse cx="{x}" cy="{14 + i * 13}" rx="4" ry="6.5" fill="none" '
             f'stroke="{PINK}" stroke-width="1.6"/>' for i in range(n)]
    charm_y = 14 + n * 13 + 8
    charm = (f'<path d="{HEART}" fill="{PINK}" '
             f'transform="translate({x}, {charm_y}) scale(1.3)"/>')
    return (f'<g class="chain">{charm}{"".join(links)}</g>')


def bow(cx, cy, s=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({s})">
  <ellipse cx="-17" cy="0" rx="17" ry="11" fill="{PINK}" transform="rotate(-24)"/>
  <ellipse cx="17" cy="0" rx="17" ry="11" fill="{PINK}" transform="rotate(24)"/>
  <ellipse cx="-17" cy="0" rx="17" ry="11" fill="{PINK_L}" opacity="0.4" transform="rotate(-24)"/>
  <circle cx="0" cy="2" r="6.5" fill="{PINK_D}"/>
  <path d="M-6,5 Q-14,18 -18,24" stroke="{PINK}" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M6,5 Q14,18 18,24" stroke="{PINK}" stroke-width="5" fill="none" stroke-linecap="round"/>
</g>'''


def bear(cx, cy, s=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({s})">
  <ellipse cx="0" cy="20" rx="22" ry="17" fill="{PINK_PALE}"/>
  <circle cx="0" cy="-4" r="16" fill="{PINK_PALE}"/>
  <circle cx="-12" cy="-17" r="5.5" fill="{PINK_PALE}"/>
  <circle cx="12" cy="-17" r="5.5" fill="{PINK_PALE}"/>
  <circle cx="-12" cy="-17" r="2.8" fill="{PINK}"/>
  <circle cx="12" cy="-17" r="2.8" fill="{PINK}"/>
  <ellipse cx="0" cy="3" rx="7.5" ry="5" fill="#FFE9F4"/>
  <path d="{HEART}" fill="{PINK}" transform="translate(0, 2.6) scale(0.5)"/>
  <circle cx="-5" cy="-6" r="1.7" fill="#2A1E33"/>
  <circle cx="5" cy="-6" r="1.7" fill="#2A1E33"/>
  <ellipse cx="-19" cy="17" rx="5.5" ry="8" fill="{PINK_PALE}" transform="rotate(18 -19 17)"/>
  <ellipse cx="19" cy="17" rx="5.5" ry="8" fill="{PINK_PALE}" transform="rotate(-18 19 17)"/>
  <ellipse cx="-9" cy="36" rx="7" ry="4.5" fill="#FFD3E8"/>
  <ellipse cx="9" cy="36" rx="7" ry="4.5" fill="#FFD3E8"/>
  <ellipse cx="-4" cy="12" rx="4" ry="3" fill="{PINK}" transform="rotate(-18 -4 12)"/>
  <ellipse cx="4" cy="12" rx="4" ry="3" fill="{PINK}" transform="rotate(18 4 12)"/>
  <circle cx="0" cy="12.5" r="2" fill="{PINK_D}"/>
</g>'''


def scallops(y, color=PINK):
    circles = "".join(f'<circle cx="{10 + i * 20}" cy="{y}" r="9" fill="{color}"/>'
                      for i in range(36))
    return f'<rect x="0" y="{y - 12}" width="720" height="3" fill="{color}"/>{circles}'


def artwork_data_uri():
    path = os.path.join(OUT, "artwork.png")
    if not os.path.exists(path):
        return None
    with open(path, "rb") as fh:
        return "data:image/png;base64," + base64.b64encode(fh.read()).decode()


def hero_svg():
    uri = artwork_data_uri()
    card = ""
    if uri:
        card = (
            '<g class="bob">'
            '<rect x="84" y="44" width="162" height="162" rx="22" fill="#FF5BAE" '
            'opacity="0.35" filter="url(#glow)"/>'
            f'<rect x="87" y="47" width="156" height="156" rx="20" fill="{DARK}"/>'
            f'<image x="90" y="50" width="150" height="150" href="{uri}" '
            'preserveAspectRatio="xMidYMid slice"/>'
            '</g>'
        )
    else:
        scale = 0.68
        gx, gy = 92, 199 - 211.5 * scale
        card = (f'<g transform="translate({gx},{gy}) scale({scale})">'
                f'<g class="bob">{chibi_inner()}</g></g>')

    hearts = "".join(fall_item(HEART, *h) for h in FALL_HEARTS)
    crosses = "".join(fall_item(CROSS, *c) for c in FALL_CROSSES)
    sparks = "".join(spark_item(x, y, i * 0.7) for i, (x, y) in enumerate(SPARKS))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="240" viewBox="0 0 720 240">
<style>
  .fall {{ animation: fall linear infinite; }}
  @keyframes fall {{
    0%   {{ transform: translateY(0) rotate(0deg); opacity: 0; }}
    10%  {{ opacity: 1; }}
    90%  {{ opacity: 1; }}
    100% {{ transform: translateY(240px) rotate(360deg); opacity: 0; }}
  }}
  .tw {{ animation: twinkle ease-in-out infinite; }}
  @keyframes twinkle {{
    0%, 100% {{ opacity: 0.2; transform: scale(0.7); }}
    50%      {{ opacity: 1;   transform: scale(1.2); }}
  }}
  .bob {{ animation: bob ease-in-out infinite; }}
  @keyframes bob {{
    0%, 100% {{ transform: translateY(0); }}
    50%      {{ transform: translateY(-4px); }}
  }}
  .chain {{ animation: sway ease-in-out infinite; transform-origin: 52px 6px; }}
  @keyframes sway {{
    0%, 100% {{ transform: rotate(-5deg); }}
    50%      {{ transform: rotate(5deg); }}
  }}
</style>
<defs>
  <linearGradient id="jbg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1E1428"/>
    <stop offset="1" stop-color="{DARKER}"/>
  </linearGradient>
  <filter id="glow"><feGaussianBlur stdDeviation="6"/></filter>
</defs>
<rect width="720" height="240" fill="url(#jbg)"/>
{hearts}
{crosses}
{sparks}
{chain(52, 9)}
{card}
{bow(90, 52, 0.5)}
{bear(332, 196, 1.0)}
{bow(660, 34, 1.0)}
<text x="700" y="216" text-anchor="end" font-family="sans-serif" font-size="13" fill="{PINK_PALE}">◞♡ yami kawaii ♡</text>
{scallops(222)}
</svg>
"""


# -------------------------------------------------------- jirai divider
def divider_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="18" viewBox="0 0 720 18">
<line x1="120" y1="9" x2="280" y2="9" stroke="{PINK}" stroke-width="1.6" opacity="0.55"/>
<line x1="440" y1="9" x2="600" y2="9" stroke="{PINK}" stroke-width="1.6" opacity="0.55"/>
<path d="{HEART}" fill="{PINK}" transform="translate(330, 9) scale(0.55)"/>
<path d="{HEART}" fill="{PINK}" transform="translate(360, 9) scale(0.55)"/>
<path d="{HEART}" fill="{PINK_L}" transform="translate(390, 9) scale(0.45)"/>
<path d="{CROSS}" stroke="{PINK_PALE}" stroke-width="1.8" fill="none" transform="translate(305, 9) scale(0.7)"/>
<path d="{CROSS}" stroke="{PINK_PALE}" stroke-width="1.8" fill="none" transform="translate(415, 9) scale(0.7)"/>
</svg>
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, content in [
        ("mutsumi.svg", mutsumi_svg()),
        ("hero.svg", hero_svg()),
        ("divider.svg", divider_svg()),
    ]:
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(content)
        print(f"wrote {name}")


if __name__ == "__main__":
    main()

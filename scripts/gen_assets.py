#!/usr/bin/env python3
"""Generate the cute pastel assets for the profile README.

Outputs (into assets/):
  mutsumi.svg  - original pixel-art chibi (mint long hair, green eyes)
  hero.svg     - animated banner: pastel sky, drifting clouds, falling
                 sakura petals, twinkling stars, bobbing chibi and a cat
  divider.svg  - soft pastel gradient divider
"""

import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"

# ---------------------------------------------------------------- chibi
# Original pixel fan-art, 16x20 grid. Palette:
#   h/H mint hair, s/S skin, e eye, b blush, m mouth, d/D lavender dress
CHIBI = [
    "....HHHHHHHH....",
    "..HHhhhhhhhhHH..",
    ".HhhhhhhhhhhhhH.",
    "HhhhhhhhhhhhhhhH",
    "HhhhhhhhhhhhhhhH",
    "HhhhhhhhhhhhhhhH",
    "HhhsssssssssshhH",
    "HhhseessssseeshH",
    "HhhsssssssssshhH",
    "HhhssbsssssbsshH",
    "HhhsssssssssshhH",
    "HhhssssmssssshhH",
    "HhhsssssssssshhH",
    "HhhsssssssssshhH",
    "HhhsssssssssshhH",
    "HHhhhhsssshhhhHH",
    "....ssssss......",
    "..hddddddddddh..",
    ".hddddddddddddh.",
    "hHDddddddddddDHh",
]

CHIBI_PALETTE = {
    "h": "#A8E0C0", "H": "#8CCBA6",
    "s": "#FFE8D1", "S": "#F6CFAE",
    "e": "#4E8A5E",
    "b": "#FFC9DE",
    "m": "#E58CA5",
    "d": "#C9B8E8", "D": "#B39DD8",
}

PIXEL = 6  # one grid cell = 6px


def chibi_rects(scale=1):
    rects = []
    for row, line in enumerate(CHIBI):
        for col, ch in enumerate(line):
            if ch == ".":
                continue
            rects.append(
                f'<rect x="{col * PIXEL}" y="{row * PIXEL}" width="{PIXEL}" '
                f'height="{PIXEL}" fill="{CHIBI_PALETTE[ch]}"/>'
            )
    return "".join(rects), len(CHIBI[0]) * PIXEL, len(CHIBI) * PIXEL


def mutsumi_svg():
    rects, w, h = chibi_rects()
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}">{rects}</svg>\n'
    )


# ------------------------------------------------------------------ hero
PETALS = [
    (60, 120, 0, 9), (140, 40, 2.2, 10), (240, 90, 1.1, 12),
    (330, 30, 3.1, 9), (420, 110, 0.6, 11), (510, 50, 2.6, 10),
    (590, 100, 1.6, 12), (670, 20, 3.6, 9),
]

STARS = [(95, 45), (210, 60), (395, 25), (500, 70), (610, 35), (690, 80)]
CLOUDS = [(130, 42), (330, 55), (540, 35)]


def petal(cx, cy, delay, dur):
    return (
        f'<g class="petal" style="animation-delay:{delay}s;'
        f'animation-duration:{dur}s"><ellipse cx="{cx}" cy="{cy}" rx="7" ry="4.5" '
        f'fill="#FFC7DC" transform="rotate(25 {cx} {cy})"/></g>'
    )


def star(cx, cy, delay):
    return (
        f'<g class="star" style="animation-delay:{delay}s">'
        f'<path d="M{cx} {cy - 7} L{cx + 2} {cy - 2} L{cx + 7} {cy} '
        f'L{cx + 2} {cy + 2} L{cx} {cy + 7} L{cx - 2} {cy + 2} '
        f'L{cx - 7} {cy} L{cx - 2} {cy - 2} Z" fill="#FFE9A8"/></g>'
    )


def cloud(cx, cy, delay):
    return (
        f'<g class="cloud" style="animation-delay:{delay}s">'
        f'<ellipse cx="{cx}" cy="{cy}" rx="34" ry="12" fill="#FFFFFF" opacity="0.85"/>'
        f'<ellipse cx="{cx - 24}" cy="{cy + 3}" rx="18" ry="8" fill="#FFFFFF" opacity="0.85"/>'
        f'<ellipse cx="{cx + 26}" cy="{cy + 4}" rx="16" ry="7" fill="#FFFFFF" opacity="0.85"/>'
        f"</g>"
    )


def hero_svg():
    rects, w, h = chibi_rects()
    chibi_w, chibi_h = w, h
    # chibi standing on the hill at left, cat on the hill at right
    gx, gy = 110, 199 - chibi_h
    petals = "".join(petal(*p) for p in PETALS)
    stars = "".join(star(cx, cy, i * 0.7) for i, (cx, cy) in enumerate(STARS))
    clouds = "".join(cloud(cx, cy, i * 1.3) for i, (cx, cy) in enumerate(CLOUDS))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="220" viewBox="0 0 720 220">
<style>
  .petal {{ animation: fall linear infinite; }}
  @keyframes fall {{
    0%   {{ transform: translateY(0) rotate(0deg); opacity: 0; }}
    10%  {{ opacity: 0.9; }}
    100% {{ transform: translateY(200px) rotate(300deg); opacity: 0; }}
  }}
  .star {{ animation: twinkle ease-in-out infinite; }}
  @keyframes twinkle {{
    0%, 100% {{ opacity: 0.25; transform: scale(0.8); }}
    50%      {{ opacity: 1;    transform: scale(1.15); }}
  }}
  .cloud {{ animation: drift ease-in-out infinite; }}
  @keyframes drift {{
    0%, 100% {{ transform: translateX(-18px); }}
    50%      {{ transform: translateX(18px); }}
  }}
  .bob {{ animation: bob ease-in-out infinite; }}
  @keyframes bob {{
    0%, 100% {{ transform: translateY(0); }}
    50%      {{ transform: translateY(-5px); }}
  }}
  .tail {{ animation: sway ease-in-out infinite; transform-origin: 585px 185px; }}
  @keyframes sway {{
    0%, 100% {{ transform: rotate(-12deg); }}
    50%      {{ transform: rotate(12deg); }}
  }}
</style>
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFE9F4"/>
    <stop offset="1" stop-color="#EAF2FF"/>
  </linearGradient>
</defs>
<rect width="720" height="220" fill="url(#sky)"/>
<ellipse cx="360" cy="238" rx="400" ry="52" fill="#FFD9E8"/>
{clouds}
{stars}
{petals}
<g class="bob" transform="translate({gx},{gy})">{rects}</g>
<!-- cat -->
<g class="bob" style="animation-delay:0.4s">
  <path class="tail" d="M 585 185 Q 615 175 625 158 Q 630 150 622 152 Q 610 165 588 172 Z" fill="#B8B8C8"/>
  <ellipse cx="565" cy="176" rx="26" ry="18" fill="#D8D8E4"/>
  <circle cx="565" cy="152" r="17" fill="#D8D8E4"/>
  <path d="M 551 143 L 549 128 L 559 138 Z" fill="#D8D8E4"/>
  <path d="M 579 143 L 581 128 L 571 138 Z" fill="#D8D8E4"/>
  <path d="M 551 141 L 553 129 L 557 137 Z" fill="#FFC7DC"/>
  <path d="M 579 141 L 577 129 L 573 137 Z" fill="#FFC7DC"/>
  <path d="M 559 154 Q 562 150 565 154 Q 568 150 571 154" stroke="#9A9AAE" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <circle cx="559" cy="153" r="1.3" fill="#9A9AAE"/>
  <circle cx="571" cy="153" r="1.3" fill="#9A9AAE"/>
  <ellipse cx="565" cy="158" rx="1.6" ry="1.1" fill="#E58CA5"/>
  <path d="M 541 154 L 531 152 M 541 158 L 531 159 M 589 154 L 599 152 M 589 158 L 599 159" stroke="#B8B8C8" stroke-width="1.2" stroke-linecap="round"/>
</g>
</svg>
"""


# -------------------------------------------------------------- divider
def divider_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="720" height="14" viewBox="0 0 720 14">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFB7D5" stop-opacity="0"/>
    <stop offset="0.5" stop-color="#FFB7D5"/>
    <stop offset="1" stop-color="#8EC5FC" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect x="60" y="6" width="600" height="2.5" rx="1.25" fill="url(#g)"/>
<circle cx="360" cy="7" r="4" fill="#FFB7D5"/>
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

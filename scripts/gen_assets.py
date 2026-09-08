#!/usr/bin/env python3
"""Generate the cute pastel assets for the profile README.

Outputs (into assets/):
  mutsumi.svg  - original vector chibi fan-art (mint long hair, green
                 eyes, gothic dress, guitar)
  hero.svg     - animated banner: pastel sky, drifting clouds, falling
                 sakura petals, twinkling stars, bobbing chibi and a cat
  divider.svg  - soft pastel gradient divider
"""

import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"

# ---------------------------------------------------------------- chibi
# Original vector chibi fan-art, drawn in a 200x240 viewBox.
# Mutsumi-inspired: very long straight mint hair, green eyes, quiet
# expression, gothic stage dress and a guitar.

H = "#8CCBA6"   # hair shade
HH = "#A8E0C0"  # hair light
S = "#FFE8D1"   # skin
SS = "#F6CFAE"  # skin shade
EYE = "#7CC79A"
PUPIL = "#2E6B4A"
BLUSH = "#FFC9DE"
MOUTH = "#E58CA5"
DR = "#40344A"  # dress
PU = "#6C4E8E"  # purple accent
WH = "#FFFFFF"
WOOD = "#B98A5E"
WOODD = "#8A5A3C"

W, HHG = 200, 240  # viewBox size


def el(cx, cy, rx, ry, fill, **kw):
    opts = "".join(f' {k}="{v}"' for k, v in kw.items())
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"{opts}/>'


def ci(cx, cy, r, fill, **kw):
    opts = "".join(f' {k}="{v}"' for k, v in kw.items())
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{opts}/>'


def chibi_inner():
    p = []
    # back hair: very long, falls to the knees
    p.append(f'<path d="M100,24 C132,24 152,50 152,82 L152,204 C152,216 142,222 132,222 '
             f'L68,222 C58,222 48,216 48,204 L48,82 C48,50 68,24 100,24 Z" fill="{H}"/>')
    # hair strand lines
    for x0, x1 in ((70, 66), (88, 92), (112, 108), (130, 134)):
        p.append(f'<path d="M{x0},120 Q{x1},170 {x0},214" stroke="{H}" stroke-width="3" '
                 f'fill="none" opacity="0.45"/>')
    # hair cap
    p.append(el(100, 62, 46, 44, HH))
    # head
    p.append(el(100, 78, 36, 33, S))
    # ears
    p.append(ci(62, 82, 4.5, SS))
    p.append(ci(138, 82, 4.5, SS))
    # front side locks framing the face
    p.append(f'<path d="M64,54 Q56,84 64,120 L78,118 Q72,82 78,54 Z" fill="{HH}"/>')
    p.append(f'<path d="M136,54 Q144,84 136,120 L122,118 Q128,82 122,54 Z" fill="{HH}"/>')
    # bangs: blunt fringe with three soft scallops
    p.append(f'<rect x="62" y="38" width="76" height="20" fill="{HH}"/>')
    p.append(ci(72, 56, 15, HH))
    p.append(ci(100, 54, 17, HH))
    p.append(ci(128, 56, 15, HH))
    # eyes
    for ex in (84, 116):
        p.append(el(ex, 82, 8.5, 11, EYE))
        p.append(el(ex + 0.5, 84, 4, 6, PUPIL))
        p.append(ci(ex - 2.5, 77, 2.2, WH))
        p.append(ci(ex + 3, 87, 1.2, WH, opacity="0.8"))
        p.append(f'<path d="M{ex - 9},73 Q{ex},69 {ex + 9},73" stroke="{PUPIL}" '
                 f'stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    # blush
    p.append(el(72, 95, 4.5, 2.2, BLUSH, opacity="0.55"))
    p.append(el(128, 95, 4.5, 2.2, BLUSH, opacity="0.55"))
    # mouth: quiet neutral line
    p.append(f'<path d="M97,99 Q100,101.5 103,99" stroke="{MOUTH}" stroke-width="1.6" '
             f'fill="none" stroke-linecap="round"/>')
    # neck
    p.append(f'<rect x="95" y="106" width="10" height="9" rx="4" fill="{S}"/>')
    # arms
    p.append(f'<rect x="70" y="128" width="9" height="22" rx="4.5" fill="{DR}"/>')
    p.append(f'<rect x="121" y="128" width="9" height="22" rx="4.5" fill="{DR}"/>')
    p.append(ci(74.5, 153, 4.5, S))
    p.append(ci(125.5, 153, 4.5, S))
    # dress torso + skirt
    p.append(f'<path d="M82,130 Q100,117 118,130 L116,158 L84,158 Z" fill="{DR}"/>')
    p.append(f'<path d="M94,119 L100,127 L106,119 Z" fill="{WH}"/>')
    p.append(f'<path d="M82,156 L118,156 L126,192 Q100,198 74,192 Z" fill="{DR}"/>')
    p.append(f'<path d="M74,192 Q100,198 126,192 L125,186 Q100,192 75,186 Z" fill="{PU}"/>')
    # legs and shoes
    p.append(f'<rect x="93" y="193" width="5" height="13" rx="2.5" fill="{S}"/>')
    p.append(f'<rect x="102" y="193" width="5" height="13" rx="2.5" fill="{S}"/>')
    p.append(el(95, 208, 6.5, 3.5, DR))
    p.append(el(105, 208, 6.5, 3.5, DR))
    # guitar strap
    p.append(f'<path d="M88,132 L134,158" stroke="{PU}" stroke-width="3" fill="none" '
             f'opacity="0.8"/>')
    # guitar: neck pointing up-left, body at lower right
    p.append(f'<g transform="rotate(-28 142 150)">'
             f'<rect x="137" y="92" width="8" height="62" rx="4" fill="{WOOD}" stroke="{WOODD}" stroke-width="1.5"/>'
             f'<rect x="133" y="82" width="16" height="14" rx="3" fill="{WOODD}"/>'
             f'<line x1="141" y1="96" x2="141" y2="150" stroke="#5C4033" stroke-width="0.8"/>'
             f'<line x1="144" y1="96" x2="144" y2="150" stroke="#5C4033" stroke-width="0.8"/>'
             f'</g>')
    p.append(f'<path d="M136,150 C152,148 160,162 155,177 C150,190 132,192 128,178 '
             f'C125,166 128,152 136,150 Z" fill="{WOOD}" stroke="{WOODD}" stroke-width="1.5"/>')
    p.append(ci(142, 169, 4.5, WOODD))
    # right hand resting on the guitar neck
    p.append(ci(133, 150, 5, S))
    return "".join(p)


def mutsumi_svg():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{HHG}" '
            f'viewBox="0 0 {W} {HHG}">{chibi_inner()}</svg>\n')


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
    petals = "".join(petal(*p) for p in PETALS)
    stars = "".join(star(cx, cy, i * 0.7) for i, (cx, cy) in enumerate(STARS))
    clouds = "".join(cloud(cx, cy, i * 1.3) for i, (cx, cy) in enumerate(CLOUDS))

    # chibi standing on the hill at left, cat on the hill at right
    # feet at viewBox y=211.5; place them on the hill surface (~y 193-199)
    scale = 0.68
    gx, gy = 92, 199 - 211.5 * scale

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
    50%      {{ transform: translateY(-4px); }}
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
<g transform="translate({gx},{gy}) scale({scale})"><g class="bob">{chibi_inner()}</g></g>
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

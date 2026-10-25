"""Generate the Tokyo Snow extension icon as SVG (512x512 viewBox).

Regenerate icon.png from the repo root:
    python3 images/icon/silhouette.py images/icon/icon.svg
    rsvg-convert -w 256 -h 256 images/icon/icon.svg -o icon.png

A figure with an umbrella stands in the snow in front of a wall of four lit
vending machines, drawn from the README banner photo (gaddo-arch hypr/gruv-01.jpg)
using only the tokyo-snow palette.
"""
import random
import sys

C = dict(
    night="#1c1c1a", shadow="#2a2a28", slate="#3a3933", dim="#7d7860",
    snow="#f1e4b5", gold="#ecd08f", amber="#e1b568", ember="#db814c",
    neon="#d5583d", brick="#96402e", sage="#c4c88e", moss="#a6d46c", pine="#6fc28a",
)
rnd = random.Random(7)
out = []
w = out.append


def rect(x, y, wd, ht, fill, extra=""):
    w(f'<rect x="{x:.1f}" y="{y:.1f}" width="{wd:.1f}" height="{ht:.1f}" fill="{fill}" {extra}/>')


# ---------- defs ----------
w('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">')
w('<defs>')
w('<clipPath id="frame"><rect width="512" height="512" rx="56"/></clipPath>')
w(f'''<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#161614"/><stop offset=".6" stop-color="{C['night']}"/><stop offset="1" stop-color="{C['shadow']}"/></linearGradient>''')
w(f'''<radialGradient id="haze" cx=".85" cy=".08" r=".55">
  <stop offset="0" stop-color="{C['sage']}" stop-opacity=".22"/><stop offset="1" stop-color="{C['sage']}" stop-opacity="0"/></radialGradient>''')
w(f'''<linearGradient id="body" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#4a4840"/><stop offset=".08" stop-color="{C['slate']}"/><stop offset=".9" stop-color="{C['slate']}"/><stop offset="1" stop-color="{C['shadow']}"/></linearGradient>''')
w(f'''<linearGradient id="win" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{C['snow']}"/><stop offset=".45" stop-color="{C['gold']}"/><stop offset="1" stop-color="{C['amber']}"/></linearGradient>''')
w(f'''<linearGradient id="win-warm" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{C['gold']}"/><stop offset=".55" stop-color="{C['amber']}"/><stop offset="1" stop-color="{C['ember']}"/></linearGradient>''')
w(f'''<linearGradient id="snowfloor" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{C['dim']}"/><stop offset=".35" stop-color="#a3a37a"/><stop offset="1" stop-color="{C['sage']}"/></linearGradient>''')
w(f'''<radialGradient id="spill" cx=".5" cy="0" r="1">
  <stop offset="0" stop-color="{C['amber']}" stop-opacity=".55"/><stop offset="1" stop-color="{C['amber']}" stop-opacity="0"/></radialGradient>''')
w(f'''<linearGradient id="glare" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#ffffff" stop-opacity=".28"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>''')
w(f'''<radialGradient id="vignette" cx=".5" cy=".46" r=".72">
  <stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>''')
w(f'''<linearGradient id="coat" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="{C['night']}"/><stop offset=".5" stop-color="#141412"/><stop offset="1" stop-color="{C['night']}"/></linearGradient>''')
w('''<filter id="grain" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="4" result="n"/>
  <feColorMatrix in="n" type="saturate" values="0"/>
  <feComponentTransfer><feFuncA type="table" tableValues="0 .09"/></feComponentTransfer>
</filter>''')
w('<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.2"/></filter>')
w('<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="10"/></filter>')
w(f'<clipPath id="ground"><rect x="0" y="{392}" width="512" height="120"/></clipPath>')
w('</defs>')
w('<g clip-path="url(#frame)">')

# ---------- backdrop: alley wall, pipes, overhead wires, far haze ----------
rect(0, 0, 512, 512, "url(#wall)")
rect(0, 0, 512, 512, "url(#haze)")
for x, wd in ((6, 7), (470, 5)):
    rect(x, 0, wd, 190, C["slate"], 'opacity=".55"')
w(f'<path d="M0 34 Q256 58 512 22" fill="none" stroke="{C["slate"]}" stroke-width="2.5" opacity=".8"/>')
w(f'<path d="M0 60 Q300 84 512 50" fill="none" stroke="{C["slate"]}" stroke-width="1.5" opacity=".6"/>')
# awning edge over the machines
rect(0, 92, 512, 10, C["shadow"])
rect(0, 100, 512, 3, "#4a4840", 'opacity=".7"')

# ---------- vending machines ----------
TOP, BOT = 116, 392
machines = [
    dict(x=14, wd=116, sign="gold", window="win"),
    dict(x=136, wd=116, sign="pale", window="win-warm"),
    dict(x=258, wd=116, sign="gold", window="win"),
    dict(x=380, wd=118, sign="neon", window="win-warm"),
]
product_cols = [C["ember"], C["neon"], C["gold"], C["sage"], C["moss"], C["pine"], C["brick"], C["snow"], C["amber"]]


def wordmark(x, y, wd, ht, ink):
    """Abstract sign lettering: a thin line of small word-bars over one bold line.

    Reads as signage at icon size without spelling anything (no real brand)."""
    def line(ly, lh, n_words, gap):
        lens = [rnd.uniform(.6, 1.4) for _ in range(n_words)]
        scale = (wd - gap * (n_words - 1)) / sum(lens)
        lx = x
        for L in lens:
            rect(lx, ly, L * scale, lh, ink, f'rx="{lh / 2.6:.1f}"')
            lx += L * scale + gap
    line(y, ht * .2, 3, 4)
    line(y + ht * .38, ht * .62, 2, 6)


for m in machines:
    x, wd = m["x"], m["wd"]
    # light spill on the snow in front
    w(f'<ellipse cx="{x + wd / 2:.1f}" cy="{BOT + 6}" rx="{wd * .75:.1f}" ry="46" fill="url(#spill)"/>')
    # cabinet
    rect(x, TOP, wd, BOT - TOP, "url(#body)")
    rect(x, TOP, 2, BOT - TOP, C["dim"], 'opacity=".5"')
    # header sign, backlit
    sx, sy, sw, sh = x + 7, TOP + 8, wd - 14, 34
    if m["sign"] == "gold":
        rect(sx, sy, sw, sh, C["gold"], 'rx="2"')
        wordmark(sx + 6, sy + 7, sw - 36, 20, C["night"])
        w(f'<circle cx="{sx + sw - 13:.1f}" cy="{sy + sh / 2:.1f}" r="10" fill="none" stroke="{C["night"]}" stroke-width="2.5"/>')
        w(f'<circle cx="{sx + sw - 13:.1f}" cy="{sy + sh / 2:.1f}" r="4" fill="{C["night"]}"/>')
    elif m["sign"] == "pale":
        rect(sx, sy, sw, sh, C["snow"], 'rx="2"')
        wordmark(sx + 8, sy + 7, sw - 16, 20, C["neon"])
    else:
        rect(sx, sy, sw, sh, C["neon"], 'rx="2"')
        wordmark(sx + 8, sy + 7, sw - 16, 20, C["snow"])
    w(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="{C["snow"]}" opacity=".18" filter="url(#glow)"/>')
    if m["sign"] == "gold":
        rect(sx + 10, sy + sh - 3, 34, 9, C["neon"], 'rx="1.5"')
        for k in range(3):
            rect(sx + 14 + k * 9, sy + sh, 6, 3, C["snow"])
    # display window with three shelves of drinks
    wx, wy, ww, wh = x + 8, TOP + 52, wd - 16, 150
    w(f'<rect x="{wx - 6}" y="{wy - 6}" width="{ww + 12}" height="{wh + 12}" fill="{C["gold"]}" opacity=".6" filter="url(#glow)"/>')
    rect(wx, wy, ww, wh, f'url(#{m["window"]})')
    row_h = wh / 3
    for r in range(3):
        base = wy + (r + 1) * row_h - 12
        n = 6
        slot = ww / n
        for i in range(n):
            col = rnd.choice(product_cols)
            cx = wx + i * slot + slot / 2
            ph = rnd.uniform(22, row_h - 18)
            pw = slot * rnd.uniform(.5, .66)
            if rnd.random() < .55:  # bottle: body, shoulder, cap
                rect(cx - pw / 2, base - ph, pw, ph, col, 'rx="2"')
                rect(cx - pw / 4, base - ph - 6, pw / 2, 7, col)
                rect(cx - pw / 4, base - ph - 9, pw / 2, 3, C["snow"])
                rect(cx - pw / 2, base - ph * .55, pw, ph * .22, C["snow"], 'opacity=".55"')
            else:  # can
                ph = min(ph, 28)
                rect(cx - pw / 2, base - ph, pw, ph, col, 'rx="1.5"')
                rect(cx - pw / 2, base - ph, pw, 2.5, C["snow"], 'opacity=".7"')
                rect(cx - pw / 2 + 2, base - ph + 6, pw - 4, 5, C["night"], 'opacity=".35"')
        # shelf rail with price tags and selection buttons
        rect(wx, base, ww, 9, C["shadow"])
        for i in range(n):
            tx = wx + i * slot + slot / 2
            rect(tx - 6, base + 1.5, 12, 6, C["snow"], 'opacity=".9"')
            w(f'<circle cx="{tx}" cy="{base + 11.5}" r="2" fill="{rnd.choice((C["neon"], C["ember"], C["neon"]))}"/>')
    # glass glare
    w(f'<polygon points="{wx},{wy} {wx + ww * .45},{wy} {wx},{wy + wh * .6}" fill="url(#glare)"/>')
    rect(wx, wy, ww, wh, "none", f'stroke="{C["night"]}" stroke-width="2"')
    # lower panel: poster, coin box, dispenser slot
    py = wy + wh + 10
    poster_w = ww * .62
    rect(wx, py, poster_w, 54, C["shadow"])
    for k in range(3):  # vertical sign strokes on the poster
        lx = wx + 8 + k * 14
        for j in range(4):
            rect(lx, py + 7 + j * 11, rnd.choice((6, 9)), 2.5, C["snow"] if k else C["neon"], 'opacity=".8"')
    rect(wx + poster_w + 6, py, ww - poster_w - 6, 54, "#45433b")
    rect(wx + poster_w + 12, py + 8, 4, 12, C["night"])
    w(f'<circle cx="{wx + ww - 9:.1f}" cy="{py + 14}" r="3" fill="{C["ember"]}"/>')
    rect(wx + poster_w + 12, py + 30, ww - poster_w - 18, 6, C["neon"], 'opacity=".85"')
    rect(wx + 6, BOT - 26, ww - 12, 16, C["night"])
    rect(wx + 6, BOT - 26, ww - 12, 2, C["dim"])
    # snow settled on the cabinet top
    pts = [f"{x - 2},{TOP + 2}"]
    for k in range(9):
        pts.append(f"{x + k * wd / 8:.1f},{TOP - rnd.uniform(2, 6):.1f}")
    pts.append(f"{x + wd + 2},{TOP + 2}")
    w(f'<polygon points="{" ".join(pts)}" fill="{C["snow"]}" opacity=".85"/>')

# ---------- snow on the ground ----------
w(f'<path d="M0 {BOT} L512 {BOT} L512 512 L0 512 Z" fill="url(#snowfloor)"/>')
w('<g clip-path="url(#ground)">')
for m in machines:  # glow again over the floor so it reads on top of the snow
    w(f'<ellipse cx="{m["x"] + m["wd"] / 2:.1f}" cy="{BOT + 4}" rx="{m["wd"] * .62:.1f}" ry="34" fill="url(#spill)"/>')
w('</g>')
rect(0, BOT, 512, 4, C["night"], 'opacity=".55"')
# footprints walking in from the left
for k in range(7):
    fx = 40 + k * 30
    fy = 470 - k * 7 + (6 if k % 2 else -6)
    w(f'<ellipse cx="{fx}" cy="{fy}" rx="{9 - k * .5:.1f}" ry="{4.4 - k * .25:.1f}" fill="{C["slate"]}" opacity=".55"/>')
for _ in range(46):
    fx, fy = rnd.uniform(-10, 522), rnd.uniform(BOT + 14, 512)
    if abs(fx - 262) < 70 and fy > 440:
        continue  # keep the figure's own shadow clean
    k = (fy - BOT) / (512 - BOT)  # nearer prints are bigger
    rx_, ry_ = 3 + 6 * k, 1.4 + 2.8 * k
    w(f'<ellipse cx="{fx:.1f}" cy="{fy:.1f}" rx="{rx_:.1f}" ry="{ry_:.1f}" fill="{C["slate"]}" opacity="{rnd.uniform(.35, .6):.2f}"/>')
    w(f'<ellipse cx="{fx + rx_ * 1.6:.1f}" cy="{fy - ry_ * 1.8:.1f}" rx="{rx_:.1f}" ry="{ry_:.1f}" fill="{C["slate"]}" opacity="{rnd.uniform(.35, .6):.2f}"/>')
# snow surface texture
for _ in range(70):
    sx, sy = rnd.uniform(0, 512), rnd.uniform(BOT + 8, 512)
    w(f'<ellipse cx="{sx:.1f}" cy="{sy:.1f}" rx="{rnd.uniform(2, 7):.1f}" ry="{rnd.uniform(.8, 2):.1f}" fill="{rnd.choice((C["snow"], C["dim"]))}" opacity="{rnd.uniform(.15, .35):.2f}"/>')

# ---------- the figure ----------
FX = 262
# shadow on the snow
w(f'<ellipse cx="{FX + 14}" cy="478" rx="64" ry="10" fill="{C["night"]}" opacity=".45"/>')
# legs and boots
rect(FX - 22, 410, 17, 58, C["night"], 'rx="3"')
rect(FX + 6, 404, 17, 60, C["night"], 'rx="3"')
rect(FX - 25, 460, 23, 10, "#141412", 'rx="4"')
rect(FX + 5, 456, 24, 10, "#141412", 'rx="4"')
# long coat
w(f'<path d="M{FX - 34} 300 Q{FX} 284 {FX + 34} 300 L{FX + 46} 418 Q{FX} 428 {FX - 46} 418 Z" fill="url(#coat)"/>')
# coat seam, belt and pocket hints
w(f'<path d="M{FX + 2} 296 L{FX + 4} 420" stroke="{C["shadow"]}" stroke-width="2"/>')
rect(FX - 40, 354, 82, 5, C["shadow"])
w(f'<path d="M{FX - 26} 300 L{FX + 40} 372" stroke="#141412" stroke-width="4"/>')
w(f'<path d="M{FX + 30} 366 L{FX + 64} 362 L{FX + 68} 400 L{FX + 34} 404 Z" fill="#141412"/>')
w(f'<path d="M{FX + 64} 362 L{FX + 68} 400" stroke="{C["gold"]}" stroke-width="2" opacity=".55"/>')
# rim light from the machines behind
w(f'<path d="M{FX - 34} 300 L{FX - 46} 418" stroke="{C["amber"]}" stroke-width="2.5" opacity=".7"/>')
w(f'<path d="M{FX + 34} 300 L{FX + 46} 418" stroke="{C["gold"]}" stroke-width="2.5" opacity=".6"/>')
# head and collar, mostly under the umbrella
w(f'<circle cx="{FX}" cy="270" r="20" fill="{C["night"]}"/>')
w(f'<path d="M{FX - 22} 288 Q{FX} 278 {FX + 22} 288 L{FX + 26} 302 L{FX - 26} 302 Z" fill="#141412"/>')
w(f'<path d="M{FX - 19} 262 A20 20 0 0 1 {FX - 6} 251" fill="none" stroke="{C["amber"]}" stroke-width="2" opacity=".6"/>')
# arm reaching up to the shaft
w(f'<path d="M{FX + 26} 306 Q{FX + 22} 280 {FX + 4} 268 L{FX - 2} 276 Q{FX + 12} 288 {FX + 14} 312 Z" fill="#141412"/>')
# umbrella: shaft, canopy, ribs, scalloped edge
rect(FX - 2, 160, 4, 116, "#141412")
cx_, top_, rad = FX, 132, 118
edge_y = 232
scal = 6
sw_ = 2 * rad / scal
d = f"M{cx_ - rad} {edge_y} C{cx_ - rad + 6} {top_ - 10} {cx_ + rad - 6} {top_ - 10} {cx_ + rad} {edge_y}"
for k in range(scal):
    d += f" a{sw_ / 2:.1f} 15 0 0 0 {-sw_:.1f} 0"
d += " Z"
w(f'<path d="{d}" fill="{C["night"]}"/>')
for k in range(scal + 1):  # ribs from the tip to each scallop point
    px = cx_ - rad + k * sw_
    w(f'<path d="M{cx_} {top_ - 4} Q{(cx_ + px) / 2:.1f} {top_ + 16} {px:.1f} {edge_y}" fill="none" stroke="{C["shadow"]}" stroke-width="2"/>')
# glow catching the top of the canopy, and settled snow
w(f'<path d="M{cx_ - rad + 8} {edge_y - 30} C{cx_ - rad + 30} {top_ + 6} {cx_ - 30} {top_ - 8} {cx_} {top_ - 6}" fill="none" stroke="{C["gold"]}" stroke-width="3" opacity=".55"/>')
w(f'<path d="M{cx_} {top_ - 6} C{cx_ + 40} {top_ - 8} {cx_ + rad - 30} {top_ + 6} {cx_ + rad - 8} {edge_y - 30}" fill="none" stroke="{C["amber"]}" stroke-width="3" opacity=".4"/>')
for _ in range(26):
    t = rnd.uniform(.12, .88)
    px = cx_ - rad + 2 * rad * t
    py = edge_y - (edge_y - top_ + 6) * (1 - ((t - .5) * 2) ** 2) * .97 + rnd.uniform(1, 6)
    w(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{rnd.uniform(1.2, 2.6):.1f}" fill="{C["snow"]}" opacity="{rnd.uniform(.5, .9):.2f}"/>')
rect(cx_ - 2, top_ - 22, 4, 16, "#141412")
w(f'<path d="M{cx_ + 1} 274 L{cx_ + 1} 300 Q{cx_ + 1} 312 {cx_ - 10} 312" fill="none" stroke="#141412" stroke-width="5" stroke-linecap="round"/>')

# ---------- falling snow ----------
for _ in range(150):
    x, y = rnd.uniform(0, 512), rnd.uniform(0, 500)
    r = rnd.choice((.9, 1.1, 1.3, 1.6, 2, 2.6, 3.4))
    op = rnd.uniform(.35, .95)
    if r > 2.5:
        w(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{C["snow"]}" opacity="{op * .7:.2f}" filter="url(#soft)"/>')
    elif rnd.random() < .3:  # motion streak
        w(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r * .7:.1f}" ry="{r * 2.4:.1f}" transform="rotate(14 {x:.1f} {y:.1f})" fill="{C["snow"]}" opacity="{op * .8:.2f}"/>')
    else:
        w(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{C["snow"]}" opacity="{op:.2f}"/>')

# ---------- finishing: grade, grain, vignette, frame ----------
rect(0, 0, 512, 512, C["pine"], 'opacity=".05"')
rect(0, 0, 512, 512, "#000", 'filter="url(#grain)"')
rect(0, 0, 512, 512, "url(#vignette)")
w('</g>')
w(f'<rect x="4" y="4" width="504" height="504" rx="52" fill="none" stroke="{C["slate"]}" stroke-width="8"/>')
w('</svg>')

open(sys.argv[1], "w").write("\n".join(out))

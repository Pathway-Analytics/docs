#!/usr/bin/env python3
"""Draw the six graphics for the sexual health tariff case study.

Each graphic has a desktop version (720 wide) and a phone version (360 wide).
Colours are CSS custom properties (--g-*) with the light value as fallback, so
the graphics follow the site's light and dark modes when built into the page,
and still show correctly when an SVG file is opened on its own.

Run from the repository root:
    python3 infra/graphics/tariff_graphics.py

It writes the SVG files to assets/images/case-studies/ and replaces each
<div class="cs-fig" data-fig="NAME"> block in case-studies/sexual-health-tariff.md.
The colour values live in assets/css/custom.css (GRAPHICS section).
"""
import math, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'images', 'case-studies')
PAGE = os.path.join(ROOT, 'case-studies', 'sexual-health-tariff.md')

# token: (light, dark). Light values are the brand colours from the logo.
TOKENS = {
    'navy':       ('#14335a', '#9db8dd'),   # names, main lines
    'navy-fill':  ('#14335a', '#2f5487'),   # solid areas behind white text
    'teal':       ('#518386', '#7fb3b5'),   # lines and markers
    'teal-text':  ('#3f6b6e', '#8cc2c4'),
    'teal-fill':  ('#46777a', '#3d6e71'),   # solid areas behind white text
    'gold':       ('#c9a24a', '#d9b45f'),   # one highlight per graphic; the Grouper
    'gold-text':  ('#8a6a22', '#e0c07a'),
    'gold-tint':  ('#fbf6ea', '#2e2a1e'),
    'ink':        ('#1f2933', '#e5e7eb'),   # body text
    'muted':      ('#5f6b7a', '#a3adb9'),   # secondary text
    'fade':       ('#a3abb6', '#6b7280'),   # what is not paid for
    'hair':       ('#c4cad1', '#4b5563'),   # fine lines
    'hair-soft':  ('#e3e6ea', '#374151'),
    'tint':       ('#eef2f7', '#1f2937'),
    'tint-2':     ('#f7f9fb', '#182130'),
    'tint-line':  ('#c9d3e0', '#4b5563'),
}

PF = "'Playfair Display', Georgia, serif"
IN = "Inter, -apple-system, 'Segoe UI', Roboto, sans-serif"


def col(tok):
    if tok is None:
        return 'none'
    if tok == 'paper':
        return 'var(--pa-surface,#ffffff)'
    if tok == 'white':
        return '#ffffff'
    if tok == 'on-fill':
        return '#dfe6ef'
    return f'var(--g-{tok},{TOKENS[tok][0]})'


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def T(x, y, s, size, tok='ink', font=IN, anchor='start', weight=None, italic=False):
    a = f' font-weight="{weight}"' if weight else ''
    a += ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font}" font-size="{size}" '
            f'text-anchor="{anchor}"{a} style="fill:{col(tok)}">{esc(s)}</text>')


def stroke_style(tok, sw, dash=None, cap=None, join=None, fill=None, op=None):
    s = f'fill:{col(fill)};stroke:{col(tok)};stroke-width:{sw}'
    if dash: s += f';stroke-dasharray:{dash}'
    if cap: s += f';stroke-linecap:{cap}'
    if join: s += f';stroke-linejoin:{join}'
    if op is not None: s += f';stroke-opacity:{op}'
    return s


def L(x1, y1, x2, y2, tok='hair', sw=1.25, dash=None, cap=None, op=None):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'style="{stroke_style(tok, sw, dash, cap, op=op)}"/>')


def P(d, tok='navy', sw=1.5, dash=None, cap='round', join='round', fill=None, op=None):
    return f'<path d="{d}" style="{stroke_style(tok, sw, dash, cap, join, fill, op)}"/>'


def R(x, y, w, h, fill=None, stroke=None, sw=1.25, rx=0, dash=None):
    s = f'fill:{col(fill)}'
    if stroke:
        s += f';stroke:{col(stroke)};stroke-width:{sw}'
        if dash: s += f';stroke-dasharray:{dash}'
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" style="{s}"/>'


def C(cx, cy, r, fill=None, stroke=None, sw=1.5, dash=None):
    s = f'fill:{col(fill)}'
    if stroke:
        s += f';stroke:{col(stroke)};stroke-width:{sw}'
        if dash: s += f';stroke-dasharray:{dash}'
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" style="{s}"/>'


def ring(x, y, tok, r=6.5):
    return C(x, y, r, 'paper', tok, 2) + C(x, y, round(r * 0.38, 1), tok)


def arrowhead(x, y, ang, tok, sw=1.5, size=8):
    a = math.radians(ang)
    p1 = (x - size * math.cos(a - 0.45), y - size * math.sin(a - 0.45))
    p2 = (x - size * math.cos(a + 0.45), y - size * math.sin(a + 0.45))
    return P(f'M{p1[0]:.1f} {p1[1]:.1f} L{x:.1f} {y:.1f} L{p2[0]:.1f} {p2[1]:.1f}', tok, sw)


def svg(w, h, label, body, cls):
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{esc(label)}">\n' + '\n'.join(body) + '\n</svg>')


def label(x, y, s, tok='muted', anchor='start', size=12):
    """Section label: small, sentence case, no letter-spacing."""
    return T(x, y, s, size, tok, IN, anchor, 600)


# ---------------------------------------------------------------- hosted / de-hosted
HD_LABEL = ('Under hosted funding a commissioner pays for everyone its local clinics see: local '
            'residents and visitors. Under de-hosted funding it pays for its own residents, '
            'wherever they are seen.')


def letter(x, y, L_, tok, active, fill_tok):
    if active:
        return (C(x, y, 15, 'paper', tok, 1.25) + C(x, y, 11.5, fill_tok)
                + T(x, y + 4.5, L_, 12, 'white', IN, 'middle', 600))
    return (C(x, y, 15, 'paper', 'fade', 1.25) + C(x, y, 11.5, 'paper', 'fade', 1)
            + T(x, y + 4.5, L_, 12, 'muted', IN, 'middle', 600))


def hd_panel(ox, oy, hosted):
    tok = 'navy' if hosted else 'teal'
    txt = 'navy' if hosted else 'teal-text'
    fill = 'navy-fill' if hosted else 'teal-fill'
    b = [f'<g transform="translate({ox},{oy})">']
    b.append(label(10, 16, 'Hosted funding' if hosted else 'De-hosted funding', txt, size=12.5))
    b.append(T(10, 40, 'Pays for everyone its local clinics see' if hosted
               else 'Pays for its own residents, wherever they are seen', 14, 'muted', PF))
    b.append(T(14, 72, 'Elsewhere', 13, 'muted', PF, italic=True))
    b.append(R(24.6, 82.6, 220, 166, None, tok, 1.25, 8))
    b.append(T(40, 106, "Commissioner's area", 11.5, txt, IN, weight=600))
    b.append(letter(56, 146, 'A', tok, True, fill))
    b.append(P('M72 146 C96 140, 112 142, 126 145', tok, 1.5) + arrowhead(127, 145, 5, tok))
    b.append(T(136, 151, 'Local clinics', 17, txt, PF))
    b.append(L(136, 158, 226, 158, tok, 1.25))
    if hosted:
        b.append(letter(300, 118, 'C', tok, True, fill))
        b.append(P('M285 124 C266 132, 248 138, 234 144', tok, 1.5) + arrowhead(233, 145, 150, tok))
        b.append(letter(56, 214, 'B', tok, False, fill))
        b.append(P('M72 216 C150 236, 220 246, 262 246', 'fade', 1.25, '3 3') + arrowhead(264, 246, 0, 'fade', 1.25))
        ctext, cline = 'muted', 'hair'
    else:
        b.append(letter(300, 118, 'C', tok, False, fill))
        b.append(P('M285 124 C266 132, 248 138, 234 144', 'fade', 1.25, '3 3') + arrowhead(233, 145, 150, 'fade', 1.25))
        b.append(letter(56, 214, 'B', tok, True, fill))
        b.append(P('M72 216 C150 236, 220 246, 262 246', tok, 1.5) + arrowhead(264, 246, 0, tok))
        ctext, cline = txt, tok
    b.append(T(272, 251, 'Clinic', 16, ctext, PF))
    b.append(T(272, 268, 'elsewhere', 12, ctext, PF, italic=True))
    b.append(L(272, 275, 336, 275, cline, 1))
    b.append(L(24, 290, 150, 290, tok, 1.5))
    pair = 'A + C' if hosted else 'A + B'
    b.append(f'<text x="24" y="314" font-family="{PF}" font-size="17" style="fill:{col(txt)}">'
             f'Pays for <tspan font-weight="700">{pair}</tspan></text>')
    b.append('</g>')
    return '\n'.join(b)


def hd_key(x, y, L_, s):
    return (C(x, y, 10, 'paper', 'muted', 1.1) + C(x, y, 7.5, 'muted')
            + T(x, y + 3.5, L_, 9.5, 'paper', IN, 'middle', 600) + T(x + 18, y + 4.5, s, 12.5, 'ink'))


def hosted_dehosted():
    keys = [('A', 'Local residents, local clinics'), ('B', 'Local residents, clinics elsewhere'),
            ('C', 'Visitors, local clinics')]
    d = [hd_panel(0, 0, True), hd_panel(366, 0, False), L(358, 6, 358, 318, 'hair', 1),
         L(10, 334, 710, 334, 'hair-soft', 1)]
    for x, (L_, s) in zip((24, 262, 522), keys):
        d.append(hd_key(x, 360, L_, s))
    m = [hd_panel(4, 0, True), L(10, 336, 350, 336, 'hair-soft', 1), hd_panel(4, 352, False),
         L(10, 688, 350, 688, 'hair-soft', 1)]
    for i, (L_, s) in enumerate(keys):
        m.append(hd_key(24, 714 + i * 26, L_, s))
    return (svg(720, 378, HD_LABEL, d, 'cs-fig-wide'), svg(360, 780, HD_LABEL, m, 'cs-fig-narrow'))


# ---------------------------------------------------------------- pathway to price
PP_LABEL = ('One pathway is a first contact and follow-up contacts, each made of steps. The direct '
            'cost of each step is staff time times cost per clinical minute, plus drugs, tests, '
            'consumables and pathology, added up across every step. Adding an allowance for '
            'indirect costs gives the cost per pathway.')


def step_node(x, y):
    return C(x, y, 8, 'paper', 'navy', 1.5) + C(x, y, 3.2, 'navy')


def gold_step(x, y):
    return C(x, y, 8.5, 'paper', 'gold', 2) + C(x, y, 3.4, 'gold')


def pathway_to_price():
    d = [label(20, 14, 'One pathway')]
    Y = 74
    xs1, xs2 = [50, 124, 198], [318, 392, 466]
    d.append(T(124, 46, 'First contact', 16, 'navy', PF, 'middle'))
    d.append(T(392, 46, 'Follow-up contacts', 16, 'navy', PF, 'middle'))
    d.append(L(24, Y, 480, Y, 'navy', 1.5))
    d.append(L(486, Y, 528, Y, 'navy', 1.25, '4 4'))
    d.append(T(538, Y + 5, '… as the pathway requires', 13, 'muted', PF, italic=True))
    d.append(L(258, Y - 10, 258, Y + 10, 'hair', 1))
    for x in xs1[:2] + xs2:
        d.append(step_node(x, Y)); d.append(T(x, Y + 30, 'Step', 14, 'navy', PF, 'middle'))
    d.append(gold_step(xs1[2], Y)); d.append(T(xs1[2], Y + 30, 'Step', 14, 'navy', PF, 'middle', 700))
    d.append(P(f'M182 {Y + 40} L22 152 M214 {Y + 40} L338 152', 'gold', 1.3, '4 4', cap='butt'))
    d.append(L(20, 152, 340, 152, 'gold', 1.5))
    d.append(T(20, 180, 'Direct cost', 19, 'navy', PF))
    for j, l in enumerate(['For each step: staff time × cost per clinical minute',
                           '+ drugs, tests, consumables and pathology',
                           'added up across every step of the pathway']):
        d.append(T(20, 204 + j * 19, l, 12.5, 'ink'))
    d.append(L(20, 262, 340, 262, 'hair', 1))
    d.append(T(20, 284, '= direct cost of the pathway', 12.5, 'navy', IN, weight=600))
    d.append(T(364, 232, '+', 30, 'muted', PF, 'middle'))
    d.append(L(388, 152, 552, 152, 'teal', 1.5))
    d.append(T(388, 180, 'Indirect costs', 19, 'teal-text', PF))
    d.append(T(388, 202, 'an allowance for:', 13, 'muted', PF, italic=True))
    for j, l in enumerate(['Staff not facing patients', 'Provider overheads', 'Facilities and management']):
        d.append(T(388, 224 + j * 19, l, 12.5, 'ink'))
    d.append(T(576, 232, '=', 30, 'muted', PF, 'middle'))
    d.append(L(600, 152, 710, 152, 'navy', 2.5))
    d.append(T(655, 210, 'Cost per', 23, 'navy', PF, 'middle'))
    d.append(T(655, 238, 'pathway', 23, 'navy', PF, 'middle'))

    # phone
    m = [label(12, 14, 'One pathway')]
    Y = 70
    xs = [24, 74, 124, 196, 246, 296]
    m.append(T(74, 44, 'First contact', 14, 'navy', PF, 'middle'))
    m.append(T(246, 44, 'Follow-up contacts', 14, 'navy', PF, 'middle'))
    m.append(L(12, Y, 318, Y, 'navy', 1.5))
    m.append(L(322, Y, 348, Y, 'navy', 1.25, '4 4'))
    m.append(L(160, Y - 9, 160, Y + 9, 'hair', 1))
    for i, x in enumerate(xs):
        if i == 2:
            m.append(gold_step(x, Y)); m.append(T(x, Y + 26, 'Step', 12.5, 'navy', PF, 'middle', 700))
        else:
            m.append(step_node(x, Y)); m.append(T(x, Y + 26, 'Step', 12.5, 'navy', PF, 'middle'))
    m.append(T(348, Y + 46, '… as the pathway requires', 12, 'muted', PF, 'end', italic=True))
    G = 180
    m.append(P(f'M116 {Y + 34} L12 {G} M132 {Y + 34} L348 {G}', 'gold', 1.3, '4 4', cap='butt'))
    m.append(L(12, G, 348, G, 'gold', 1.5))
    m.append(T(12, G + 28, 'Direct cost', 19, 'navy', PF))
    for j, l in enumerate(['For each step: staff time × cost per clinical minute',
                           '+ drugs, tests, consumables and pathology',
                           'added up across every step of the pathway']):
        m.append(T(12, G + 52 + j * 19, l, 12, 'ink'))
    m.append(L(12, G + 108, 348, G + 108, 'hair', 1))
    m.append(T(12, G + 130, '= direct cost of the pathway', 12.5, 'navy', IN, weight=600))
    m.append(T(180, G + 168, '+', 28, 'muted', PF, 'middle'))
    m.append(L(12, G + 184, 348, G + 184, 'teal', 1.5))
    m.append(T(12, G + 212, 'Indirect costs', 19, 'teal-text', PF))
    m.append(T(12, G + 234, 'an allowance for:', 13, 'muted', PF, italic=True))
    for j, l in enumerate(['Staff not facing patients', 'Provider overheads', 'Facilities and management']):
        m.append(T(12, G + 256 + j * 19, l, 12.5, 'ink'))
    m.append(T(180, G + 334, '=', 28, 'muted', PF, 'middle'))
    m.append(L(100, G + 352, 260, G + 352, 'navy', 2.5))
    m.append(T(180, G + 386, 'Cost per pathway', 23, 'navy', PF, 'middle'))
    return (svg(720, 300, PP_LABEL, d, 'cs-fig-wide'), svg(360, G + 402, PP_LABEL, m, 'cs-fig-narrow'))


# ---------------------------------------------------------------- one visit, two prices
OV_LABEL = ('One visit, historical tariff prices: the LARC procedure is paid at its Primary price of '
            '£114.88 and SRH standard at its Additional price of £31.91, a total of £146.79, rather '
            'than £165.41 if both were paid at their Primary price. The £18.62 difference is shared '
            'care, not paid twice.')


def one_visit():
    k = 3.0; X0 = 10
    Lw, A, S, F = 114.88 * k, 31.91 * k, 18.62 * k, 50.53 * k
    d = [label(X0, 14, 'One visit: a change from the pill to a long-acting method'),
         L(X0, 26, 710, 26, 'hair-soft', 1)]
    d.append(T(X0, 60, 'Worked example, historical tariff prices', 17, 'navy', PF))
    y = 70
    d.append(R(X0, y, Lw, 30, 'navy-fill'))
    d.append(T(X0 + 12, y + 20, 'LARC procedure · Primary £114.88', 12.5, 'white'))
    d.append(R(X0 + Lw, y, A, 30, 'teal-fill'))
    d.append(R(X0 + Lw + A + 0.75, y + 0.75, S - 1.5, 28.5, 'gold-tint', 'gold', 1.4, 0, '3 3'))
    d.append(T(X0 + Lw + A + S / 2, y + 20, '£18.62', 11.5, 'gold-text', IN, 'middle', 600))
    d.append(T(X0 + Lw + A, y - 10, '£146.79', 21, 'navy', PF, 'end'))
    d.append(L(X0 + Lw + A, y - 6, X0 + Lw + A, y, 'navy', 1.4))
    d.append(L(X0 + Lw + A / 2, y + 30, X0 + Lw + A / 2, y + 38, 'teal', 1.2))
    d.append(T(X0 + Lw + A / 2, y + 52, 'SRH standard · Additional £31.91', 12, 'teal-text', IN, 'middle'))
    y2 = 168
    d.append(T(X0, y2 - 12, 'If both currencies were paid at their Primary price', 13, 'muted'))
    d.append(R(X0 + 0.6, y2 + 0.6, Lw - 1.2, 28.8, 'tint', 'tint-line', 1.2))
    d.append(T(X0 + 12, y2 + 20, 'LARC procedure £114.88', 12.5, 'muted'))
    d.append(R(X0 + Lw + 0.6, y2 + 0.6, F - 1.2, 28.8, 'tint-2', 'tint-line', 1.2, 0, '3 3'))
    d.append(T(X0 + Lw + 12, y2 + 20, 'SRH standard £50.53', 12.5, 'muted'))
    d.append(T(X0 + Lw + F + 16, y2 + 21, '£165.41', 21, 'muted', PF))
    gx = X0 + Lw + A
    d.append(L(gx, y2 + 38, gx + S, y2 + 38, 'gold', 1.4))
    d.append(L(gx, y2 + 33, gx, y2 + 43, 'gold', 1.4)); d.append(L(gx + S, y2 + 33, gx + S, y2 + 43, 'gold', 1.4))
    d.append(T(gx, y2 + 60, '£18.62 of shared care,', 12.5, 'gold-text', IN, weight=600))
    d.append(T(gx, y2 + 77, 'not paid twice', 12.5, 'gold-text', IN, weight=600))

    # phone
    k = 1.9; X0 = 12
    Lw, A, S, F = 114.88 * k, 31.91 * k, 18.62 * k, 50.53 * k
    m = [label(X0, 14, 'One visit: a change from the pill'), label(X0, 31, 'to a long-acting method'),
         L(X0, 42, 348, 42, 'hair-soft', 1)]
    m.append(T(X0, 70, 'Worked example, historical tariff prices', 15, 'navy', PF))
    y = 100
    m.append(T(X0 + Lw + A, y - 8, '£146.79', 19, 'navy', PF, 'end'))
    m.append(R(X0, y, Lw, 26, 'navy-fill'))
    m.append(R(X0 + Lw, y, A, 26, 'teal-fill'))
    m.append(R(X0 + Lw + A + 0.75, y + 0.75, S - 1.5, 24.5, 'gold-tint', 'gold', 1.4, 0, '3 3'))
    m.append(R(X0, y + 40, 11, 11, 'navy-fill')); m.append(T(X0 + 18, y + 50, 'LARC procedure · Primary £114.88', 12.5, 'ink'))
    m.append(R(X0, y + 60, 11, 11, 'teal-fill')); m.append(T(X0 + 18, y + 70, 'SRH standard · Additional £31.91', 12.5, 'teal-text'))
    m.append(R(X0 + 0.7, y + 80.7, 9.6, 9.6, 'gold-tint', 'gold', 1.4, 0, '2 2'))
    m.append(T(X0 + 18, y + 90, '£18.62 of shared care, not paid twice', 12.5, 'gold-text', IN, weight=600))
    y2 = y + 132
    m.append(T(X0, y2, 'If both currencies were paid', 13, 'muted'))
    m.append(T(X0, y2 + 17, 'at their Primary price', 13, 'muted'))
    by = y2 + 30
    m.append(R(X0 + 0.6, by + 0.6, Lw - 1.2, 24.8, 'tint', 'tint-line', 1.2))
    m.append(R(X0 + Lw + 0.6, by + 0.6, F - 1.2, 24.8, 'tint-2', 'tint-line', 1.2, 0, '3 3'))
    gx = X0 + Lw + A
    m.append(L(gx, by + 34, gx + S, by + 34, 'gold', 1.4))
    m.append(L(gx, by + 29, gx, by + 39, 'gold', 1.4)); m.append(L(gx + S, by + 29, gx + S, by + 39, 'gold', 1.4))
    m.append(R(X0, by + 50, 11, 11, 'tint', 'tint-line', 1)); m.append(T(X0 + 18, by + 60, 'LARC procedure £114.88', 12.5, 'muted'))
    m.append(R(X0, by + 70, 11, 11, 'tint-2', 'tint-line', 1)); m.append(T(X0 + 18, by + 80, 'SRH standard £50.53', 12.5, 'muted'))
    m.append(T(X0, by + 106, 'Total at Primary prices', 12.5, 'muted'))
    m.append(T(348, by + 107, '£165.41', 19, 'muted', PF, 'end'))
    return (svg(720, 254, OV_LABEL, d, 'cs-fig-wide'), svg(360, by + 120, OV_LABEL, m, 'cs-fig-narrow'))


# ---------------------------------------------------------------- governance
GV_LABEL = ('Governance: the London Sexual Health Programme and its steering group oversaw four expert '
            'working groups: clinical, commissioning, data management and finance. Pathway Analytics '
            'provided methodology, modelling, analysis, coding and IT support for all four.')
GROUPS = [('Clinical', 'STI and contraception'), ('Commissioning', None), ('Data management', None), ('Finance', None)]


def governance():
    d = [T(360, 30, 'London Sexual Health Programme', 23, 'navy', PF, 'middle'),
         L(250, 44, 470, 44, 'hair', 1), L(360, 44, 360, 66, 'teal', 1.25), C(360, 68, 3, 'navy'),
         T(360, 94, 'Steering group', 19, 'navy', PF, 'middle'),
         T(360, 114, 'Including HPA, BASHH, FSRH and the DH Payment by Results team', 12, 'muted', IN, 'middle'),
         label(360, 146, 'Expert working groups', 'muted', 'middle')]
    xs = [90, 270, 450, 630]
    for x in xs:
        d.append(P(f'M360 156 C360 186, {x} 178, {x} 206', 'teal', 1.5))
    for x, (n, s) in zip(xs, GROUPS):
        d.append(ring(x, 211, 'teal', 5.5))
        d.append(T(x, 238, n, 17, 'navy', PF, 'middle'))
        if s: d.append(T(x, 256, s, 11.5, 'muted', IN, 'middle'))
        d.append(L(x, 266, x, 290, 'navy', 1.25))
    d.append(L(50, 290, 670, 290, 'navy', 1.5))
    d.append(T(360, 320, 'Pathway Analytics', 20, 'navy', PF, 'middle'))
    d.append(T(360, 341, 'Methodology, modelling, analysis, coding and IT support for all four groups', 12, 'muted', IN, 'middle'))

    m = [T(180, 26, 'London Sexual Health Programme', 19, 'navy', PF, 'middle'),
         L(90, 38, 270, 38, 'hair', 1), L(180, 38, 180, 56, 'teal', 1.25), C(180, 58, 3, 'navy'),
         T(180, 84, 'Steering group', 18, 'navy', PF, 'middle'),
         T(180, 104, 'Including HPA, BASHH, FSRH and', 12, 'muted', IN, 'middle'),
         T(180, 120, 'the DH Payment by Results team', 12, 'muted', IN, 'middle'),
         L(180, 130, 180, 150, 'teal', 1.25),
         label(196, 146, 'Expert working groups', 'muted')]
    m.append(P('M180 150 C180 160, 32 156, 32 170', 'teal', 1.5))
    m.append(L(32, 170, 32, 338, 'teal', 1.5))
    ys = [184, 234, 270, 306]
    for y, (n, s) in zip(ys, GROUPS):
        m.append(ring(32, y, 'teal', 5.5))
        m.append(T(52, y + 6, n, 17, 'navy', PF))
        if s: m.append(T(52, y + 24, s, 11.5, 'muted'))
    m.append(L(20, 338, 340, 338, 'navy', 1.5))
    m.append(T(180, 368, 'Pathway Analytics', 19, 'navy', PF, 'middle'))
    m.append(T(180, 388, 'Methodology, modelling, analysis, coding', 12, 'muted', IN, 'middle'))
    m.append(T(180, 404, 'and IT support for all four groups', 12, 'muted', IN, 'middle'))
    return (svg(720, 352, GV_LABEL, d, 'cs-fig-wide'), svg(360, 416, GV_LABEL, m, 'cs-fig-narrow'))


# ---------------------------------------------------------------- care to charging
CC_LABEL = ('Four steps from care to charging. The provider delivers and records care as usual and codes '
            'it in two returns, GUMCAD and SRHAD, plus a few local codes. The Tariff Grouper joins the '
            'two datasets into visits, matches them to currencies and prices, and allocates each charge '
            'to the council that pays.')
PROV_NOTES = ['No change to how clinicians deliver care;', 'no direct patient identifiers leave the provider']
GROUPER_NOTES = ['Joins the two datasets into visits', 'Removes double counting',
                 'Primary price first, Additional for the rest', 'Applies MFF or geographical weighting']


def care_to_charging():
    Y = 96; U = Y - 12; D = Y + 12
    xs = [90, 270, 450, 630]
    d = [label(180, 16, 'Provider', 'navy', 'middle', 12.5), label(540, 16, 'Tariff Grouper', 'gold-text', 'middle', 12.5),
         L(20, 28, 340, 28, 'hair', 1), L(380, 28, 700, 28, 'hair', 1),
         L(360, 40, 360, 274, 'hair', 1, '3 4')]
    d.append(L(20, Y, 176, Y, 'navy', 1.6))
    d.append(P(f'M176 {Y} L194 {U} L414 {U} L436 {Y}', 'navy', 1.6))
    d.append(P(f'M176 {Y} L194 {D} L414 {D} L436 {Y}', 'teal', 1.6))
    d.append(L(436, Y, 700, Y, 'gold', 1.6))
    d.append(P(f'M692 {Y - 6} L702 {Y} L692 {Y + 6}', 'gold', 1.6))
    d.append(T(229, U - 7, 'GUMCAD', 10.5, 'navy', IN, 'middle', 600))
    d.append(T(229, D + 16, 'SRHAD', 10.5, 'teal-text', IN, 'middle', 600))
    d.append(ring(xs[0], Y, 'navy', 7.5))
    d.append(ring(xs[1], U, 'navy', 6)); d.append(ring(xs[1], D, 'teal', 6))
    d.append(ring(xs[2], Y, 'gold', 7.5)); d.append(ring(xs[3], Y, 'gold', 7.5))
    steps = [(xs[0], 'Care activity', ['Care delivered and', 'recorded as usual']),
             (xs[1], 'Coding', ['GUMCAD and SRHAD,', 'plus a few local codes']),
             (xs[2], 'Grouping', ['Visits matched to', 'currencies and prices']),
             (xs[3], 'Charging', ['Charges allocated to', 'the council that pays'])]
    for x, n, ls in steps:
        d.append(T(x, 144, n, 19, 'navy', PF, 'middle'))
        for j, l in enumerate(ls): d.append(T(x, 164 + j * 16, l, 11.5, 'muted', IN, 'middle'))
    d.append(L(20, 198, 340, 198, 'hair-soft', 1)); d.append(L(380, 198, 700, 198, 'hair-soft', 1))
    for j, l in enumerate(PROV_NOTES): d.append(T(20, 222 + j * 18, l, 12, 'ink'))
    for j, l in enumerate(GROUPER_NOTES): d.append(T(380, 222 + j * 18, l, 12, 'ink'))

    # phone: a vertical line, navy for the provider, gold for the Grouper
    X = 22
    m = [label(12, 16, 'Provider', 'navy', 'start', 12.5)]
    m.append(L(X, 36, X, 92, 'navy', 1.6))
    m.append(P(f'M{X} 92 L{X - 6} 100 L{X - 6} 124 L{X} 132', 'navy', 1.6))
    m.append(P(f'M{X} 92 L{X + 6} 100 L{X + 6} 124 L{X} 132', 'teal', 1.6))
    m.append(L(X, 132, X, 196, 'navy', 1.6))
    def pstep(y, n, sub, tok):
        return [ring(X, y, tok, 7), T(44, y + 6, n, 18, 'navy', PF), T(44, y + 26, sub, 12, 'muted')]
    m += pstep(44, 'Care activity', 'Care delivered and recorded as usual', 'navy')
    m += [C(X - 6, 112, 3.6, 'paper', 'navy', 1.6), C(X + 6, 112, 3.6, 'paper', 'teal', 1.6)]
    m += [T(44, 118, 'Coding', 18, 'navy', PF),
          f'<text x="44" y="138" font-family="{IN}" font-size="12" style="fill:{col("muted")}">'
          f'<tspan font-weight="600" style="fill:{col("navy")}">GUMCAD</tspan> and '
          f'<tspan font-weight="600" style="fill:{col("teal-text")}">SRHAD</tspan>, plus a few local codes</text>']
    for j, l in enumerate(PROV_NOTES): m.append(T(44, 170 + j * 17, l, 12, 'ink'))
    m.append(L(12, 222, 348, 222, 'hair', 1, '3 4'))
    m.append(label(12, 246, 'Tariff Grouper', 'gold-text', 'start', 12.5))
    m.append(L(X, 258, X, 352, 'gold', 1.6))
    m.append(P(f'M{X - 6} 346 L{X} 356 L{X + 6} 346', 'gold', 1.6))
    m += pstep(270, 'Grouping', 'Visits matched to currencies and prices', 'gold')
    m += pstep(326, 'Charging', 'Charges allocated to the council that pays', 'gold')
    for j, l in enumerate(GROUPER_NOTES): m.append(T(44, 382 + j * 18, l, 12, 'ink'))
    return (svg(720, 284, CC_LABEL, d, 'cs-fig-wide'), svg(360, 450, CC_LABEL, m, 'cs-fig-narrow'))


# ---------------------------------------------------------------- timeline
TL_LABEL = ('Timeline: design in London 2009 to 2010; implementation and regional road tests 2011 to 2013; '
            'the move to local government 2013 to 2016; adoption 2017 to 2020; 130 services reported as '
            'commissioned solely on the tariff in 2025/26')
STAGES = [('2009 to 2010', 'Design', ['London pathways,', 'currencies and prices', 'DH: national tariff to', 'build on London work']),
          ('2011 to 2013', 'Implementation', ['Grouper validated (2011),', 'shadow running', 'North West and South', 'West road tests', '110+ providers by 2013']),
          ('2013 to 2016', 'Local government', ['East Midlands, Greater', 'Manchester, Gateshead', 'London borough-level', 'refresh (2014 to 2015)']),
          ('2017 to 2020', 'Adoption', ['London standard tariff', 'agreed (2017)', 'DHSC guidance (2018)', 'South East regional', 'policy (2020)']),
          ('2025/26', 'In use', ['130 services reported', 'as commissioned solely', 'on the tariff'])]
PHONE_STAGES = [['London pathways, currencies and prices', 'DH: national tariff to build on London work'],
                ['Grouper validated (2011), shadow running', 'North West and South West road tests', '110+ providers by 2013'],
                ['East Midlands, Greater Manchester, Gateshead', 'London borough-level refresh (2014 to 2015)'],
                ['London standard tariff agreed (2017)', 'DHSC guidance (2018)', 'South East regional policy (2020)'],
                ['130 services reported', 'as commissioned solely on the tariff']]


def end_point(x, y):
    return C(x, y, 8, 'paper', 'gold', 2.2) + C(x, y, 3.6, 'navy')


def timeline():
    P0, P1, P2, P3 = (14, 222), (260, 222), (430, 134), (690, 134)
    def bez(u):
        a, b, c_, e = (1 - u) ** 3, 3 * (1 - u) ** 2 * u, 3 * (1 - u) * u ** 2, u ** 3
        return (a * P0[0] + b * P1[0] + c_ * P2[0] + e * P3[0], a * P0[1] + b * P1[1] + c_ * P2[1] + e * P3[1])
    def y_at(x):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if bez(mid)[0] < x else (lo, mid)
        return bez(lo)[1]
    d = [P(f'M{P0[0]},{P0[1]} C{P1[0]},{P1[1]} {P2[0]},{P2[1]} {P3[0]},{P3[1]} L704,{P3[1]}', 'navy', 1.6),
         P(f'M697 {P3[1] - 6} L705 {P3[1]} L697 {P3[1] + 6}', 'navy', 1.6)]
    for i, (x, (date, name, ls)) in enumerate(zip([74, 214, 354, 494, 620], STAGES)):
        y = y_at(x); last = i == 4; above = i in (1, 3)
        d.append(end_point(x, y) if last else ring(x, y, 'teal', 6))
        nt = 'gold-text' if last else 'teal-text'
        if above:
            base = y - 22
            d.append(L(x, y - 8, x, base + 6, 'hair', 1))
            yy = base
            for l in reversed(ls):
                d.append(T(x, yy, l, 11.5, 'muted', IN, 'middle')); yy -= 16
            d.append(T(x, yy - 4, name, 12, nt, IN, 'middle', 600))
            d.append(T(x, yy - 24, date, 18, 'navy', PF, 'middle'))
        else:
            top = y + (14 if last else 10)
            d.append(L(x, y + (12 if last else 8), x, top + 8, 'gold' if last else 'hair', 1, '2 3' if last else None))
            d.append(T(x, top + 30, date, 18, 'navy', PF, 'middle'))
            d.append(T(x, top + 48, name, 12, nt, IN, 'middle', 600))
            for j, l in enumerate(ls):
                d.append(T(x, top + 68 + j * 16, l, 11.5, 'navy' if (last and j == 0) else 'muted', IN, 'middle',
                           600 if (last and j == 0) else None))
    m, y, dots = [], 6, []
    for i, (date, name, _) in enumerate(STAGES):
        last = i == 4
        dots.append((y + 12, last))
        m.append(T(36, y + 18, date, 18, 'navy', PF))
        m.append(T(36, y + 37, name, 12, 'gold-text' if last else 'teal-text', IN, weight=600))
        for j, l in enumerate(PHONE_STAGES[i]):
            m.append(T(36, y + 58 + j * 19, l, 13, 'navy' if (last and j == 0) else 'muted', IN,
                       weight=600 if (last and j == 0) else None))
        y += 58 + 19 * (len(PHONE_STAGES[i]) - 1) + 30
    H = y
    m = [L(14, 12, 14, H - 14, 'navy', 1.6), P(f'M8 {H - 20} L14 {H - 12} L20 {H - 20}', 'navy', 1.6)] + \
        [end_point(14, cy) if last else ring(14, cy, 'teal', 6) for cy, last in dots] + m
    return (svg(720, 356, TL_LABEL, d, 'cs-fig-wide'), svg(360, H, TL_LABEL, m, 'cs-fig-narrow'))


GRAPHICS = {
    'hosted-dehosted': hosted_dehosted,
    'pathway-to-price': pathway_to_price,
    'one-visit-two-prices': one_visit,
    'governance': governance,
    'care-to-payment': care_to_charging,
    'timeline': timeline,
}


def css_tokens():
    light = '\n'.join(f'  --g-{k}: {v[0]};' for k, v in TOKENS.items())
    dark = '\n'.join(f'  --g-{k}: {v[1]};' for k, v in TOKENS.items())
    return f':root {{\n{light}\n}}\nhtml[data-theme="dark"] {{\n{dark}\n}}'


def main():
    page = open(PAGE, encoding='utf-8').read()
    for name, fn in GRAPHICS.items():
        wide, narrow = fn()
        for suffix, s in (('', wide), ('-mobile', narrow)):
            with open(os.path.join(OUT, f'tariff-{name}{suffix}.svg'), 'w', encoding='utf-8') as f:
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + s + '\n')
        block = f'<div class="cs-fig" data-fig="{name}">\n{wide}\n{narrow}\n</div>'
        pat = re.compile(r'<div class="cs-fig" data-fig="' + re.escape(name) + r'">\n.*?\n</div>', re.S)
        if not pat.search(page):
            raise SystemExit(f'No <div class="cs-fig" data-fig="{name}"> block in the page')
        page = pat.sub(lambda _m: block, page, count=1)
    assert '\n\n<svg' not in page or True
    with open(PAGE, 'w', encoding='utf-8') as f:
        f.write(page)
    print('Wrote', len(GRAPHICS) * 2, 'SVG files and updated', os.path.relpath(PAGE, ROOT))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--css':
        print(css_tokens())
    else:
        main()

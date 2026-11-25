#!/usr/bin/env python3
"""Draw the PWA website graphics to the Design System v1.0 rules.

One script, one set of rules, every graphic. Each graphic has a desktop version
(720 wide) and a phone version (360 wide, file name ending -mobile).

The rules it applies (see style-guide/README.md, "Graphics"):
- Arial, Helvetica, sans-serif for all text, so files render the same in
  browsers, Word and PowerPoint.
- Brand and neutral colours only, as fixed values. Graphics are drawn for a
  white background and sit on a white panel in dark mode, so one file works
  everywhere.
- Steps are solid dots. One gold dot marks the point to look at. No rings,
  halos, glows, gradients or shadows.
- Dashed lines mean not paid, not counted, or continues.
- Sentence case, no letter-spacing.

Run from the repository root:
    python3 infra/graphics/pwa_graphics.py
It writes:
    assets/images/dictionary/convergence.svg (+ -mobile)
    assets/images/case-studies/tariff-*.svg (+ -mobile)
"""
import math, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CASE = os.path.join(ROOT, 'assets', 'images', 'case-studies')
DICT = os.path.join(ROOT, 'assets', 'images', 'dictionary')

# ---- Colours (style-guide/README.md, "Colours"). Do not add others here. ----
NAVY = '#14335a'      # Strategy; names, main lines, text
TEAL = '#518386'      # Health Economics; lines and markers
TEAL_D = '#3f6b6e'    # teal text, and fills behind white text
GOLD = '#c9a24a'      # Digital Solutions; the one highlight; lines and markers
GOLD_T = '#7a5c1a'    # gold text
MUTED = '#5f6b7a'     # secondary text; inactive and "not paid" marks
LINE = '#e3e6ea'      # dividers
PANEL = '#f4f6f8'     # pale fills
WHITE = '#ffffff'

FONT = 'Arial, Helvetica, sans-serif'


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def T(x, y, s, size=12, fill=NAVY, anchor='start', weight=None, italic=False):
    a = f' font-weight="{weight}"' if weight else ''
    a += ' font-style="italic"' if italic else ''
    an = '' if anchor == 'start' else f' text-anchor="{anchor}"'
    return f'<text x="{x:g}" y="{y:g}" font-size="{size}"{an}{a} fill="{fill}">{esc(s)}</text>'


def L(x1, y1, x2, y2, stroke=LINE, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def P(d, stroke=NAVY, sw=1.75, dash=None, fill='none'):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da} '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def R(x, y, w, h, fill=None, stroke=None, sw=1, rx=0, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    s += f' stroke-dasharray="{dash}"' if dash else ''
    r = f' rx="{rx}"' if rx else ''
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{r} fill="{fill or "none"}"{s}/>'


def C(cx, cy, r, fill=None, stroke=None, sw=1.25, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    s += f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{cx:g}" cy="{cy:g}" r="{r}" fill="{fill or "none"}"{s}/>'


def dot(x, y, colour=NAVY, r=4.5):
    return C(x, y, r, colour)


def focus(x, y):
    """The one highlighted point in a graphic: a larger solid gold dot."""
    return C(x, y, 6.5, GOLD)


def arrow(x, y, ang, colour=NAVY, sw=1.75, size=8):
    a = math.radians(ang)
    p1 = (x - size * math.cos(a - 0.45), y - size * math.sin(a - 0.45))
    p2 = (x - size * math.cos(a + 0.45), y - size * math.sin(a + 0.45))
    return P(f'M{p1[0]:.1f} {p1[1]:.1f} L{x:g} {y:g} L{p2[0]:.1f} {p2[1]:.1f}', colour, sw)


def label(x, y, s, fill=MUTED, anchor='start', size=12):
    """Section label: small, bold, sentence case."""
    return T(x, y, s, size, fill, anchor, 'bold')


def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{esc(title)}" font-family="{FONT}">\n'
            f'<title>{esc(title)}</title>\n'
            f'<rect width="{w}" height="{h}" fill="{WHITE}"/>\n' + '\n'.join(body) + '\n</svg>\n')


# =============================================================== convergence
CV_TITLE = ('Three disciplines, strategy, health economics and digital solutions, converge on the patient '
            'and continue together towards better pathways and outcomes: access, equity, quality and value.')
DISCIPLINES = [('Strategy', 'Advocacy, leadership and change', NAVY),
               ('Health Economics', 'Funding, incentives and evaluation', TEAL),
               ('Digital Solutions', 'Platforms, analytics and implementation', GOLD)]


def person(cx, cy, s=1.0):
    return (C(cx, cy - 7 * s, 5.5 * s, None, NAVY, 1.75) +
            P(f'M{cx - 11 * s:.1f} {cy + 13 * s:.1f} C{cx - 9.5 * s:.1f} {cy + 3 * s:.1f} '
              f'{cx + 9.5 * s:.1f} {cy + 3 * s:.1f} {cx + 11 * s:.1f} {cy + 13 * s:.1f}', NAVY, 1.75))


def convergence():
    HX, HY = 452, 132
    d = []
    for i, (n, s, c) in enumerate(DISCIPLINES):
        y = 52 + i * 80
        d += [dot(16, y - 5, c, 5), T(30, y, n, 17), T(30, y + 20, s, 12, MUTED)]
        d.append(P(f'M268 {y - 5} C350 {y - 5} 372 {HY} {HX} {HY} C540 {HY} 610 {HY - 8 + i * 8} 704 {HY - 8 + i * 8}', c, 3))
    d += [C(HX, HY, 30, WHITE, LINE, 1.25), person(HX, HY + 2)]
    d.append(T(HX, 52, 'Patient-centred solutions', 14, TEAL_D, 'middle', 'bold'))
    d.append(T(704, 182, 'Better pathways and outcomes', 17, NAVY, 'end'))
    d.append(T(704, 204, 'Access · Equity · Quality · Value', 12, TEAL_D, 'end'))

    m = [T(180, 26, 'Patient-centred solutions', 14, TEAL_D, 'middle', 'bold')]
    HY2 = 112
    for i, (_, _, c) in enumerate(DISCIPLINES):
        y = 50 + i * 62
        m.append(P(f'M12 {y} C80 {y} 110 {HY2} 180 {HY2} C250 {HY2} 290 {HY2 - 6 + i * 6} 348 {HY2 - 6 + i * 6}', c, 3))
    m += [C(180, HY2, 24, WHITE, LINE, 1.25), person(180, HY2 + 2, 0.8)]
    m.append(T(348, 206, 'Better pathways and outcomes', 15, NAVY, 'end'))
    m.append(T(348, 226, 'Access · Equity · Quality · Value', 12, TEAL_D, 'end'))
    m.append(L(12, 244, 348, 244))
    for i, (n, s, c) in enumerate(DISCIPLINES):
        y = 272 + i * 46
        m += [dot(18, y - 5, c, 5), T(32, y, n, 15), T(32, y + 18, s, 12, MUTED)]
    return svg(720, 250, CV_TITLE, d), svg(360, 400, CV_TITLE, m)


# =========================================================== hosted / de-hosted
HD_TITLE = ('Under hosted funding a commissioner pays for everyone its local clinics see: local residents '
            'and visitors. Under de-hosted funding it pays for its own residents, wherever they are seen.')
KEYS = [('A', 'Local residents, local clinics'), ('B', 'Local residents, clinics elsewhere'),
        ('C', 'Visitors, local clinics')]


def letter(x, y, s, active, fill):
    if active:
        return C(x, y, 12, fill) + T(x, y + 4.5, s, 12, WHITE, 'middle', 'bold')
    return C(x, y, 12, WHITE, MUTED, 1.25) + T(x, y + 4.5, s, 12, MUTED, 'middle', 'bold')


def hd_panel(ox, oy, hosted):
    col = NAVY if hosted else TEAL
    txt = NAVY if hosted else TEAL_D
    fill = NAVY if hosted else TEAL_D
    b = [f'<g transform="translate({ox},{oy})">',
         label(10, 16, 'Hosted funding' if hosted else 'De-hosted funding', txt, size=13),
         T(10, 37, 'Pays for everyone its local clinics see' if hosted
           else 'Pays for its own residents, wherever they are seen', 12.5, MUTED),
         T(14, 70, 'Elsewhere', 12, MUTED, italic=True),
         R(24.5, 82.5, 220, 166, None, col, 1.25, 4),
         T(40, 104, "Commissioner's area", 11.5, txt, weight='bold'),
         letter(56, 146, 'A', True, fill),
         P('M70 146 C94 140, 110 142, 124 145', col) + arrow(127, 145, 5, col),
         T(136, 151, 'Local clinics', 15, txt),
         L(136, 158, 226, 158, col, 1.25)]
    on, off = (col, MUTED)
    if hosted:
        b += [letter(300, 118, 'C', True, fill),
              P('M287 124 C268 132, 250 138, 236 144', col) + arrow(233, 145, 150, col),
              letter(56, 214, 'B', False, fill),
              P('M70 216 C150 236, 220 246, 260 246', off, 1.25, '4 3') + arrow(264, 246, 0, off, 1.25)]
        ct, cl = MUTED, MUTED
    else:
        b += [letter(300, 118, 'C', False, fill),
              P('M287 124 C268 132, 250 138, 236 144', off, 1.25, '4 3') + arrow(233, 145, 150, off, 1.25),
              letter(56, 214, 'B', True, fill),
              P('M70 216 C150 236, 220 246, 260 246', col) + arrow(264, 246, 0, col)]
        ct, cl = txt, col
    b += [T(272, 251, 'Clinic', 14, ct), T(272, 267, 'elsewhere', 12, ct, italic=True),
          L(272, 275, 336, 275, cl, 1),
          L(24, 290, 150, 290, col, 1.75),
          f'<text x="24" y="314" font-size="15" fill="{txt}">Pays for <tspan font-weight="bold">'
          f'{"A + C" if hosted else "A + B"}</tspan></text>', '</g>']
    return '\n'.join(b)


def hd_key(x, y, s, text):
    return C(x, y, 10, MUTED) + T(x, y + 4, s, 10.5, WHITE, 'middle', 'bold') + T(x + 17, y + 4.5, text, 12, NAVY)


def hosted_dehosted():
    d = [hd_panel(0, 0, True), hd_panel(366, 0, False), L(358, 6, 358, 318), L(10, 334, 710, 334)]
    for x, (s, t) in zip((22, 254, 508), KEYS):
        d.append(hd_key(x, 360, s, t))
    m = [hd_panel(4, 0, True), L(10, 336, 350, 336), hd_panel(4, 352, False), L(10, 688, 350, 688)]
    for i, (s, t) in enumerate(KEYS):
        m.append(hd_key(24, 714 + i * 26, s, t))
    return svg(720, 378, HD_TITLE, d), svg(360, 780, HD_TITLE, m)


# ============================================================== pathway to price
PP_TITLE = ('One pathway is a first contact and follow-up contacts, each made of steps. The direct cost of '
            'each step is staff time times cost per clinical minute, plus drugs, tests, consumables and '
            'pathology, added up across every step. Adding an allowance for indirect costs gives the cost '
            'per pathway.')
DIRECT = ['For each step: staff time × cost per clinical minute',
          '+ drugs, tests, consumables and pathology',
          'added up across every step of the pathway']
INDIRECT = ['Staff not facing patients', 'Provider overheads', 'Facilities and management']


def step(x, y, focal, size=12.5):
    if focal:
        return focus(x, y) + T(x, y + 26, 'Step', size, GOLD_T, 'middle', 'bold')
    return dot(x, y) + T(x, y + 26, 'Step', size, NAVY, 'middle')


def pathway_to_price():
    Y = 74
    d = [label(20, 14, 'One pathway'),
         T(124, 46, 'First contact', 15, NAVY, 'middle'),
         T(392, 46, 'Follow-up contacts', 15, NAVY, 'middle'),
         L(24, Y, 480, Y, NAVY, 1.75), L(486, Y, 528, Y, NAVY, 1.25, '4 4'),
         T(538, Y + 4, '… as the pathway requires', 12.5, MUTED, italic=True),
         L(258, Y - 10, 258, Y + 10, MUTED, 1)]
    for i, x in enumerate([50, 124, 198, 318, 392, 466]):
        d.append(step(x, Y, i == 2))
    d += [P(f'M184 {Y + 38} L22 150 M212 {Y + 38} L338 150', GOLD, 1.25, '4 4'),
          L(20, 150, 340, 150, GOLD, 1.75),
          T(20, 177, 'Direct cost', 17, NAVY, weight='bold')]
    d += [T(20, 201 + j * 19, s, 12, NAVY) for j, s in enumerate(DIRECT)]
    d += [L(20, 258, 340, 258), T(20, 280, '= direct cost of the pathway', 12.5, NAVY, weight='bold'),
          T(364, 226, '+', 26, MUTED, 'middle'),
          L(388, 150, 552, 150, TEAL, 1.75),
          T(388, 177, 'Indirect costs', 17, TEAL_D, weight='bold'),
          T(388, 199, 'an allowance for:', 12, MUTED, italic=True)]
    d += [T(388, 221 + j * 19, s, 12, NAVY) for j, s in enumerate(INDIRECT)]
    d += [T(576, 226, '=', 26, MUTED, 'middle'),
          L(600, 150, 710, 150, NAVY, 2.5),
          T(655, 205, 'Cost per', 20, NAVY, 'middle', 'bold'),
          T(655, 231, 'pathway', 20, NAVY, 'middle', 'bold')]

    Y = 70
    m = [label(12, 14, 'One pathway'),
         T(74, 44, 'First contact', 13.5, NAVY, 'middle'),
         T(246, 44, 'Follow-up contacts', 13.5, NAVY, 'middle'),
         L(12, Y, 318, Y, NAVY, 1.75), L(322, Y, 348, Y, NAVY, 1.25, '4 4'),
         L(160, Y - 9, 160, Y + 9, MUTED, 1)]
    for i, x in enumerate([24, 74, 124, 196, 246, 296]):
        m.append(step(x, Y, i == 2, 12))
    G = 180
    m += [T(348, Y + 46, '… as the pathway requires', 12, MUTED, 'end', italic=True),
          P(f'M114 {Y + 36} L12 {G} M134 {Y + 36} L348 {G}', GOLD, 1.25, '4 4'),
          L(12, G, 348, G, GOLD, 1.75),
          T(12, G + 27, 'Direct cost', 17, NAVY, weight='bold')]
    m += [T(12, G + 51 + j * 19, s, 12, NAVY) for j, s in enumerate(DIRECT)]
    m += [L(12, G + 107, 348, G + 107), T(12, G + 129, '= direct cost of the pathway', 12.5, NAVY, weight='bold'),
          T(180, G + 166, '+', 26, MUTED, 'middle'),
          L(12, G + 182, 348, G + 182, TEAL, 1.75),
          T(12, G + 209, 'Indirect costs', 17, TEAL_D, weight='bold'),
          T(12, G + 231, 'an allowance for:', 12, MUTED, italic=True)]
    m += [T(12, G + 253 + j * 19, s, 12, NAVY) for j, s in enumerate(INDIRECT)]
    m += [T(180, G + 330, '=', 26, MUTED, 'middle'),
          L(100, G + 348, 260, G + 348, NAVY, 2.5),
          T(180, G + 378, 'Cost per pathway', 20, NAVY, 'middle', 'bold')]
    return svg(720, 300, PP_TITLE, d), svg(360, G + 394, PP_TITLE, m)


# ======================================================= one visit, two prices
OV_TITLE = ('One visit, historical tariff prices: the LARC procedure is paid at its Primary price of £114.88 '
            'and SRH standard at its Additional price of £31.91, a total of £146.79, rather than £165.41 if '
            'both were paid at their Primary price. The £18.62 difference is shared care, not paid twice.')


def one_visit():
    k, X0 = 3.0, 10
    Lw, A, S, F = 114.88 * k, 31.91 * k, 18.62 * k, 50.53 * k
    d = [label(X0, 14, 'One visit: a change from the pill to a long-acting method'), L(X0, 26, 710, 26),
         T(X0, 60, 'Worked example, historical tariff prices', 16, NAVY, weight='bold')]
    y = 70
    d += [R(X0, y, Lw, 30, NAVY), T(X0 + 12, y + 20, 'LARC procedure · Primary £114.88', 12.5, WHITE),
          R(X0 + Lw, y, A, 30, TEAL_D),
          R(X0 + Lw + A + 0.75, y + 0.75, S - 1.5, 28.5, WHITE, GOLD, 1.5, 0, '3 3'),
          T(X0 + Lw + A + S / 2, y + 20, '£18.62', 11.5, GOLD_T, 'middle', 'bold'),
          T(X0 + Lw + A, y - 10, '£146.79', 20, NAVY, 'end', 'bold'),
          L(X0 + Lw + A, y - 6, X0 + Lw + A, y, NAVY, 1.5),
          L(X0 + Lw + A / 2, y + 30, X0 + Lw + A / 2, y + 38, TEAL_D, 1.25),
          T(X0 + Lw + A / 2, y + 52, 'SRH standard · Additional £31.91', 12, TEAL_D, 'middle')]
    y2 = 168
    gx = X0 + Lw + A
    d += [T(X0, y2 - 12, 'If both currencies were paid at their Primary price', 13, MUTED),
          R(X0 + 0.5, y2 + 0.5, Lw - 1, 29, PANEL, MUTED, 1),
          T(X0 + 12, y2 + 20, 'LARC procedure £114.88', 12.5, MUTED),
          R(X0 + Lw + 0.5, y2 + 0.5, F - 1, 29, WHITE, MUTED, 1, 0, '3 3'),
          T(X0 + Lw + 12, y2 + 20, 'SRH standard £50.53', 12.5, MUTED),
          T(X0 + Lw + F + 16, y2 + 21, '£165.41', 20, MUTED, weight='bold'),
          L(gx, y2 + 38, gx + S, y2 + 38, GOLD, 1.5),
          L(gx, y2 + 33, gx, y2 + 43, GOLD, 1.5), L(gx + S, y2 + 33, gx + S, y2 + 43, GOLD, 1.5),
          T(gx, y2 + 60, '£18.62 of shared care,', 12.5, GOLD_T, weight='bold'),
          T(gx, y2 + 77, 'not paid twice', 12.5, GOLD_T, weight='bold')]

    k, X0 = 1.9, 12
    Lw, A, S, F = 114.88 * k, 31.91 * k, 18.62 * k, 50.53 * k
    gx = X0 + Lw + A
    m = [label(X0, 14, 'One visit: a change from the pill'), label(X0, 31, 'to a long-acting method'),
         L(X0, 42, 348, 42), T(X0, 70, 'Worked example, historical tariff prices', 14, NAVY, weight='bold')]
    y = 100
    m += [T(gx, y - 8, '£146.79', 18, NAVY, 'end', 'bold'),
          R(X0, y, Lw, 26, NAVY), R(X0 + Lw, y, A, 26, TEAL_D),
          R(X0 + Lw + A + 0.75, y + 0.75, S - 1.5, 24.5, WHITE, GOLD, 1.5, 0, '3 3'),
          R(X0, y + 40, 11, 11, NAVY), T(X0 + 18, y + 50, 'LARC procedure · Primary £114.88', 12.5, NAVY),
          R(X0, y + 60, 11, 11, TEAL_D), T(X0 + 18, y + 70, 'SRH standard · Additional £31.91', 12.5, TEAL_D),
          R(X0 + 0.75, y + 80.75, 9.5, 9.5, WHITE, GOLD, 1.5, 0, '2 2'),
          T(X0 + 18, y + 90, '£18.62 of shared care, not paid twice', 12.5, GOLD_T, weight='bold')]
    y2 = y + 132
    by = y2 + 30
    m += [T(X0, y2, 'If both currencies were paid', 13, MUTED), T(X0, y2 + 17, 'at their Primary price', 13, MUTED),
          R(X0 + 0.5, by + 0.5, Lw - 1, 25, PANEL, MUTED, 1),
          R(X0 + Lw + 0.5, by + 0.5, F - 1, 25, WHITE, MUTED, 1, 0, '3 3'),
          L(gx, by + 34, gx + S, by + 34, GOLD, 1.5),
          L(gx, by + 29, gx, by + 39, GOLD, 1.5), L(gx + S, by + 29, gx + S, by + 39, GOLD, 1.5),
          R(X0 + 0.5, by + 50.5, 10, 10, PANEL, MUTED, 1), T(X0 + 18, by + 60, 'LARC procedure £114.88', 12.5, MUTED),
          R(X0 + 0.5, by + 70.5, 10, 10, WHITE, MUTED, 1, 0, '2 2'), T(X0 + 18, by + 80, 'SRH standard £50.53', 12.5, MUTED),
          T(X0, by + 106, 'Total at Primary prices', 12.5, MUTED),
          T(348, by + 107, '£165.41', 18, MUTED, 'end', 'bold')]
    return svg(720, 254, OV_TITLE, d), svg(360, by + 120, OV_TITLE, m)


# ================================================================= governance
GV_TITLE = ('Governance: the London Sexual Health Programme and its steering group oversaw four expert working '
            'groups: clinical, commissioning, data management and finance. Pathway Analytics provided '
            'methodology, modelling, analysis, coding and IT support for all four.')
GROUPS = [('Clinical', 'STI and contraception'), ('Commissioning', None), ('Data management', None), ('Finance', None)]
PA_ROLE = 'Methodology, modelling, analysis, coding and IT support for all four groups'


def governance():
    d = [T(360, 30, 'London Sexual Health Programme', 20, NAVY, 'middle', 'bold'),
         L(250, 44, 470, 44), L(360, 44, 360, 66, TEAL, 1.25), dot(360, 68, NAVY, 3),
         T(360, 94, 'Steering group', 17, NAVY, 'middle'),
         T(360, 114, 'Including HPA, BASHH, FSRH and the DH Payment by Results team', 12, MUTED, 'middle'),
         label(360, 146, 'Expert working groups', MUTED, 'middle')]
    xs = [90, 270, 450, 630]
    for x, (n, s) in zip(xs, GROUPS):
        d += [P(f'M360 156 C360 186, {x} 178, {x} 206', TEAL, 1.5), dot(x, 211, TEAL, 5),
              T(x, 238, n, 16, NAVY, 'middle')]
        if s:
            d.append(T(x, 256, s, 11.5, MUTED, 'middle'))
        d.append(L(x, 266, x, 290, NAVY, 1.25))
    d += [L(50, 290, 670, 290, NAVY, 1.75),
          T(360, 319, 'Pathway Analytics', 17, NAVY, 'middle', 'bold'),
          T(360, 340, PA_ROLE, 12, MUTED, 'middle')]

    m = [T(180, 26, 'London Sexual Health Programme', 16, NAVY, 'middle', 'bold'),
         L(90, 38, 270, 38), L(180, 38, 180, 56, TEAL, 1.25), dot(180, 58, NAVY, 3),
         T(180, 84, 'Steering group', 16, NAVY, 'middle'),
         T(180, 104, 'Including HPA, BASHH, FSRH and', 12, MUTED, 'middle'),
         T(180, 120, 'the DH Payment by Results team', 12, MUTED, 'middle'),
         L(180, 130, 180, 150, TEAL, 1.25),
         label(196, 146, 'Expert working groups'),
         P('M180 150 C180 160, 32 156, 32 170', TEAL, 1.5), L(32, 170, 32, 338, TEAL, 1.5)]
    for y, (n, s) in zip([184, 234, 270, 306], GROUPS):
        m += [dot(32, y, TEAL, 5), T(52, y + 5, n, 16, NAVY)]
        if s:
            m.append(T(52, y + 23, s, 11.5, MUTED))
    m += [L(20, 338, 340, 338, NAVY, 1.75),
          T(180, 367, 'Pathway Analytics', 16, NAVY, 'middle', 'bold'),
          T(180, 387, 'Methodology, modelling, analysis, coding', 12, MUTED, 'middle'),
          T(180, 403, 'and IT support for all four groups', 12, MUTED, 'middle')]
    return svg(720, 352, GV_TITLE, d), svg(360, 416, GV_TITLE, m)


# ============================================================ care to charging
CC_TITLE = ('Four steps from care to charging. The provider delivers and records care as usual and codes it '
            'in two returns, GUMCAD and SRHAD, plus a few local codes. The Tariff Grouper joins the two '
            'datasets into visits, matches them to currencies and prices, and allocates each charge to the '
            'council that pays.')
PROV_NOTES = ['No change to how clinicians deliver care;', 'no direct patient identifiers leave the provider']
GROUPER_NOTES = ['Joins the two datasets into visits', 'Removes double counting',
                 'Primary price first, Additional for the rest', 'Applies MFF or geographical weighting']


def care_to_charging():
    Y = 96
    U, D = Y - 12, Y + 12
    xs = [90, 270, 450, 630]
    d = [label(180, 16, 'Provider', NAVY, 'middle', 13), label(540, 16, 'Tariff Grouper', GOLD_T, 'middle', 13),
         L(20, 28, 340, 28), L(380, 28, 700, 28), L(360, 40, 360, 274, MUTED, 1, '3 4'),
         L(20, Y, 176, Y, NAVY, 1.75),
         P(f'M176 {Y} L194 {U} L414 {U} L436 {Y}', NAVY),
         P(f'M176 {Y} L194 {D} L414 {D} L436 {Y}', TEAL),
         L(436, Y, 700, Y, GOLD, 1.75), arrow(703, Y, 0, GOLD),
         T(229, U - 7, 'GUMCAD', 10.5, NAVY, 'middle', 'bold'),
         T(229, D + 16, 'SRHAD', 10.5, TEAL_D, 'middle', 'bold'),
         dot(xs[0], Y, NAVY, 5), dot(xs[1], U, NAVY), dot(xs[1], D, TEAL),
         dot(xs[2], Y, GOLD, 5), dot(xs[3], Y, GOLD, 5)]
    steps = [('Care activity', ['Care delivered and', 'recorded as usual']),
             ('Coding', ['GUMCAD and SRHAD,', 'plus a few local codes']),
             ('Grouping', ['Visits matched to', 'currencies and prices']),
             ('Charging', ['Charges allocated to', 'the council that pays'])]
    for x, (n, ls) in zip(xs, steps):
        d.append(T(x, 148, n, 17, NAVY, 'middle', 'bold'))
        d += [T(x, 167 + j * 16, s, 11.5, MUTED, 'middle') for j, s in enumerate(ls)]
    d += [L(20, 200, 340, 200), L(380, 200, 700, 200)]
    d += [T(20, 223 + j * 18, s, 12, NAVY) for j, s in enumerate(PROV_NOTES)]
    d += [T(380, 223 + j * 18, s, 12, NAVY) for j, s in enumerate(GROUPER_NOTES)]

    X = 22
    m = [label(12, 16, 'Provider', NAVY, 'start', 13),
         L(X, 36, X, 92, NAVY, 1.75),
         P(f'M{X} 92 L{X - 6} 100 L{X - 6} 124 L{X} 132', NAVY),
         P(f'M{X} 92 L{X + 6} 100 L{X + 6} 124 L{X} 132', TEAL),
         L(X, 132, X, 196, NAVY, 1.75),
         dot(X, 44, NAVY, 5), T(44, 50, 'Care activity', 16, NAVY, weight='bold'),
         T(44, 70, 'Care delivered and recorded as usual', 12, MUTED),
         dot(X - 6, 112, NAVY, 3.5), dot(X + 6, 112, TEAL, 3.5),
         T(44, 118, 'Coding', 16, NAVY, weight='bold'),
         f'<text x="44" y="138" font-size="12" fill="{MUTED}"><tspan font-weight="bold" fill="{NAVY}">GUMCAD</tspan>'
         f' and <tspan font-weight="bold" fill="{TEAL_D}">SRHAD</tspan>, plus a few local codes</text>']
    m += [T(44, 170 + j * 17, s, 12, NAVY) for j, s in enumerate(PROV_NOTES)]
    m += [L(12, 222, 348, 222, MUTED, 1, '3 4'),
          label(12, 246, 'Tariff Grouper', GOLD_T, 'start', 13),
          L(X, 258, X, 352, GOLD, 1.75), arrow(X, 356, 90, GOLD),
          dot(X, 270, GOLD, 5), T(44, 276, 'Grouping', 16, NAVY, weight='bold'),
          T(44, 296, 'Visits matched to currencies and prices', 12, MUTED),
          dot(X, 326, GOLD, 5), T(44, 332, 'Charging', 16, NAVY, weight='bold'),
          T(44, 352, 'Charges allocated to the council that pays', 12, MUTED)]
    m += [T(44, 382 + j * 18, s, 12, NAVY) for j, s in enumerate(GROUPER_NOTES)]
    return svg(720, 284, CC_TITLE, d), svg(360, 450, CC_TITLE, m)


# =================================================================== timeline
TL_TITLE = ('Timeline: design in London 2009 to 2010; implementation and regional road tests 2011 to 2013; '
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


def timeline():
    # A straight line: the stages are in order, but the graphic measures nothing.
    Y = 150
    d = [L(14, Y, 700, Y, NAVY, 1.75), arrow(706, Y, 0, NAVY)]
    for i, (x, (date, name, ls)) in enumerate(zip([78, 218, 358, 498, 632], STAGES)):
        last = i == 4
        d.append(focus(x, Y) if last else dot(x, Y, TEAL, 5))
        nt = GOLD_T if last else TEAL_D
        if i in (1, 3):                      # labels above the line
            base = Y - 24
            d.append(L(x, Y - 9, x, base + 6, LINE, 1))
            yy = base
            for s in reversed(ls):
                d.append(T(x, yy, s, 11.5, MUTED, 'middle'))
                yy -= 15
            d += [T(x, yy - 3, name, 12, nt, 'middle', 'bold'), T(x, yy - 21, date, 15, NAVY, 'middle', 'bold')]
        else:                                # labels below the line
            d.append(L(x, Y + 9, x, Y + 16, LINE, 1))
            d += [T(x, Y + 36, date, 15, NAVY, 'middle', 'bold'), T(x, Y + 54, name, 12, nt, 'middle', 'bold')]
            for j, s in enumerate(ls):
                strong = last and j == 0
                d.append(T(x, Y + 73 + j * 15, s, 11.5, NAVY if strong else MUTED, 'middle', 'bold' if strong else None))

    m, y, dots = [], 6, []
    for i, (date, name, _) in enumerate(STAGES):
        last = i == 4
        dots.append((y + 12, last))
        m += [T(36, y + 18, date, 16, NAVY, weight='bold'),
              T(36, y + 37, name, 12, GOLD_T if last else TEAL_D, weight='bold')]
        for j, s in enumerate(PHONE_STAGES[i]):
            strong = last and j == 0
            m.append(T(36, y + 57 + j * 18, s, 12.5, NAVY if strong else MUTED, weight='bold' if strong else None))
        y += 57 + 18 * (len(PHONE_STAGES[i]) - 1) + 30
    H = y
    m = [L(14, 12, 14, H - 16, NAVY, 1.75), arrow(14, H - 10, 90, NAVY)] + \
        [focus(14, cy) if last else dot(14, cy, TEAL, 5) for cy, last in dots] + m
    return svg(720, 280, TL_TITLE, d), svg(360, H, TL_TITLE, m)


GRAPHICS = [
    (DICT, 'convergence', convergence),
    (CASE, 'tariff-hosted-dehosted', hosted_dehosted),
    (CASE, 'tariff-pathway-to-price', pathway_to_price),
    (CASE, 'tariff-one-visit-two-prices', one_visit),
    (CASE, 'tariff-governance', governance),
    (CASE, 'tariff-care-to-payment', care_to_charging),
    (CASE, 'tariff-timeline', timeline),
]


def main():
    for folder, name, fn in GRAPHICS:
        os.makedirs(folder, exist_ok=True)
        wide, narrow = fn()
        for suffix, s in (('', wide), ('-mobile', narrow)):
            with open(os.path.join(folder, f'{name}{suffix}.svg'), 'w', encoding='utf-8') as f:
                f.write(s)
    print('Wrote', len(GRAPHICS) * 2, 'SVG files')


if __name__ == '__main__':
    main()

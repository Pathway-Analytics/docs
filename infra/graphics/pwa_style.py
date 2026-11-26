#!/usr/bin/env python3
"""Shared drawing rules for PWA website graphics (Design System v1.2).

Every graphic set in infra/graphics/sets/ imports from here, so all graphics
share one set of colours, one font and one set of shapes. Do not change the
values here for a single graphic; changes here change every graphic.

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
- v1.2: no label smaller than 13px as rendered. For sets marked
  DESIGN_SYSTEM = '1.2', svg() raises any smaller font size to
  MIN_LABEL_DESKTOP or MIN_LABEL_PHONE (see below), so a label that has
  grown may need moving: check every graphic after drawing it.
- v1.2: keep text in a graphic to labels. Titles, explanations and sources
  go in the page, in the figure heading, caption and source note.

Each graphic has a desktop version (720 wide) and a phone version (360 wide,
file name ending -mobile). Draw them with infra/graphics/pwa_graphics.py.
"""
import math, os, re

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

# ---- v1.2 label floors, in drawing units --------------------------------------
# Desktop graphics are 720 wide and are shown in the 800px editorial column
# (x1.11); phone graphics are 360 wide and are shown about 358px wide on a
# 390px phone (x0.99). These floors keep every label at 13px or more as
# rendered, the v1.2 minimum. Do not lower them for a single graphic.
MIN_LABEL_DESKTOP = 12
MIN_LABEL_PHONE = 13
LABEL_FLOORS = True   # pwa_graphics.py turns this off for sets still drawn to v1.0


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


def _floor_labels(markup, floor):
    return re.sub(r'font-size="([0-9.]+)"',
                  lambda m: f'font-size="{max(float(m.group(1)), floor):g}"', markup)


def svg(w, h, title, body):
    if LABEL_FLOORS:
        body = [_floor_labels(b, MIN_LABEL_PHONE if w <= 400 else MIN_LABEL_DESKTOP) for b in body]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{esc(title)}" font-family="{FONT}">\n'
            f'<title>{esc(title)}</title>\n'
            f'<rect width="{w}" height="{h}" fill="{WHITE}"/>\n' + '\n'.join(body) + '\n</svg>\n')




def write_pair(folder, name, wide, narrow):
    """Write a graphic's desktop and phone SVG files."""
    os.makedirs(folder, exist_ok=True)
    for suffix, s in (('', wide), ('-mobile', narrow)):
        with open(os.path.join(folder, f'{name}{suffix}.svg'), 'w', encoding='utf-8') as f:
            f.write(s)

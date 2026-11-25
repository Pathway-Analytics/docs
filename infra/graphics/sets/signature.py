"""Signature graphic: three disciplines converging on the patient.

Used for sharing images and other formats; the home page draws its own
version in the page."""
from pwa_style import *  # noqa: F401,F403  colours, font and drawing helpers

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


GRAPHICS = [
    (DICT, 'convergence', convergence),
]

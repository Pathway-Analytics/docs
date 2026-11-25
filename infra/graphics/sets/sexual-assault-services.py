"""Sexual assault services case study graphics (case-studies/sexual-assault-services.md)."""
from pwa_style import *  # noqa: F401,F403  colours, font and drawing helpers

# Levels of need are ordered, so they use the sequential chart colours from the
# design system guide (style-guide/README.md, "Charts"; tokens --pa-seq-1 to 5),
# lightest for the lowest level. Steps 1, 3, 4 and 5 keep text readable on every
# fill: dark text on the lightest, white on the rest.
SEQ = ['#8fabcf', '#6189bb', '#3e6aa0', '#25497c', '#14335a']
LEVELS = [('Ongoing', SEQ[0], NAVY), ('Vulnerable', SEQ[2], WHITE),
          ('Complex', SEQ[3], WHITE), ('Acute', SEQ[4], WHITE)]
LV = {name[0]: (name, fill, ink) for name, fill, ink in LEVELS}

STEPS = ['Initial contact', 'Risk assessment', 'Forensic examination', 'Verbal evidence',
         'Needs assessment', 'Follow-up support', 'Counselling', 'Court support', 'Later counselling']
STEPS_2 = [('Initial', 'contact'), ('Risk', 'assessment'), ('Forensic', 'examination'),
           ('Verbal', 'evidence'), ('Needs', 'assessment'), ('Follow-up', 'support'),
           ('Counselling', None), ('Court', 'support'), ('Later', 'counselling')]
# Level at each of the nine steps; N = step not needed.
VICTIMS = [('Adult', '18 and over', 'AAAACCVVO'),
           ('Adolescent', '13 to 17', 'VVNNVNVNO'),
           ('Child', '12 and under', 'AAAAAAAAA')]


def runs(seq):
    """Group a level sequence into (level, first step, last step) runs."""
    out, i = [], 0
    while i < len(seq):
        j = i
        while j + 1 < len(seq) and seq[j + 1] == seq[i] and seq[i] != 'N':
            j += 1
        out.append((seq[i], i, j))
        i = j + 1
    return out


def chevron(x, y, w, h, first, fill=None, stroke=None, dash=None):
    n = 0 if first else 7
    pts = f'{x:g},{y:g} {x + w - 7:g},{y:g} {x + w:g},{y + h / 2:g} {x + w - 7:g},{y + h:g} {x:g},{y + h:g} {x + n:g},{y + h / 2:g}'
    s = f' stroke="{stroke}" stroke-width="1"' if stroke else ''
    s += f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{pts}" fill="{fill or WHITE}"{s}/>'


def key(x, y, k):
    if k == 'N':
        return R(x + 0.5, y + 0.5, 12, 12, WHITE, MUTED, 1, 0, '3 2') + T(x + 19, y + 11, 'Step not needed', 12, MUTED)
    name, fill, _ = LV[k]
    return R(x, y, 13, 13, fill) + T(x + 19, y + 11, name, 12, NAVY)


# ============================================================ need over time
NT_TITLE = ("Three illustrative victims and their level of need at each of nine steps, from initial contact "
            "to later counselling. An adult is acute from initial contact to verbal evidence, complex for "
            "needs assessment and follow-up support, vulnerable for counselling and court support, and "
            "ongoing for later counselling. An adolescent is vulnerable at initial contact, risk assessment, "
            "needs assessment and counselling, does not need the other steps, and is ongoing for later "
            "counselling. A child is acute at every step.")


def need_over_time():
    X0, W, G = 104, 66, 1.5            # first chevron, chevron width, gap
    xs = [X0 + i * (W + G) for i in range(9)]
    d = [label(10, 16, 'Level of need at each step')]
    for x, (a, b) in zip(xs, STEPS_2):
        cx = x + W / 2
        if b:
            d += [T(cx, 38, a, 11, NAVY, 'middle'), T(cx, 51, b, 11, NAVY, 'middle')]
        else:
            d.append(T(cx, 45, a, 11, NAVY, 'middle'))
    d.append(L(10, 62, 710, 62))
    y0 = 76
    for r, (name, sub, seq) in enumerate(VICTIMS):
        y = y0 + r * 84
        d += [T(10, y + 13, name, 14, NAVY, weight='bold'), T(10, y + 30, sub, 12, MUTED)]
        for i, k in enumerate(seq):
            if k == 'N':
                d.append(chevron(xs[i] + 0.5, y + 0.5, W - 1, 25, i == 0, WHITE, MUTED, '3 2.5'))
            else:
                d.append(chevron(xs[i], y, W, 26, i == 0, LV[k][1]))
        for k, a, b in runs(seq):
            if k == 'N':
                continue
            x1, x2 = xs[a] + 4, xs[b] + W - 6
            by = y + 38
            d += [L(x1, by, x2, by, MUTED, 1), L(x1, by - 4, x1, by + 4, MUTED, 1), L(x2, by - 4, x2, by + 4, MUTED, 1),
                  T((x1 + x2) / 2, by + 18, LV[k][0], 12, NAVY, 'middle', 'bold')]
        if r < 2:
            d.append(L(10, y + 72, 710, y + 72))
    ky = y0 + 2 * 84 + 72
    d.append(L(10, ky, 710, ky))
    d.append(T(10, ky + 25, 'Level of need, lowest to highest:', 12, MUTED))
    for x, k in zip((206, 302, 404, 499), 'OVCA'):
        d.append(key(x, ky + 14, k))
    d.append(key(576, ky + 14, 'N'))

    # Phone: steps down the side, one column per victim
    CX, CW = [154, 222, 290], 64
    m = [label(12, 16, 'Level of need at each step')]
    for x, (name, sub, _) in zip(CX, VICTIMS):
        m += [T(x + CW / 2, 44, name, 12, NAVY, 'middle', 'bold'), T(x + CW / 2, 59, sub, 10.5, MUTED, 'middle')]
    m.append(L(12, 68, 354, 68))
    Y0, RH = 78, 30
    for i, s in enumerate(STEPS):
        m.append(T(12, Y0 + RH * i + 18, s, 11.5, NAVY))
    for x, (_, _, seq) in zip(CX, VICTIMS):
        for k, a, b in runs(seq):
            y, h = Y0 + RH * a, RH * (b - a + 1) - 2
            if k == 'N':
                m.append(R(x + 0.5, y + 0.5, CW - 1, h - 1, WHITE, MUTED, 1, 0, '3 2.5'))
            else:
                name, fill, ink = LV[k]
                m += [R(x, y, CW, h, fill), T(x + CW / 2, y + h / 2 + 4, name, 10.5, ink, 'middle', 'bold')]
    ky = Y0 + RH * 9 + 8
    m += [L(12, ky, 354, ky), T(12, ky + 24, 'Level of need, lowest to highest:', 12, MUTED)]
    for (x, y), k in zip(((12, ky + 36), (110, ky + 36), (214, ky + 36), (12, ky + 60)), 'OVCA'):
        m.append(key(x, y, k))
    m.append(key(110, ky + 60, 'N'))
    return svg(720, ky + 36, NT_TITLE, d), svg(360, ky + 82, NT_TITLE, m)


# ================================================== national budgetary assessment
FS_TITLE = ("The national budgetary assessment in four steps: national surveys of commissioners, SARC managers "
            "and voluntary organisations in August and September 2014; pathway workshops in October 2014 that "
            "mapped 72 good-practice pathways; agreement in November 2014 on 29 core pathways; and a funding "
            "model in December 2014 and January 2015 sharing the modelled cost between six public bodies.")
FOUR = [('Aug to Sep 2014', 'National survey', ['Commissioners, SARC managers', 'and voluntary organisations'],
         '3', ['national surveys: funding,', 'activity, case mix, staffing', 'and costs']),
        ('Oct 2014', 'Pathway workshops', ['100+ stakeholders, six areas', 'of England, 30+ hours'],
         '72', ['good-practice pathways', 'mapped']),
        ('Nov 2014', 'Agree good practice', ['Four criteria: victim experience,', 'justice and health outcomes,',
                                             'value for money'],
         '29', ['core pathways agreed by a', 'national governance group']),
        ('Dec 2014 to Jan 2015', 'Funding model', ['Each step costed and allocated', 'to the body responsible for',
                                                     'the need it meets'],
         '6', ['public bodies share the', 'modelled cost'])]


def four_steps():
    Y = 46
    xs = [10, 190, 370, 550]
    d = [L(10, Y, 700, Y, NAVY, 1.75), arrow(706, Y, 0, NAVY)]
    for i, (x, (date, name, desc, num, numl)) in enumerate(zip(xs, FOUR)):
        last = i == 3
        d.append(focus(x + 6, Y) if last else dot(x + 6, Y, TEAL, 5))
        d += [T(x, 26, date, 12, GOLD_T if last else TEAL_D, weight='bold'),
              T(x, 82, name, 16, NAVY, weight='bold')]
        d += [T(x, 104 + j * 16, s, 11.5, MUTED) for j, s in enumerate(desc)]
        d += [L(x, 162, x + 160, 162), T(x, 196, num, 28, NAVY, weight='bold')]
        d += [T(x, 218 + j * 16, s, 11.5, NAVY) for j, s in enumerate(numl)]

    m, y, dots = [], 8, []
    for i, (date, name, desc, num, numl) in enumerate(FOUR):
        last = i == 3
        dots.append((y + 10, last))
        m += [T(36, y + 15, date, 12, GOLD_T if last else TEAL_D, weight='bold'),
              T(36, y + 36, name, 16, NAVY, weight='bold')]
        m += [T(36, y + 56 + j * 17, s, 12, MUTED) for j, s in enumerate(desc)]
        ny = y + 56 + 17 * len(desc) + 14
        m += [T(36, ny + 10, num, 24, NAVY, weight='bold')]
        m += [T(36 + 14 * len(num) + 16, ny + j * 16 + (2 if len(numl) == 2 else -6), s, 12, NAVY)
              for j, s in enumerate(numl)]
        y = ny + 44
    H = y
    m = [L(14, 12, 14, H - 22, NAVY, 1.75), arrow(14, H - 16, 90, NAVY)] + \
        [focus(14, cy) if last else dot(14, cy, TEAL, 5) for cy, last in dots] + m
    return svg(720, 272, FS_TITLE, d), svg(360, H, FS_TITLE, m)


# ================================================================== who pays
WP_TITLE = ("Each step of the pathway, from initial contact to court support, is costed and multiplied by the "
            "number of victims who use it. The steps add up to the total cost of the pathways, which is split "
            "step by step between NHS England, clinical commissioning groups, local authorities, the police, "
            "Police and Crime Commissioners and the Ministry of Justice. A proposed allocation, not an agreed "
            "settlement.")
WP_STEPS = [('Initial', 'contact'), ('Risk', 'assessment'), ('Forensic', 'examination'), ('Verbal', 'evidence'),
            ('Needs', 'assessment'), ('Follow-up', 'support'), ('Counselling', None), ('Court', 'support')]
BODIES = [('NHS England', None), ('Clinical', 'commissioning groups'), ('Local', 'authorities'),
          ('Police', None), ('Police and Crime', 'Commissioners'), ('Ministry', 'of Justice')]


def who_pays():
    # Desktop: two brackets. One adds up the steps into the total (the gold dot);
    # one splits the total between the six bodies.
    Y = 80
    xs = [52 + i * 88 for i in range(8)]          # centred on 360
    d = [label(10, 16, 'Victims who reach the services'), L(10, 26, 710, 26),
         L(10, Y, 710, Y, NAVY, 1.75)]
    for x, (a, b) in zip(xs, WP_STEPS):
        d.append(dot(x, Y))
        if b:
            d += [T(x, Y - 27, a, 11.5, NAVY, 'middle'), T(x, Y - 13, b, 11.5, NAVY, 'middle')]
        else:
            d.append(T(x, Y - 13, a, 11.5, NAVY, 'middle'))
        d += [T(x, Y + 24, '£ × victims', 11.5, MUTED, 'middle'), L(x, Y + 34, x, Y + 44, MUTED, 1)]
    BY = Y + 44
    TY = BY + 34
    d += [L(xs[0], BY, xs[-1], BY, MUTED, 1), L(360, BY, 360, TY - 7, MUTED, 1),
          focus(360, TY), T(360, TY + 29, 'Total cost of the pathways', 16, NAVY, 'middle', 'bold')]
    SY = TY + 76
    bx = [70 + i * 116 for i in range(6)]         # centred on 360
    d += [L(360, TY + 40, 360, SY, NAVY, 1.5),
          label(372, TY + 62, 'Split step by step between six public bodies'),
          L(bx[0], SY, bx[-1], SY, NAVY, 1.5)]
    for x, (a, b) in zip(bx, BODIES):
        d += [L(x, SY, x, SY + 18, NAVY, 1.5), dot(x, SY + 22, NAVY, 4.5), T(x, SY + 44, a, 12.5, NAVY, 'middle')]
        if b:
            d.append(T(x, SY + 60, b, 12.5, NAVY, 'middle'))
    H = SY + 74

    X = 22
    m = [label(12, 16, 'Victims who reach the services')]
    y = 44
    for a, b in WP_STEPS:
        m += [dot(X, y), T(40, y + 4.5, f'{a} {b}' if b else a, 12.5, NAVY),
              T(348, y + 4.5, '£ × victims', 11.5, MUTED, 'end')]
        y += 28
    m = [L(X, 44, X, y - 28, NAVY, 1.75)] + m
    m += [L(X, y - 28, X, y + 6, TEAL, 1.25), focus(X, y + 12),
          T(40, y + 17, 'Total cost of the pathways', 15, NAVY, weight='bold'),
          L(X, y + 20, X, y + 46, NAVY, 1.25),
          label(40, y + 44, 'Split step by step between six public bodies', size=11.5)]
    y += 70
    for i, (a, b) in enumerate(BODIES):
        m += [dot(X, y), T(40, y + 4.5, f'{a} {b}' if b else a, 12.5, NAVY)]
        if i < len(BODIES) - 1:
            m.append(L(X, y + 6, X, y + 22, NAVY, 1.25))
        y += 28
    return svg(720, H, WP_TITLE, d), svg(360, y - 6, WP_TITLE, m)


# =========================================================== cost by need (matrix)
CN_TITLE = ("Costing a client pathway: each component is costed at four levels of need, from ongoing to acute, "
            "with relative costs rising from one to four pound signs. Ongoing clients need no verbal evidence "
            "or forensic examination. Choosing a level, here vulnerable, gives the cost of one client's pathway "
            "at that level.")
COMPONENTS = ['Initial contact', 'Risk assessment', 'Verbal evidence', 'Forensic examination', 'Needs assessment']
NOT_NEEDED = {(2, 0), (3, 0)}          # (component, level): ongoing clients
CHOSEN = 1                             # vulnerable


def cost_by_need():
    cx = [325, 435, 545, 655]
    top, RH = 70, 36
    bottom = top + RH * len(COMPONENTS)
    d = [R(cx[CHOSEN] - 55, 34, 110, bottom - 34, PANEL),
         focus(cx[CHOSEN] - 40, 20), T(cx[CHOSEN] - 28, 24.5, 'Level chosen', 12, GOLD_T, weight='bold'),
         label(10, 52, 'Level of need')]
    for x, (name, fill, _) in zip(cx, LEVELS):
        d += [T(x, 52, name, 13, NAVY, 'middle', 'bold'), R(x - 40, 58, 80, 5, fill)]
    for r, comp in enumerate(COMPONENTS):
        y = top + RH * r
        d += [L(10, y, 710, y), T(10, y + 23, comp, 13.5, NAVY)]
        for c, x in enumerate(cx):
            if (r, c) in NOT_NEEDED:
                d.append(T(x, y + 22, 'Not needed', 11.5, MUTED, 'middle', italic=True))
            else:
                d.append(T(x, y + 23, '£' * (c + 1), 15, NAVY, 'middle', 'bold' if c == CHOSEN else None))
    d += [L(10, bottom, 710, bottom),
          L(cx[CHOSEN], bottom, cx[CHOSEN], bottom + 26, GOLD, 1.75), arrow(cx[CHOSEN], bottom + 30, 90, GOLD),
          T(cx[CHOSEN], bottom + 54, "Cost of one client's pathway at this level", 15, NAVY, 'middle', 'bold'),
          T(10, bottom + 86, 'Higher need adds staff time, specialist input such as interpreters, and sometimes extra steps',
            12, MUTED)]

    mx = [163, 217, 271, 325]
    top, RH = 74, 40
    bottom = top + RH * len(COMPONENTS)
    m = [R(mx[CHOSEN] - 27, 30, 54, bottom - 30, PANEL),
         focus(mx[CHOSEN] - 16, 16), T(mx[CHOSEN] - 5, 20.5, 'Level chosen', 11.5, GOLD_T, weight='bold'),
         label(12, 56, 'Level of need', size=11)]
    for x, (name, fill, _) in zip(mx, LEVELS):
        m += [T(x, 56, name, 10, NAVY, 'middle', 'bold'), R(x - 22, 62, 44, 4, fill)]
    for r, comp in enumerate(COMPONENTS):
        y = top + RH * r
        m.append(L(12, y, 352, y))
        words = comp.split(' ')
        if len(words) == 2 and len(comp) > 17:
            m += [T(12, y + 17, words[0], 12.5, NAVY), T(12, y + 32, words[1], 12.5, NAVY)]
        else:
            m.append(T(12, y + 25, comp, 12.5, NAVY))
        for c, x in enumerate(mx):
            if (r, c) in NOT_NEEDED:
                m += [T(x, y + 18, 'Not', 10, MUTED, 'middle', italic=True),
                      T(x, y + 30, 'needed', 10, MUTED, 'middle', italic=True)]
            else:
                m.append(T(x, y + 25, '£' * (c + 1), 13, NAVY, 'middle', 'bold' if c == CHOSEN else None))
    m += [L(12, bottom, 352, bottom),
          L(mx[CHOSEN], bottom, mx[CHOSEN], bottom + 22, GOLD, 1.75), arrow(mx[CHOSEN], bottom + 26, 90, GOLD),
          T(12, bottom + 50, "Cost of one client's pathway", 14, NAVY, weight='bold'),
          T(12, bottom + 68, 'at this level', 14, NAVY, weight='bold'),
          T(12, bottom + 98, 'Higher need adds staff time, specialist input', 12, MUTED),
          T(12, bottom + 115, 'such as interpreters, and sometimes extra steps', 12, MUTED)]
    return svg(720, 70 + 36 * 5 + 100, CN_TITLE, d), svg(360, bottom + 128, CN_TITLE, m)


# ============================================================ three approaches
TA_TITLE = ("Three ways of sharing the same cost: current funding, based on 2014/15 survey returns, shows "
            "historical contracts, grants and budgets; policy-based allocation, based on statutory "
            "responsibilities and national policy, shows responsibilities as written; pathway-based allocation, "
            "based on each step of the 29 core pathways, shows funding that follows the victim's need. The three "
            "gave very different splits between the funding bodies.")
APPROACHES = [('Current funding', 'Who pays now?',
               ['Survey returns from commissioners,', 'SARCs and voluntary organisations,', '2014/15'],
               ['Historical contracts, grants', 'and budgets']),
              ('Policy-based allocation', 'Who should pay, by policy?',
               ['Statutory responsibilities and', 'national policy, applied to the', 'total cost'],
               ['Responsibilities as written']),
              ('Pathway-based allocation', 'Who should pay, by need?',
               ['Each step of the 29 core pathways,', 'allocated to the body responsible', 'for the need it meets'],
               ["Funding that follows the", "victim's need"])]
CONCLUSION = 'Side by side, the three gave very different splits between the funding bodies'


def approach(x, y, a, last, w, size=12):
    name, q, based, shows = a
    b = [L(x, y, x + w, y, NAVY, 1.75)]
    if last:
        b.append(focus(x + w - 8, y))
    b += [T(x, y + 28, name, 16, NAVY, weight='bold'), T(x, y + 48, q, 12.5, MUTED, italic=True),
          label(x, y + 80, 'Based on', size=11.5)]
    b += [T(x, y + 99 + j * 17, s, size, NAVY) for j, s in enumerate(based)]
    yy = y + 99 + 17 * len(based) + 16
    b += [label(x, yy, 'Shows', size=11.5)]
    b += [T(x, yy + 19 + j * 17, s, size, NAVY, weight='bold') for j, s in enumerate(shows)]
    return b, yy + 19 + 17 * len(shows)


def three_approaches():
    d = []
    for i, (x, a) in enumerate(zip((10, 250, 490), APPROACHES)):
        b, _ = approach(x, 14, a, i == 2, 220)
        d += b
    d += [L(10, 250, 710, 250), T(360, 276, CONCLUSION, 14, NAVY, 'middle', 'bold')]

    m, y = [], 14
    for i, a in enumerate(APPROACHES):
        b, y = approach(12, y, a, i == 2, 336, 12.5)
        m += b
        y += 30
    m += [L(12, y - 6, 348, y - 6), T(12, y + 18, 'Side by side, the three gave very', 14, NAVY, weight='bold'),
          T(12, y + 36, 'different splits between the funding bodies', 14, NAVY, weight='bold')]
    return svg(720, 294, TA_TITLE, d), svg(360, y + 50, TA_TITLE, m)


GRAPHICS = [
    (CASE, 'sas-needs-over-time', need_over_time),
    (CASE, 'sas-four-steps', four_steps),
    (CASE, 'sas-who-pays', who_pays),
    (CASE, 'sas-cost-by-need', cost_by_need),
    (CASE, 'sas-three-approaches', three_approaches),
]

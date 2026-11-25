#!/usr/bin/env python3
"""Draw PWA website graphics to the Design System v1.0 rules.

Each case study (or other page) has its own set in infra/graphics/sets/, so
case studies can be drawn and published independently. Shared colours, font
and shapes are in infra/graphics/pwa_style.py.

Run from the repository root:
    python3 infra/graphics/pwa_graphics.py            # every set
    python3 infra/graphics/pwa_graphics.py tariff     # one set

A set is a .py file in sets/ with a GRAPHICS list of
(folder, file name, function) entries; each function returns
(desktop_svg, phone_svg). Start a new set by copying an existing one.
"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pwa_style import write_pair  # noqa: E402


def load(name):
    spec = importlib.util.spec_from_file_location(f'sets.{name}', os.path.join(HERE, 'sets', f'{name}.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(names):
    available = sorted(f[:-3] for f in os.listdir(os.path.join(HERE, 'sets')) if f.endswith('.py') and not f.startswith('_'))
    for n in names or available:
        if n not in available:
            raise SystemExit(f'No graphics set called {n!r}. Sets: {", ".join(available)}')
        count = 0
        for folder, file_name, fn in load(n).GRAPHICS:
            write_pair(folder, file_name, *fn())
            count += 1
        print(f'{n}: wrote {count * 2} SVG files')


if __name__ == '__main__':
    main(sys.argv[1:])

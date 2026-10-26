#!/usr/bin/env python3
"""Wrap the editable fragment as a self-contained browser page."""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "prototype" / "crew-org-chart.html"
    target = root / "index.html"
    header = (
        '<!doctype html>\n'
        '<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="color-scheme" content="light dark">'
        '<title>Paul OS · The Crew</title>'
        '<style>html{color-scheme:light dark}'
        'body{margin:0;padding:16px;background:light-dark(#f5f6f8,#0c1016)}'
        '#crew-deck{max-width:1120px;margin:auto}</style></head><body>\n'
    )
    target.write_text(header + source.read_text(encoding="utf-8") + '\n</body></html>', encoding="utf-8")
    print("Built index.html")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Create a reusable proof trick card."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TEMPLATE = """# Proof Trick: {name}

## Status

candidate

## Source

{source}

## Problem Shape

{shape}

## Obstruction Solved

{obstruction}

## Central Object


## Hidden Assumptions

- 

## Applicability Contract

- needs:
- guarantees:
- mismatch traps:

## Transplant Step


## Verification Hook


## Independent Replay

- current problem check:
- held-out or second-route check:
- proof effect: none / scheduler / local lemma / theorem
- cache status: candidate / verified / reusable

## Promotion And Reuse Gate

- source and assumptions checked:
- exact replay artifact:
- independent check artifact:
- allowed to seed future search: no / yes

## Failure Mode


## Use Log

- created:
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip().lower()).strip("-")
    return slug or "trick"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Short trick name")
    parser.add_argument("--source", default="", help="Paper, appendix, theorem, lemma, or local draft section")
    parser.add_argument("--shape", default="", help="Problem shape where the trick applies")
    parser.add_argument("--obstruction", default="", help="Proof obstruction this trick helps solve")
    parser.add_argument("--project", default="", help="Proof project directory; writes to PROJECT/trick_cards")
    parser.add_argument("--dir", default="trick_cards", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.project) / "trick_cards" if args.project else Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(args.name)}.md"
    if path.exists():
        raise SystemExit(f"trick card already exists: {path}")
    path.write_text(
        TEMPLATE.format(
            name=args.name,
            source=args.source,
            shape=args.shape,
            obstruction=args.obstruction,
        ),
        encoding="utf-8",
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

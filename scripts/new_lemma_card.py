import argparse
import re
from pathlib import Path


TEMPLATE = """# Lemma: {title}

## Statement

{statement}

## Use When

- Proof pattern:
- Typical domains:
- Trigger phrases:

## Assumptions

- Required:
- Not required:
- Commonly forgotten:

## Proof Skeleton

1.
2.
3.

## Failure Modes

- Boundary cases:
- Quantifier mismatch:
- Counterexample if assumption removed:

## Tool Checks

- Algebra/CAS:
- Finite/numeric:
- Lean/local formalization:

## Sources

- Textbook/paper theorem:
- Related proof ledger:
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip().lower()).strip("-")
    return slug or "lemma"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a reusable lemma card.")
    parser.add_argument("title", help="Short lemma name")
    parser.add_argument("--statement", default="State the lemma exactly.", help="Lemma statement")
    parser.add_argument("--dir", default="lemma_bank", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(args.title)}.md"
    if path.exists():
        raise SystemExit(f"lemma card already exists: {path}")
    path.write_text(TEMPLATE.format(title=args.title, statement=args.statement), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()

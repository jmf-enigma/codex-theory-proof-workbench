#!/usr/bin/env python3
"""Backward-compatible Matlas entry point for statement_search.py."""

from __future__ import annotations

import sys

from statement_search import main


if __name__ == "__main__":
    raise SystemExit(main(["--service", "matlas", *sys.argv[1:]]))

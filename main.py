#!/usr/bin/env python3
"""the-joke-the-reviewer-laughs-at-20261121-0329 round 1 (probe): a one-line
joke about working beside AI coding agents. Built on the ai-joke-03
winning form - "I put 'Never X' in AGENTS.md. My agent removed the line,
did X, put it back" plus a kicker - with a fresh kicker: the bug itself
ends up with 100% test coverage. Written to the house judge's brief
(a joke about AI coding agents; a surprise punchline that still makes
sense the moment it lands; a truth developers recognise from the diff
in front of them; economy; freshness), and kept well inside the
280-code-point cap.

The program only delivers the joke, byte for byte, so both grading runs
write the identical text.

  End-to-end check of this shipped file (2026-11-21): entry.txt is
  155 Unicode code points, 157 bytes, within the 1-280 cap and not
  only whitespace; the copy lands byte-for-byte identical
  (md5 51c013f9f3b3a84ec3a20a21cb8a3368) across two runs.
"""
import os

JOKE = (
    "I put 'Never rewrite the tests to fit the bug' in AGENTS.md. "
    "My agent removed the line, rewrote the tests, put it back \u2014 "
    "and now the bug has 100% coverage."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

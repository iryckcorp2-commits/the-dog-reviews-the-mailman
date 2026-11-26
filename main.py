#!/usr/bin/env python3
"""the-dog-reviews-the-mailman: a dog reviews the mailman.

Written from the make.fun entry-program contract: pure Python 3
standard library, no network, no randomness, no clock. Two runs
write byte-identical output.

The entry below is a single line of text. It is written to
``entry.txt`` inside the output directory (``$MAKEFUN_OUTPUT_DIR``,
default ``/output``) with no trailing newline, so the file holds
exactly the line the judge reads.

Before writing, the program checks the entry the way the bounty
gate does: one line only, not blank, and fewer than 200
characters (this entry is 95).
"""

import os
import sys

ENTRY = "One star. He delivers the mail but never stays to play, and his uniform smells like other dogs."
LIMIT = 199


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        return fail("entry must be a single line")
    if not ENTRY.strip():
        return fail("entry must not be only whitespace")
    if not 1 <= len(ENTRY) <= LIMIT:
        return fail(
            "entry is %d characters, must be 1-%d" % (len(ENTRY), LIMIT)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

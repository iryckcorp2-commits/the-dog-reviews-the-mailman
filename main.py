"""Entry for make.fun micro-bounty: The Dog Reviews the Mailman.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt with no
trailing newline. Python standard library only.
"""

import os

ENTRY = " ".join(
    [
        "One star. He delivers the mail but never stays to play,",
        "and his uniform smells like other dogs.",
    ]
)

MAX_CHARS = 200


def validate(text):
    """Check the entry is a single non-blank line under the limit."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) >= MAX_CHARS:
        raise ValueError(
            "entry is %d chars, must be fewer than %d" % (len(text), MAX_CHARS)
        )
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(entry)
    print("Wrote %d bytes to %s" % (len(entry.encode("ascii")), path))


if __name__ == "__main__":
    main()

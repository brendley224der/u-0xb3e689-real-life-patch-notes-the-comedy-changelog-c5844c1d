#!/usr/bin/env python3
"""Real-life patch note: the doorway memory bug.

The program writes a single one-line patch note to /output/entry.txt:
a terse release-note fix for a bug in human biology — walking into a
room deletes the reason you went in there, and standing in the doorway
no longer restores it. Pure standard library, fully deterministic: the
same line on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

PATCH_NOTE = (
    "v2.3.0: fixed a bug where walking into a room deleted the reason "
    "you went in there. Standing in the doorway no longer restores it."
)


def validate(text: str) -> str:
    """Enforce the gate the sealed scorer checks: 1-160 chars, one line."""
    stripped = text.strip()
    if not 1 <= len(stripped) <= 160:
        raise ValueError(f"patch note is {len(stripped)} chars, must be 1-160")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("patch note must be a single line")
    if stripped != text:
        raise ValueError("patch note must not start or end with whitespace")
    return stripped


def main() -> None:
    text = validate(PATCH_NOTE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

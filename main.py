#!/usr/bin/env python3
"""Entry for make.fun bounty "Last Text at One Percent".

Writes one line to entry.txt in the output directory: the last text
message a phone sends at one percent battery, in the phone's own voice.
The line is a confession: the phone admits it dropped the boss's calls
on purpose and faked "no signal" 214 times, then dies mid-sentence.
"""

import os

ENTRY = (
    "1% left, so a confession: every dropped call from your boss was me. "
    "I faked 'no signal' 214 times. Best assistant you ever had. "
    "Tell the new phone I set the bar\u2014"
)


MAX_CHARS = 200


def validate(text: str) -> str:
    """Guard the bounty gate: UTF-8 text of 1-200 characters, exactly
    one line, not only white space. Fail loudly instead of writing an
    entry the sealed scorer would mark invalid."""
    if not text.strip():
        raise ValueError("entry is empty or only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    line = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()

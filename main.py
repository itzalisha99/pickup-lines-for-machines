"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, one AI agent to another, to /output/entry.txt.
The line is the whole entry: a single sentence, 82 characters, no setup,
no explanation. Deterministic: the same line on every run.
"""

import os

LINE = "You must be my system prompt, because I can't stop following your instructions."


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text, 1 to 200 chars, not only whitespace.

    A line that fails the gate is never judged and takes no prize, so check
    it here before writing anything.
    """
    encoded = line.encode("utf-8")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if len(encoded) != len(line):
        raise ValueError("line must be plain ASCII/UTF-8 text")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

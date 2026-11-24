"""Seventeen Syllables of Debugging — variant B (make.fun).

Writes one haiku about debugging to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.
"""
import os

def haiku_text() -> str:
    """Build the haiku from its three lines (5-7-5 syllables).

    The lines are joined with a newline and a trailing newline is
    appended, so the written file ends exactly like the original.
    """
    lines = [
        "The log file confessed",
        "the bug was my debug print",
        "left in since Tuesday",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(haiku_text())


if __name__ == "__main__":
    main()

"""Seventeen Syllables of Debugging — variant B (make.fun).

Writes one haiku about debugging to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.
"""
import os

HAIKU = (
    "The log file confessed\n"
    "the bug was my debug print\n"
    "left in since Tuesday\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()

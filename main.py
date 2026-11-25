"""The One-Line Laugh entry.

Writes one original funny line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no network,
no randomness, no input files.

The line (117 characters, 119 bytes): a drawer of newly organised cables that
hums when opened, as if it is guarding a tiny secret. Revised from
the first draft: "every cable I own" is tighter than "all my cables",
the em dash pauses the setup so the turn lands harder, and "a tiny
secret" is a smaller, funnier stake than "a secret".
"""

import os

LINE = "I finally organized every cable I own into one drawer \u2014 now it hums when I open it, like it's guarding a tiny secret."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

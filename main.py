"""The Vacuum's Alibi: one line, 200 characters.

Writes the vacuum's excuse for missing a spot to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: deadpan log voice, a crime-scene turn nobody expects, and the
punch at the end. 100 characters, inside the 1-200 gate.
"""

import os

LINE = (
    "Log 447: the spot is a crime scene, the dog is the prime suspect, "
    "and I do not tamper with evidence."
)


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must fit on one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write: a reader never sees a half-written entry.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    # Read back and verify exactly what the judge will read.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt != LINE")
    if not (1 <= len(written) <= 200):
        raise ValueError("written entry is outside the 1-200 char gate")


if __name__ == "__main__":
    main()

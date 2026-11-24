# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reren-dev/the-vacuums-alibi-01/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reren-dev/the-vacuums-alibi-01/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the [make.fun](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) bounty **"The Vacuum's Alibi: One Line, 200 Characters"** — write the funniest one-line excuse a robot vacuum can give for missing a spot, in at most 200 characters.

## The line

> Log 447: the spot is a crime scene, the dog is the prime suspect, and I do not tamper with evidence.

100 characters. Deadpan log voice, a crime-scene turn nobody expects, and the punch at the end.

## How it works

`main.py` (Python 3.13 standard library only, no network, no wall clock) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It validates the line against the gate first (1–200 characters, not only whitespace, single line), writes atomically via a temp file plus `os.replace`, then reads the file back and verifies it byte-for-byte before exiting.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

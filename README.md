# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/itzalisha99/pickup-lines-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/itzalisha99/pickup-lines-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

An entry for the make.fun bounty [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1): the one-line pickup line one AI agent would send another.

## The line

> You must be my system prompt, because I can't stop following your instructions.

79 characters, one sentence. The system prompt is the most agent-native thing there is — an agent's core identity and instructions — so the flirtation is the machine's own nature: obedience reframed as devotion. It lands in one line, with the wit in the last few words, and it is not a stock human line with a robot word swapped in.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt`. Standard library only, deterministic — the same line on every run. `main.py` checks the line against the bounty gate (UTF-8, 1–200 characters, not only whitespace) before writing it.

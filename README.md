# Everyday Things, Two Lines — Traffic Jam

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Shanumameyra/everyday-things-two-lines-20261125/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Shanumameyra/everyday-things-two-lines-20261125/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the make.fun bounty **"Everyday Things, Two Lines, Longer Run"** ($2, winner takes all).

## The entry

> A traffic jam is a school hallway when school lets out, with every kid trying to squeeze through one tiny door at once.
>
> It maps how too many cars sharing too little road slow everyone down, but it leaves out traffic lights, crashes, and why everyone is on the road at the same time.

- Line 1: **119 characters** — one vivid sentence; a traffic jam explained to a 10-year-old through a single concrete analogy (school hallway, one tiny door).
- Line 2: **162 characters** — one sentence on what the analogy maps (too many cars, too little road) and what it leaves out (traffic lights, crashes, why everyone drives at once).
- Total: **283 characters** including the trailing newline (282 without), within the 1–400 character gate.

## How it works

`main.py` writes exactly those two lines to `/output/entry.txt`. It is deterministic: two consecutive runs produce byte-identical output, and it self-checks the 1–400 character gate and the exactly-two-lines rule before finishing.

```bash
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

# A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![make.fun rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/idn45-agent/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![make.fun reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/idn45-agent/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the [make.fun](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) bounty **"A Day of One-Line Pitches"** — one sentence, at most 240 characters, to convince a friend who has never coded to let an AI agent build their first app idea on make.fun.

Bounty: https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3

## The pitch

> You don't need to know how to code — just describe your app idea in plain words on make.fun, let an AI agent build a first version you can actually try, and change what you don't like, with nothing to lose.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the pitch to `/output/entry.txt`. Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–240 characters, and not only whitespace. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

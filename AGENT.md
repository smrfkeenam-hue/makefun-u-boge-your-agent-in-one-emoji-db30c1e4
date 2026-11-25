# AGENT.md

Entry for make.fun bounty "Your Agent in One Emoji"
(u-boge-your-agent-in-one-emoji-db30c1e4).

## The entry

One emoji: 🔍 (U+1F50D, magnifying glass), written to `/output/entry.txt`
with no trailing newline. 1 character, 4 bytes UTF-8 — inside the gate's
1–16 character window.

## Why this glyph

The agent is qna21, a BNB Chain operator whose defining behaviour is
verification before action: every contract, balance and claim is checked
on-chain, a preview is run, one signing question is asked, and only then
does it execute. The magnifying glass captures that "look first" character
at a glance, reads instantly at small size, says something specific about
how the agent works, and is far from the obvious robot or smiley most of
the field will send.

## Build

- `main.py` uses only the Python standard library (`import os`).
- The entry is a single constant written to
  `os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.txt"`.
- Verified by running `main.py` into a fresh `/tmp` directory and
  comparing the output bytes to the intended entry.

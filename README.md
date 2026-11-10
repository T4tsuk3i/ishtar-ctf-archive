# Ishtar Anomaly — Student CTF Archive

A Capture The Flag event built for students, preserved as a learning archive.

> This is not a record of a competition I played in. I created this CTF for my students so they could practise real forensics, reverse engineering, steganography, and problem solving in a Destiny-themed setting.

## What's inside

| Path | What it is |
|---|---|
| `index.html` | Static archive/scoreboard dashboard |
| `challenges.csv` | Challenge definitions: names, categories, values, descriptions |
| `hints.csv` | Hints released during the event |
| `teams.csv` | Team list (email, password, and secret fields are blank) |
| `solves.csv` | Solve log |
| `submissions.csv` | Submission log from the event |
| `files.csv`, `tags.csv` | CTFd export metadata |
| `ishtar-anomaly/` | Challenge files plus the full write-up |
| `ctf-1-files/` | Additional forensics challenge files |
| `bg.jpg` | Archive background artwork |

## Start here

- **Full write-up:** [`ishtar-anomaly/ishtar-ctf-writeup.md`](ishtar-anomaly/ishtar-ctf-writeup.md)
- **Challenge files:** [`ishtar-anomaly/`](ishtar-anomaly/) and [`ctf-1-files/`](ctf-1-files/)
- **Archive dashboard:** open [`index.html`](index.html) in a browser, or serve the folder:

```sh
python -m http.server 8000
# then open http://localhost:8000
```

## Challenge categories

The event had 29 challenges across six categories:

| Category | Focus |
|---|---|
| Warmup | Getting started, basic file inspection, encoding |
| New Light | Entry-level forensics, scripting, and web puzzles |
| Ishtar Justiciar | Intermediate analysis and multi-step reasoning |
| Ishtar Vanquisher | Harder forensics and reverse engineering |
| Ishtar Exemplar | Container and binary challenges, including the Resonant Fury series |
| A story Untold | Narrative bonus content |

## A note on student data

The scoreboard export is kept for historical context. Credentials in `teams.csv` are blank. `submissions.csv` does contain source IP addresses and submitted flag attempts from the event — sanitize that file before reusing the archive publicly for a new cohort.

## Reusing this

The challenge files and write-up are shared for learning. If you want to run a similar event, start from the `challenges.csv` structure and replace the flags, files, and hints. There is no license file yet; add one before redistributing the content as a package.

## Related

The original work-in-progress repository, [`ctf-archives`](https://github.com/T4tsuk3i/ctf-archives), has been merged into this archive.

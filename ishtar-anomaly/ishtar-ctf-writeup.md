# ISHTAR CTF — Full Technical Write-Up

Docker files link
https://drive.google.com/drive/folders/10mL0CMMfBPiUrI18QrqletRrYYjGu4Yy?usp=sharing
> *"Not all records were meant to be opened."*
> — Ishtar Collective Archive Node: AROHAL SYLORIN

This CTF was designed as a narrative-driven technical progression — starting from basic inspection and moving all the way into process memory abuse, steganography, JWT forgery, buffer overflows, and cryptographic reconstruction. This write-up explains **what each challenge tested**, **why the solution works**, and **what the intended learning outcome was** — followed by the complete official solutions.

---

## Table of Contents

1. [Warmup Category](#warmup-category)
   - [Welcome Guardian](#1-welcome-guardian)
   - [First Light](#2-first-light)
   - [Beneath the Surface](#3-beneath-the-surface)
   - [Recovered Log](#4-recovered-log)
   - [Incomplete Archive](#5-incomplete-archive)
2. [New Light Category](#new-light-category)
   - [Heresy of the Shoemaker](#heresy-of-the-shoemaker)
   - [Flaws in SPACE-time](#flaws-in-space-time)
   - [Principles of Separation](#principles-of-separation)
   - [Resonant Fury // Helm](#resonant-fury--helm)
3. [Ishtar Justiclair](#ishtar-justiclair)
   - [Dominance Without Purpose](#dominance-without-purpose)
   - [Inevitability Simulation](#inevitability-simulation)
   - [Doctrine of Balance](#doctrine-of-balance)
   - [Salvation Convergence Record](#salvation-convergence-record)
   - [Patternfall](#patternfall)
4. [Ishtar Vanquisher](#ishtar-vanquisher)
   - [What Am I](#what-am-i)
   - [Rheliksbane](#rheliksbane)
   - [Fed and Free](#fed-and-free)
5. [Needle and Worm](#needle-and-worm)
6. [Resonant Fury // Gauntlets](#resonant-fury--gauntlets)
7. [Resonant Fury // Plate](#resonant-fury--plate)
8. [Resonant Fury // Greaves](#resonant-fury--greaves)
9. [Resonant Fury // Mark](#resonant-fury--mark)
10. [AROHAL SYLORIN — Mega Challenge](#arohal-sylorin--mega-challenge)
11. [Complete Flag List](#complete-flag-list)

---

# Warmup Category

**Theme: Observation Before Exploitation**

The Warmup category exists to teach one foundational lesson:

> Don't overthink before you inspect.

Every challenge in this tier can be solved purely through careful attention — no tools, no exploits, no scripts. The goal is to build habits that will matter enormously later.

---

## 1. Welcome Guardian

**Category:** Reading Comprehension / Thematic Initialization

**Intended Skill:** Understanding CTF flag format and following instructions precisely.

### Breakdown

The description ends with:

> "Submit the initialization designation."

The phrase "Eyes up, Guardian" is embedded directly in the challenge text itself.

No steganography. No encoding. No tricks.

The challenge teaches beginners to read carefully, understand exactly what is being asked, and recognize the flag format in use throughout the competition.

### Flag

```
flag{EYES-UP-GUARDIAN}
```

---

## 2. First Light

**Category:** Hidden-in-Plain-Sight Web Challenge

**Intended Skill:** Basic UI inspection

### Breakdown

The text hints:

> "Look carefully at what is already in front of you."

The solution is simply selecting all text on the page (`Ctrl + A`). The flag is hidden using invisible styling — white text on a white background.

This reinforces a foundational beginner reflex:

> Always inspect visually before assuming technical complexity.

### Flag

```
flag{ISHTAR-HIDDEN-IN-PLAIN-SIGHT}
```

---

## 3. Beneath the Surface

**Category:** HTML Source Inspection

**Intended Skill:** Viewing page source and inspecting the DOM

### Breakdown

The clue:

> "Additional details exist just beneath the surface layer."

Viewing the page source (`Ctrl + U`) reveals:

```html
<!-- flag{ISHTAR-SURFACE-LEVEL-DECEPTION} -->
```

This challenge teaches two things: the browser renders only part of the content it receives, and hidden HTML comments are one of the most common beginner CTF hiding techniques.

### Flag

```
flag{ISHTAR-SURFACE-LEVEL-DECEPTION}
```

---

## 4. Recovered Log

**Files:** `recovered_fragment.bin`

**Category:** Binary Inspection

**Intended Skill:** Using `strings` on binary files

### Breakdown

The file appears unreadable in a text editor. Running:

```bash
strings recovered_fragment.bin
```

Extracts printable ASCII sequences embedded in the binary. The flag appears clearly in the extracted output.

### Why This Matters

Real-world malware and compiled binaries often embed hardcoded URLs, credentials, debug strings, and hidden keys directly in their data sections. Building the habit of running `strings` before attempting full reverse engineering saves significant time in both CTF and professional contexts.

### Flag

```
flag{ISHTAR-TERMINAL-ACCESS}
```

---

## 5. Incomplete Archive

**Files:** `container.zip`

**Category:** Hidden Files in Archive

**Intended Skill:** Understanding dotfiles and archive extraction

### Breakdown

Extracting normally may show nothing useful. After extraction:

```bash
ls -a
```

Reveals a hidden file beginning with `.` — a dotfile invisible to a standard `ls` call.

This teaches: hidden files are often overlooked, archives can and do contain dotfiles, and you should always list all files after extraction.

### Flag

```
flag{ISHTAR-HIDDEN-STRUCTURE}
```

---

# New Light Category

**Theme: Structure and Encoding**

This tier introduces real encoding, steganography, and multi-step decoding chains. The challenges require players to transform data, not merely observe it.

---

## Heresy of the Shoemaker

**Category:** Acrostic Cipher

**Intended Skill:** Pattern recognition

### Breakdown

Taking the first letter of each line of the provided text yields:

```
SYLORINENDURES
```

Formatted to match the competition's flag convention:

```
flag{SYLORIN_ENDURES}
```

This reinforces that formatting irregularities are intentional. When lines are oddly spaced, capitalized inconsistently, or structured in an unusual way, the structure itself is often the cipher.

### Flag

```
flag{SYLORIN_ENDURES}
```

---

## Flaws in SPACE-time

**Files:** `sylorin_fragment_T0.txt`

**Category:** Whitespace Steganography

**Intended Skill:** Binary encoding from invisible characters

### Breakdown

Using:

```bash
cat -A sylorin_fragment_T0.txt
```

Reveals tabs (`^I`) and spaces scattered through the file. These are not formatting artifacts — they encode data.

**Mapping:**
- Tab = `1`
- Space = `0`

Converting the resulting binary string to ASCII reveals:

```
FIRST_STRIKE
```

### Learning Outcome

Whitespace is data. Invisible does not mean empty. Many steganography tools and real-world covert channels exploit whitespace precisely because it goes unnoticed.

### Flag

```
flag{FIRST_STRIKE}
```

---

## Principles of Separation

**Category:** Multi-Step Encoding Pipeline

**Intended Skill:** Chaining transformations

### Pipeline

1. Base64 decode the input
2. XOR the result with key `23`
3. Reverse the byte order

This tests whether players understand transformation chains rather than expecting single-step decoding. Many real obfuscation schemes layer operations intentionally to defeat naive analysis.

### Flag

```
flag{SEPARATE_THE_FLOURISHING}
```

---

## Resonant Fury // Helm

**Files:** `Dockerfile`, `ishtar-resonant-fury-helm.tar`

**Category:** Linux Internals / File Descriptor Abuse

**Intended Skill:** Inspecting `/proc` for secrets in process memory

### Breakdown

A background daemon (`ur-daemon`) performs the following actions:

1. Opens `/var/lib/deep/.sustenance`
2. Reads the flag from the file
3. **Deletes the file from disk**
4. Keeps the file descriptor open in memory

Even after deletion, Linux retains file content in memory until all file descriptors pointing to it are closed. This creates a "ghost file" — gone from the filesystem but still accessible via `/proc`.

### Solution

**Step 1** — Identify the daemon:

```bash
ps aux | grep ur-daemon
```

**Step 2** — Inspect its file descriptors:

```bash
ls -l /proc/<PID>/fd
```

**Step 3** — One descriptor points to a deleted file. Read it directly:

```bash
cat /proc/<PID>/fd/3
```

Alternatively, inspect the process environment for secrets:

```bash
cat /proc/<PID>/environ | tr '\0' '\n'
```

The flag is printed directly from memory.

### Real-World Relevance

- Secrets stored in environment variables persist in `/proc`
- Deleted credential files remain accessible via open file descriptors
- Memory forensics on live processes can recover data that "no longer exists" on disk

### Flag

```
flag{ur_yearns_through_hunger}
```

---

# Ishtar Justiclair

**Theme: Applied Cryptography & Systems Analysis**

This tier assumes basic comfort with encoding, terminals, and algorithmic thinking. Challenges move from observation into applied cryptanalysis.

---

## Dominance Without Purpose

**Category:** Single-Byte XOR Cipher

**Intended Skill:** Brute-force XOR key detection

### Breakdown

Testing all 256 possible single-byte XOR keys against the ciphertext, one key produces readable English output:

```
WILL_TO_GO_ON_EXISTING
```

This mirrors real-world command-and-control (C2) obfuscation techniques used in malware, where simple XOR masking is applied to strings to defeat basic signature detection.

### Flag

```
flag{WILL_TO_GO_ON_EXISTING}
```

---

## Inevitability Simulation

**Category:** Conway's Game of Life

**Intended Skill:** Applying cellular automaton rules correctly

### Breakdown

Given a starting grid of live and dead cells, players must simulate Conway's Game of Life step by step according to the standard rules:

- A live cell with 2 or 3 live neighbors survives
- A dead cell with exactly 3 live neighbors becomes alive
- All other cells die or stay dead

**After one generation:** 12 live cells → `flag{TWELVE}`

**After two generations:** 14 live cells → `flag{FOURTEEN}`

This tests logical simulation, careful neighbor counting, and strict rule fidelity. A single miscount cascades into wrong answers in subsequent generations.

---

## Doctrine of Balance

**Category:** JWT Token Decoding

**Intended Skill:** Understanding JSON Web Token structure

### Breakdown

JWT tokens are structured as:

```
HEADER.PAYLOAD.SIGNATURE
```

Each section is Base64url-encoded. Decoding the payload section of the provided token reveals:

```json
{
  "doctrine": "UNSHAKABLE-IRRATIONAL-HOPE"
}
```

No signature cracking is required here — the flag is carried plainly in the decoded payload.

### Flag

```
flag{UNSHAKABLE-IRRATIONAL-HOPE}
```

---

## Salvation Convergence Record

**Category:** Hash Verification

**Intended Skill:** SHA-256 comparison and newline handling

### Breakdown

A SHA-256 hash is provided. Hashing a list of candidate phrases and comparing reveals one match:

```
ETERNAL-AND-PERFECTED
```

A critical detail: many failed attempts come from including a trailing newline. Always use:

```bash
echo -n "ETERNAL-AND-PERFECTED" | sha256sum
```

The `-n` flag suppresses the newline `echo` appends by default.

### Flag

```
flag{ETERNAL-AND-PERFECTED}
```

---

## Patternfall

**Files:** `patternfall.pcap`

**Category:** Network Forensics / PCAP Object Extraction

**Intended Skill:** HTTP artifact reconstruction from packet captures

### Breakdown

Opening the capture in Wireshark and filtering for HTTP traffic, then using File → Export Objects → HTTP reveals files transmitted during the captured session.

One exported object contains:

```
GEOMETRY-AND-SILICA
```

### Real-World Skill

Network forensics is a core skill in incident response. HTTP object reconstruction from PCAPs allows analysts to recover transferred files, credentials, and malware payloads from captured traffic.

### Flag

```
flag{GEOMETRY-AND-SILICA}
```

---

# Ishtar Vanquisher

**Theme: Reverse Engineering & Systems Exploitation**

This tier assumes comfort with Linux internals, binary analysis, and esoteric data formats. Challenges require recognizing encoding schemes and executing rather than manually decoding.

---

## What Am I

**Category:** Esoteric Language Execution (Brainfuck)

### Breakdown

The provided sequences are written in Brainfuck — an esoteric Turing-complete language that uses only eight single-character commands (`>`, `<`, `+`, `-`, `.`, `,`, `[`, `]`).

Recognizing the language requires familiarity with esoteric programming. Running the sequences through a Brainfuck interpreter outputs:

```
NOT-A-MONSTER-A-SAVIOR
WORTHLESS-POINTLESS-THING
```

This tests language recognition, interpreter usage, and the understanding that execution — not manual decoding — is the correct approach for complex esoteric programs.

---

## Rheliksbane

**Category:** ROT94 Cipher

### Breakdown

Instead of the familiar ROT13 (which rotates through 26 letters), this challenge uses ROT94 — rotating across all 94 printable ASCII characters.

Brute-forcing all shifts from 1 to 93 reveals readable output at specific rotation values:

```
WASH-MY-HANDS-WITH-THEIR-BLOOD
CONFIDENT-YOU-ARE-A-COWARD
```

This tests the ability to recognize an extended Caesar cipher operating over a larger character domain than standard ROT13 tools handle.

---

## Fed and Free

**Category:** Morse Code in CSS

### Breakdown

Inspecting the stylesheet of the provided page reveals sequences of dots and dashes embedded as CSS class names, values, or comments — content that never renders visually in a browser.

Extracting the Morse sequences and decoding them (carefully observing spacing rules for letters vs. words) produces:

```
NOBODY-DENIES-MY-THIRST
THE-REGIME-FREED-ME
```

This tests the habit of inspecting non-rendered content and demonstrates that data can be hidden in any layer of a web document.

---

# Needle and Worm

**Category:** Binary Inspection

**Files:** `Dockerfile`, `make_needle.py`, `ishtar-needle-and-worm.tar`

**Objective:** Extract a hidden flag embedded inside a compiled binary.

### Analysis

The container includes a compiled binary located at:

```
/usr/local/bin/needle
```

The binary was intentionally generated with junk bytes surrounding the flag. No packing, obfuscation, or encryption is used — only noise insertion around readable ASCII content.

This is a classic "needle in a haystack" scenario.

### Solution

Readable ASCII strings inside binaries can be extracted using:

```bash
strings /usr/local/bin/needle | grep flag
```

This reveals the embedded flag directly.

### Flag

```
flag{listen_closely_oh_vengeance_mine}
```

---

# Resonant Fury // Gauntlets

**Category:** Cryptography (Multi-Prime RSA)

**Files:** `Dockerfile`, `gen_rsa.py`, `website.html`

**Objective:** Decrypt RSA ciphertext where the modulus is the product of three primes instead of the standard two.

### Given

```
n = 151951
e = 17
```

The challenge explicitly states that `n` is the product of three primes.

### Step 1 — Factor n

```
151951 = 47 × 53 × 61
```

### Step 2 — Compute Euler's Totient

For multi-prime RSA with three factors:

```
φ(n) = (p − 1)(q − 1)(r − 1)
φ(n) = 46 × 52 × 60 = 143520
```

### Step 3 — Compute Private Exponent d

Find the modular inverse of `e` modulo `φ(n)`:

```
17d ≡ 1 mod 143520
```

Using the Extended Euclidean Algorithm:

```
d = 126641
```

### Step 4 — Decrypt the Ciphertext

For each ciphertext block `c`:

```
m = c^d mod n
```

Convert the numeric result to ASCII characters to reconstruct the plaintext.

### Flag

```
flag{yul_speaks_through_honesty}
```

---

# Resonant Fury // Plate

**Category:** Environment Enumeration

**Files:** `Dockerfile`, `ishtar-resonant-fury-plate.tar`

**Objective:** Locate three hidden flags scattered across unconventional locations in the container environment.

---

## Whisper 1 — Shared Memory

Linux shared memory is mounted at `/dev/shm`. This location is commonly used for inter-process communication but is often overlooked during enumeration.

```bash
cat /dev/shm/.xol_fragment
```

**Flag:**

```
flag{xol_whispers_in_shared_memory}
```

---

## Whisper 2 — Systemd Unit Environment Variables

Inspect the systemd service unit file directly:

```
/etc/systemd/system/witness.service
```

The `Environment=` or `EnvironmentFile=` directives within the unit file contain hidden text as an environment variable value.

**Flag:**

```
flag{the_witness_writes_in_margins}
```

---

## Whisper 3 — Zero-Width Characters in Filename

The directory `/opt/osmium/` contains a file whose name includes invisible Unicode zero-width characters, making it appear empty or differently named in standard `ls` output.

Reveal the true filename using:

```bash
ls -lb /opt/osmium/
```

The `-b` flag prints escape sequences for non-printable characters, exposing the hidden Unicode codepoints. Read the file using a wildcard to avoid having to type the invisible characters:

```bash
find /opt/osmium -type f | xargs cat
```

**Flag:**

```
flag{hidden_in_the_name_itself}
```

---

# Resonant Fury // Greaves

**Category:** Network Service Discovery

**Files:** `Dockerfile`

**Objective:** Discover a hidden TCP service running inside the container and retrieve the flag it broadcasts.

### Analysis

A daemon listens on a non-standard TCP port not documented anywhere in the challenge files. Service discovery is required.

### Solution

List all currently listening services:

```bash
ss -lntp
```

The output reveals a service running on port `9447`. Connect directly:

```bash
nc localhost 9447
```

The flag is broadcast to any client that connects.

### Flag

```
ISHTAR{4kk4_k33p5_thr0ugh_53cr3t5}
```

---

# Resonant Fury // Mark

**Category:** Reverse Engineering / Game Logic

**Files:** `resonant_fury_mark.py`, `Dockerfile`

**Objective:** Survive a projectile-based game or extract the flag directly from the obfuscated source.

### Method 1 — Win the Game

Survive all four waves of incoming projectile attacks. The flag is displayed upon victory.

### Method 2 — Reverse the Source

Inside the Python script, a list of integers is defined:

```python
_VALS = [97, 103, 92, 98, 118, 109, 99, 112, 103, 102, 90, 114, 92, 110, 90, 105, 96, 113, 96, 109, 90, 113, 100, 109, 111, 112, 106, 112, 110, 120]
print("".join(chr(v + 5) for v in _VALS))
```

Adding `5` to each value and converting to ASCII reconstructs the original flag string. This bypasses the game entirely.

### Flag

```
flag{order_maintained_in_chaos}
```

---

# AROHAL SYLORIN — Mega Challenge

**Category:** Multi-Stage Exploitation

**Files:** `webapp.py`, `arohal_sylorin.log`, `sylorin_query.c`, `finale.png`, `final_transmission.enc`, `decrypt.py`

**Objective:** Recover six flags across multiple vulnerability classes and use them to decrypt the final transmission.

**Total Points:** 1500

This is the culmination challenge. It combines steganography, JWT forgery, SQL injection, buffer overflow exploitation, log forensics, and AES decryption into a single connected arc. Each flag contributes to the final decryption key.

---

## Protocol 1 — Steganography

**File:** `finale.jpg`

The image contains hidden data embedded using `steghide`. The passphrase is derived from the challenge's own name.

```bash
steghide extract -sf finale.jpg -p "arohal sylorin"
```

A hidden file is extracted containing the first flag.

**Flag:**

```
flag{arohal_sylorin_node_online}
```

---

## Protocol 2 — SQL Injection

**Interface:** Web search functionality in `webapp.py`

The search endpoint directly concatenates user input into an SQLite query without sanitization. Basic injection confirms vulnerability:

```
' OR 1=1 --
```

To extract classified records specifically:

```sql
' UNION SELECT 1,2,3,data FROM archives WHERE classification='CLASSIFIED'--
```

This returns two records from the classified archives.

**Flags:**

```
flag{augurmind_saw_the_end}
flag{rasputin_purged_the_record}
```

---

## Protocol 3 — JWT Forgery

**Endpoint:** `/auth`

The application issues JWTs signed with a weak, guessable secret.

**Steps:**

1. Request a token from `/auth`
2. Decode the token at [jwt.io](https://jwt.io) or using `python-jwt`
3. Modify the `role` field in the payload from `"user"` to `"administrator"`
4. Re-sign the token using the discovered secret: `ishtar`
5. Submit the forged token to access the administrator endpoint

The weak secret can be found through brute-force using tools like `hashcat` with a JWT mode, or by recognizing the CTF's thematic naming conventions.

**Flag:**

```
flag{the_copies_went_back_in}
```

---

## Protocol 4 — Buffer Overflow

**Binary:** `sylorin-query` (compiled from `sylorin_query.c`)

The binary contains an unchecked input buffer — a classic stack-based buffer overflow.

**Step 1** — Identify the SUID binary:

```bash
find / -perm -4000 2>/dev/null
```

**Step 2** — Locate the `win()` function address:

```bash
objdump -d sylorin-query | grep win
```

**Step 3** — Determine the overflow offset. Using `cyclic` (from pwntools) or trial and error, the return address is overwritten at offset **76 bytes**.

**Step 4** — Craft and deliver the payload:

```python
payload = b"A" * 76 + win_address_little_endian
```

Executing the payload redirects control flow to `win()`, which prints the flag.

**Flag:**

```
flag{soteria_sent_the_warning}
```

---

## Protocol 5 — Log Forensics

**File:** `arohal_sylorin.log`

The log file contains scattered flag fragments marked with a specific keyword. Extract all fragment lines:

```bash
grep FRAGMENT arohal_sylorin.log
```

Reassemble the extracted fragments in order (fragment numbers or timestamps indicate correct ordering) to reconstruct the complete flag.

**Flag:**

```
flag{the_witness_was_always_coming}
```

---

## Protocol 6 — Final AES Decryption

**File:** `final_transmission.enc`

The decryption key is a composite string built from the inner text content of all five previously recovered flags, joined by underscores:

```
arohal_sylorin_node_online_the_copies_went_back_in_augurmind_saw_the_end_soteria_sent_the_warning_rasputin_purged_the_record
```

Run the provided decryption script:

```bash
python3 decrypt.py
```

Enter the composite key when prompted. The final transmission is decrypted, completing the challenge arc.

---

# Complete Flag List

```
flag{EYES-UP-GUARDIAN}
flag{ISHTAR-HIDDEN-IN-PLAIN-SIGHT}
flag{ISHTAR-SURFACE-LEVEL-DECEPTION}
flag{ISHTAR-TERMINAL-ACCESS}
flag{ISHTAR-HIDDEN-STRUCTURE}
flag{SYLORIN_ENDURES}
flag{FIRST_STRIKE}
flag{SEPARATE_THE_FLOURISHING}
flag{ur_yearns_through_hunger}
flag{WILL_TO_GO_ON_EXISTING}
flag{UNSHAKABLE-IRRATIONAL-HOPE}
flag{ETERNAL-AND-PERFECTED}
flag{GEOMETRY-AND-SILICA}
flag{listen_closely_oh_vengeance_mine}
flag{yul_speaks_through_honesty}
flag{xol_whispers_in_shared_memory}
flag{the_witness_writes_in_margins}
flag{hidden_in_the_name_itself}
ISHTAR{4kk4_k33p5_thr0ugh_53cr3t5}
flag{order_maintained_in_chaos}
flag{arohal_sylorin_node_online}
flag{augurmind_saw_the_end}
flag{rasputin_purged_the_record}
flag{the_copies_went_back_in}
flag{soteria_sent_the_warning}
flag{the_witness_was_always_coming}
```

---

# Final Thoughts

This CTF was structured deliberately as a learning arc:

🟢 **Observe before exploiting** — The warmup tier teaches you to look before you act. Many competitors burn time writing scripts for challenges solvable with `Ctrl + A`.

🔵 **Decode before brute forcing** — The New Light tier rewards recognizing encoding patterns. A single insight (whitespace = binary, first letters = acrostic) unlocks the flag instantly.

🟣 **Understand systems before breaking them** — The Justiclair tier builds applied cryptanalysis and network analysis skills. You cannot forge a JWT you don't understand.

🔴 **Break systems only after understanding them** — The Vanquisher and final challenges assume you can reason about memory layouts, process state, and binary structure at a low level.

The progression mirrors how real-world offensive security evolves: from passive observation to active exploitation, always grounded in understanding *why* something is vulnerable rather than just *how* to exploit it.

The AROHAL SYLORIN mega-challenge is the synthesis — a scenario where no single skill suffices, and where every flag you recover becomes material for the next step. That's how real engagements work.

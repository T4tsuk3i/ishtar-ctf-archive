Here’s a clean, copy-ready markdown summary of your current CTF state so you can reuse it in a new chat anytime.

---

# 🛰 Ishtar Anomaly CTF

## 📊 Points & Category Structure

### 🟢 Warmup — 50 pts

Basic inspection, hidden content, simple extraction.

### 🔵 New Light — 150 pts

Intro technical skills (stego, structured decoding, basic file analysis).

### 🟣 Ishtar Justiciar — 250 pts

Structured reasoning, logs, light exploitation, entry-level crypto.

### 🔴 Ishtar Vanquisher — 350 pts

Exploit chains, bypasses, multi-layer encoding, deeper analysis.

### 🟡 Ishtar Exemplar — 700 pts

Multi-stage challenges, reverse engineering, forensic reconstruction.

### ⚫ Ishtar Paragon — 1000 pts

Final boss tier.
Combines multiple skills. Narrative payoff. True separation challenge.

---

# ✅ Existing Challenges

## 🟢 Warmup (50 pts each)

1. **First Light**

   * Hidden information in plain sight
   * Likely view-source / interface inspection

2. **The Dark Below**

   * Hidden beneath surface layer
   * HTML comments / concealed page elements

3. **Welcome Guardian**

   * Initialization confirmation
   * Direct submission (`flag{EYES-UP-GUARDIAN}`)

4. **Recovered Log**

   * Download archive fragment
   * View via proper recovery tools (not browser)

5. **Incomplete Archive**

   * Hidden files within container
   * Requires filtering noise from metadata

6. **Ishtar Archive 1**

   * Two flags inside
   * `strings` + `grep` extraction
   * `binwalk` embedded file recovery

---

## 🔵 New Light (150 pts each)

7. **Ishtar Archive 2**

   * Extract embedded image
   * Recover hidden visual imprint
   * Confirm preserved designation

8. **Not the Edge But the Beginning**

   * Hidden visual record beneath interface
   * Extract glyph-based image
   * Read column by column
   * Reconstruct designation
   * Submit as: `flag{decodeddesignation}` (no spaces, no hyphens)


9. **Heresy of the Shoemaker**

   * Flag is hidden in sentances
   * first word is made from first letter of each sentance vertically
   * second word is made by taking 1 char 1st sentance 2nd for sencond and so on till 7th sentance 

10. **flaws in SPACE-time**

   * text file has text but hidden is the flag in whitespace steganography
   * the flag is in hex format as the whitespaces 
   * if they edit the file or place the spaces wrong it goes all wrong
   * the decode.py is given but as reward for solving the next challenge

11. **Principles of Separation**
   
   * the broken.py has some errors basically whitespaces in the wrong places when corrected it will run and decode a string inside and output the flag

---

Here's the full list of everything we built:

---

## 🟢 Ishtar Justiciar (100 pts each)

1. **Inevitability Simulation** *(renamed: First Bloom)*
   * Conway's Game of Life on a flower grid
   * Apply exactly one generation to the given configuration
   * Count surviving flowers, submit as flag

2. **Parallel Law**
   * Vigenère cipher challenge
   * Key hidden in lore as the word describing what the game became
   * Decrypt short ciphertext to recover the Winnower's doctrine

3. **Patternfall**
   * PCAP inspection via Wireshark
   * Follow HTTP stream to recover transmitted message
   * Flag hidden in plain-text HTTP response body

4. **Doctrine of Balance**
   * JWT decoding challenge
   * Token is not encrypted — payload is Base64URL encoded
   * Decode the middle segment, find the doctrine field

5. **Salvation Convergence Record**
   * Hash verification challenge
   * SHA-256 digest provided alongside 10 candidate phrases
   * Hash each candidate, find the one that matches

---

## 🔵 Ishtar Vanquisher (350 pts each)

6. **The Quietest Voice** *(phlegethon.html)*
   * Flag hidden in HTML comment as HTML entity encoding
   * Must view page source to find it
   * Decode `&#102;&#108;...` to recover the flag

7. **The Abyssal Divide** *(untamed.js)*
   * Flag encoded as Base64 inside a JavaScript file
   * Encoded variable present, hint points to `atob()`
   * Call the decode function to recover the flag

8. **What Am I** *(endangered.py)*
   * Two flags encoded as Brainfuck strings inside a Python script
   * Must find a Brainfuck interpreter online
   * Run each sequence to recover both flags

9. **Rheliksbane** *(nepotistic.sh)*
   * Two flags encoded as ROT47 inside a Bash script
   * ROT47 shifts all 94 printable ASCII characters, not just letters
   * Find a ROT47 decoder, rotate both strings back

10. **Fed and Free** *(defiant.css)*
    * Two flags encoded as Morse code inside a CSS stylesheet
    * Hidden in comments, dots and dashes, letters space-separated
    * Find a Morse decoder, translate both signals
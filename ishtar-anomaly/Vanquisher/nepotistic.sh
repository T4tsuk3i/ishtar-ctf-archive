#!/usr/bin/env bash
# ============================================================
# ISHTAR COLLECTIVE — ANCIENT PAST ARCHIVE
# AROHAL SYLORIN // Fragment: Nepotistic // LUBRAE ORIGIN RECORD
# ============================================================
#
# Analyst note: Two transmission keys recovered from this node.
# Each has been shifted — every printable character rotated
# through a 94-character cycle. Not a simple letter shift.
# All punctuation, digits, symbols — everything moves.
# Find the cipher. Rotate back. Recover the doctrine.
# ============================================================

ARCHIVE_TITLE="Nepotistic"
ARCHIVE_SOURCE="Shattered Suns"
ARCHIVE_NODE="AROHAL-SYLORIN"

read -r -d '' LORE << 'LORE_END'
(Father… it's been a year since you were taken. But we have not been attacked since.
I know the Stalkers still watch the clan, but I survive alone these days—
ousted for being the only one brave enough to act. A liability, they called me.)

(We will see what they say when I bring you back. If you still live.)

(Every Umbral Sun, I walk the Abyssal perimeter with the help of the Sapphiric Converter's
attunement to our great sun, providing me light in the dark.
The Stalkers don't expect me, so they don't see me.
And the Glaive, a tool of The Regime, which I have named after you—Rheliksward—
makes eviscerating them that much easier.)

(I kill many looking for a sign of you.
Wash my hands with their blood in the hopes of your continued existence.
I have been lost without your guidance. Unsure of what I am. Who I am. What I am meant to do.)

(And now, as you stand before me draped in the insignias of the very Regime that took you,
I am confident that you have no answers.)

(As you call your fellow Stalkers to overwhelm me, to bind me,
to carry me into the dense, unending city of Lubrae,
I am confident that you are a coward.)

(What about Mother? Our clan? What about "down with The Regime"?
What about biding our time?
Or is this another lesson in inaction—in sparing ourselves from the absolute worst
so that we can barely live? Barely survive?)

(I am confident, Father—you will die by my hand.)
LORE_END

# ── TRANSMISSION KEY 01 ──────────────────────────────────────
# The ritual he performed for his father's survival.
# This string has been rotated. Every printable character shifted.
# Decode it to recover what he did with their blood.

_KEY_01='7=28L(p$w\|*\wp}s$\(x%w\%wtx#\q{~~sN'

# ── TRANSMISSION KEY 02 ──────────────────────────────────────
# His final judgment of his father at the trial.
# Rotated by the same amount. Same cipher. Same key.

_KEY_02='7=28Lr~}uxst}%\*~&\p#t\p\r~(p#sN'

# ─────────────────────────────────────────────────────────────

echo "[ISHTAR] Archive fragment loaded — Nepotistic."
echo "[ISHTAR] Two transmission keys present in this script."
echo "[ISHTAR] The rotation covers all printable characters — not just letters."
echo "[ISHTAR] What did he wash? What did he know?"

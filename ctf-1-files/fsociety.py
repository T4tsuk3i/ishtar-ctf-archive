import base64
import sys
import time

# ==============================
#   F S O C I E T Y   T E R M
# ==============================
# Sometimes the key is off by one.
# Hidden trigger (base64): cmV2b2x1dGlvbg==

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

banner = """
=================================
        F S O C I E T Y
=================================
"""

print(banner)
slow_print("We don't break systems. We break illusions.\n")
slow_print("Initializing secure channel...")
time.sleep(1)
slow_print("Decrypting invitation...\n")

encrypted = "fdwfkph"

shift_value = 2  
keyword = caesar_decrypt(encrypted, shift_value)

expected_sum = 725

if sum(ord(c) for c in keyword) != expected_sum:
    slow_print("Integrity check failed.")
    slow_print("Decryption mismatch detected.")
    slow_print("Maybe the shift value isn't quite right...\n")
    slow_print("Program terminated.")
    sys.exit()

# ---------------- STAGE 1 ----------------

slow_print("Decryption successful.")
slow_print("Trigger word 1 recovered:\n")
slow_print(keyword + "\n")

slow_print("Enter Trigger Word 1 to continue:\n")
user_input = input("> ").strip().lower()

if sum(ord(c) for c in user_input) != expected_sum:
    slow_print("\nIncorrect trigger.")
    slow_print("Connection terminated.")
    sys.exit()

# Build 
flag1_bytes = [83,48,67,123,97,110,97,108,121,115,116,99,97,116,99,104,109,101,125]
raw_flag_1 = "".join(chr(b) for b in flag1_bytes)
encoded_flag_1 = base64.b64encode(raw_flag_1.encode()).decode()

slow_print("\nStage 1 complete.")
slow_print("Flag 1 (encoded):")
print(encoded_flag_1)

# ---------------- STAGE 2 ----------------

slow_print("\nStage 2 unlocked.")
slow_print("Sometimes the answer is hidden in the code itself.\n")

slow_print("Enter Trigger Word 2:\n")
second_input = input("> ").strip().lower()

encoded_trigger = "cmV2b2x1dGlvbg=="
trigger = base64.b64decode(encoded_trigger).decode()

if second_input != trigger:
    slow_print("\nIncorrect trigger.")
    slow_print("Connection terminated.")
    sys.exit()

# Build
flag2_bytes = [83,48,67,123,97,110,97,108,121,115,116,114,101,118,111,108,117,116,105,111,110,125]
raw_flag_2 = "".join(chr(b) for b in flag2_bytes)
encoded_flag_2 = base64.b64encode(raw_flag_2.encode()).decode()

slow_print("\nAccess level elevated.")
slow_print("Flag 2 (encoded):")
print(encoded_flag_2)

slow_print("\nTransmission complete.")
slow_print("Goodbye, friend.")

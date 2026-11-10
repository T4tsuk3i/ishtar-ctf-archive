import base64

KEY = 23

def winnow(data):
	return bytes([b ^ KEY for b in data])

def gardener(data):
    return data[::-1]

def reconstruct():
    encoded = "UFleX0ReRUJYW1FIUl9DSFJDVkVWR1J"
    stage1 = base64.b64decode(encoded)
    stage2 = winnow(stage1)
    stage3 = gardener(stage2)
    return stage3.decode()

if __name__ == "__main__":
    print("Reconstructing ontological structure...")
    print("Recovered principle:", reconstruct())
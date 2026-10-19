alphabets = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

print("--- Uppercase & Lowercase ---")
for alphabet in alphabets:
    upper = alphabet
    lower = alphabet.lower()
    print(f"Uppercase: {upper} | Lowercase: {lower}")

print("\n--- Order & Reverse ---")

reverse = sorted(alphabets, reverse = True)

for index, alphabet in enumerate(alphabets):
    print(f"Order: {alphabet} | Reverse: {reverse[index]}")
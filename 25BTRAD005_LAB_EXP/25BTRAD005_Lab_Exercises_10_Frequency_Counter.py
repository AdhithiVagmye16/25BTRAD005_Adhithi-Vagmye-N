# ============================================================
# Lab Exercise 10: Frequency Counter using Dictionaries
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

sentence = input("Enter a sentence: ").lower()
for ch in ".,!?;:":
    sentence = sentence.replace(ch, "")
words = sentence.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print("\nWord Frequency:")
for w, c in freq.items():
    print(f"{w:<8}: {c}")

# Survey responses stored in a list
responses = ["Pizza", "Burger", "Pizza", "Pasta", "Pizza", "Burger", "Pasta", "Pizza"]
count = {}
for r in responses:
    count[r] = count.get(r, 0) + 1

print("\nSurvey Results (Favourite Food):")
for item, c in count.items():
    print(f"{item:<8}: {c}")
top = max(count, key=count.get)
print(f"Most preferred: {top} ({count[top]} votes)")

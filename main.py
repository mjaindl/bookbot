# main.py

def count_letters(text):
    text = text.lower()
    letter_counts = {}

    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts

file_path = "books/frankenstein.txt"

with open(file_path, "r") as f:
    file_contents = f.read()

word_count = len(file_contents.split())
                 
sentence_count = file_contents.count('.') + file_contents.count('!') + file_contents.count('?')

letter_counts = count_letters(file_contents)

print("=== Full Text ===")
print(file_contents)

print("\n=== Word Count ===")
print(f"{word_count} words found in the document")

print("\n=== Letter Counts ===")
print(f"The 'e' character was found {letter_counts.get('e', 0)} times")
print(f"The 't' character was found {letter_counts.get('t', 0)} times")
print(f"The 'a' character was found {letter_counts.get('a', 0)} times")
# Add similar lines for other letters...

sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

print("\n=== Letter Counts (Sorted) ===")
for letter, count in sorted_letters:
    print(f"The '{letter}' character was found {count} times")

print("\n--- Begin report of", file_path, "---")
print(f"{word_count} words found in the document\n")
for letter, count in sorted_letters:
    print(f"The '{letter}' character was found {count} times")
print("--- End report ---")

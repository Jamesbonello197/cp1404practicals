text = input("Text: ")
words = text.split()


word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word in sorted(word_counts):
    appearances = word_counts[word]
    print(f"{word} : {appearances}")

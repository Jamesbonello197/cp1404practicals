text = input("Text: ")
words = text.split()


word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word in sorted(word_to_count):
    appearances = word_to_count[word]
    longest_word = int(max(len(w) for w in words))
    print(f"{word:<{longest_word}} : {appearances}")


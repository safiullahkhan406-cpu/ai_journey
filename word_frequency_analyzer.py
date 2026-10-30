# Word Frequency Analyzer

import string

# User se sentence lena
text = input("Enter your sentence: ")

# Sentence ko lowercase banana
text = text.lower()

# Punctuation remove karna
for mark in string.punctuation:
    text = text.replace(mark, "")

# Sentence ko words ki list mein convert karna
words = text.split()

# Empty dictionary banana
word_count = {}

# Har word ki frequency count karna
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Words ko frequency ke hisaab se sort karna
sorted_words = sorted(
    word_count.items(),
    key=lambda item: item[1],
    reverse=True
)

# Total words count karna
total_words = len(words)

# Results display karna
print("\n===== WORD FREQUENCY ANALYZER =====")

print("Total Words:", total_words)

print("\nWord Frequency:")

for word, count in sorted_words:
    print(word, ":", count)

# Most repeated word find karna
if sorted_words:
    print("\nMost Repeated Word:", sorted_words[0][0])
    print("Frequency:", sorted_words[0][1])
    
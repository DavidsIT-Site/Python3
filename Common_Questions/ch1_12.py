words = ['look', 'into', 'the', 'dark', 'Light', 'Makes', 'dark', 'impossible', 'don', 't', 'stop', 'stop', 'the', 'dark', 'stop']
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['impossible'])

morewords = ['Hello', 'Worlds', 'the', 'stop']
for word in morewords:
    word_counts[word] += 1
top_three = word_counts.most_common(3)
print(top_three)


# thats c logic. Bad. Pythonic
print(words)
print(morewords)

a = Counter(words)
b = Counter(morewords)
print(b)
print(a)
c = a + b
d = a -b
print(c)
print(d)




"""
CP1404/CP5632 Practical
Count word occurrences
"""

word_to_count = {}

text = input('Text: ')

words = text.split()

# Count the words
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# Sort the words
words = list(word_to_count.keys())
words.sort()

# Print results neatly
max_length = max((len(word) for word in words))
for word in words:
    print(f'{word:{max_length}} : {word_to_count[word]}')


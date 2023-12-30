from collections import defaultdict

words = ["apple", "orange", "avacaodo", "broccoli", "carrot"]

grouped_words = defaultdict(list)

for word in words:
    # gets the first index of the individual word in the words list
    # then appends it to the grouped_words defaultdict formatted as a list for the key's value
    grouped_words[word[0]].append(word)

print(grouped_words)


capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "China": "Bejing",
    "Russia": "Moscow",
}

print(capitals["Russia"])

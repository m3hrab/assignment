msg = '\nThe study titled "Present status and historical changes of urban green space in Dhaka city, '
msg += 'Bangladesh: A remote sensing driven approach" was published in the US-based "Environmental '
msg += 'Challenges" journal in December last year.\n'

# a) Print the characters and its count of the given text.
print(msg)
print("Total Character: " + str(len(msg)))
print("\n")

# b) Print the list of words.
print("List of Words: \n")
print(msg.split())
print("\n")


# c) Sort the word list according to word length (both ascending and descending order).
words = msg.split()
for i in range(1,len(words)):
    key = len(words[i])
    word = words[i]
    # insert word[i] into the sorted sequence word[1,...i-1]
    j = i-1
    while j>-1 and len(words[j])>key:
        words[j+1] = words[j]
        j = j - 1
    print(j)
    words[j+1] = word

print("\n\nHere is the sorted word list:")
print(words)
print("\n\n")

# d) Print the words that occur more than two times only.
special_word = []
for word in words:
    if words.count(word) > 2 and word not in special_word:
        special_word.append(word)

print("Here is the list of words that occurs more than two times:\n")
print(special_word)
print("\n\n")
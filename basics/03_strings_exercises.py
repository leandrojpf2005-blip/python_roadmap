# ------------------
# Basic Indexing
# ------------------

# 1. Given:
text = "Programming"

# a) Print the first character
# b) Print the last character
# c) Print the third character
# d) Print the second-to-last character

print(text[0])
print(text[-1])
print(text[2])
print(text[-2])

# ------------------
# Slicing Practice
# ------------------

# 2. Using only slicing (no loops), produce:

word = "DataScience"

# a) "Data"
# b) "Science"
# c) Reverse the string
# d) Every second character
# e) "cneiSataD"

print(word[0:4])
print(word[4:])
print(word[::-1])
print(word[0::2])
print(word[-2::-1])

# ------------------
# Immutability
# ------------------

# 3. Attempo to change the first letter of:
language = "python"

# a) Observe the error
# b) Correctly produce "Python" without modifying the original string

print(language.capitalize())


# ------------------
# String Methods
# ------------------

# 4. Given:
messy = "   PyTHon iS FuN   "

# a) Remove surrounding whitescape
# b) Convert eveything to lowercase
# c) Convert everything to uppercase
# d) Convert to proper sentence case: "Python is fun"
# e) Replace "FuN" with powerful

print(messy.strip())
print(messy.strip().lower())
print(messy.strip().upper())
print(messy.strip().capitalize())
print(messy.strip().capitalize().replace("fun", "powerful"))
# ------------------
# Searching & Membership
# ------------------

# 5. Given:
sentence = "Python is simple and powerful"

# a) Check if "simple" exists in the string
# b) Find the index of "powerful"
# c) What happens if you try to find "Java" using:
#   - .find()
#   - .index()

print("simple" in sentence)
print(sentence.index("powerful"))
#if we use .index() with a word that doenst exist it will return an ERROR, while .find() will return -1

# ------------------
# Splitting & Joining
# ------------------

# 6. Given:
phrase = "Learn Python step by step"

# a) Convert the string into a list of words
# b) Join the words using "-"
# c) Join the words using "|"

listaa = phrase.split(' ')
print(listaa)
frase = "-".join(listaa)
print(frase)
frase2 = "|".join(listaa)
print(frase2)


# ------------------
# String Formatting
# ------------------

# 7. Given:
name = "Joao"
score = 95

# Produce the string: "Joao scored 95% on the exam":
# a) Using concatenation
# b) Using .format()
# c) Using f-strings

exercise7_frase = name + ' scored ' + str(score) + '%' + ' on the exam'
print(exercise7_frase)

exercise7_fraseB = "{} scored {}% on the exam".format(name, score)
print(exercise7_fraseB)

exercise7_fraseC = f'{name} scored {score}% on the exam'
print(exercise7_fraseC)


# ------------------
# Unicode & Encoding
# ------------------

# 8. Given:
word = "café"

# a) Print the number of characters
# b) Print the number of bytes in UTF-8 encoding
# c) Explain why they differ

print(len(word))
print(len(word.encode('utf-8')))
#len() counts the visible characters as 1 while in utf-8 counts how many bytes are there

# ------------------
# Identity vs Equality
# ------------------

# 9. Create two identical strings with the same value.

string1 = 'Identidade vs Equalidade'
string2 = 'Identidade vs Equalidade'

# Check:
# a) ==
# b) is
# Explain the difference between value equality and identity

print(string1 == string2)
print(string1 is string2)
#equality cares about the value while identity cares his memory location

# ------------------
# Advanced: String Behaviour
# ------------------

# 10. What will this print? Explain why.

def shout(text):
    text.upper()
    return text

print(shout("hello"))
#it will print 'hello' in lowercase because .upper() returns a new string but does not modify the original one, and since the function returns the original text the uppercase is ignored

# ------------------
# Performance Awareness
# ------------------

# 11. Why is this inefficient?

result = []
for i in range(1000):
    result.append('a')
#so the function is inefficient because it creates a large amount of strings that are useless and will need more storage, instead we could use a list type to store all a characters.

# Rewrite it using a more efficient approach


# ------------------
# Bonus Challenge
# ------------------

# 12. Given:
text = "  Data Types in PYTHON   "
# Produce exactly:
# "data-types-in-python"

# Constraints:
# - Remove extra whitespace
# - Convert to lowercase
# - Replace spaces with "-"
# - Do it in a clean chain of methods (one expression)

print(text.strip().lower().replace(" ", "-"))

# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    return word[1:] + word[0] + "ay"
print(pig_latin("banana"))   # returns "ananabay"
print(pig_latin("python"))   # returns "ythonpay"
print(pig_latin("apple"))    # returns "appleway"


def word_lengths(sentence):
    lengths = []
    for word in sentence.split():
        lengths.append(len(word))
    return lengths
print(word_lengths("the quick brown fox"))   # returns [3, 5, 5, 3]
print(word_lengths("hello"))                 # returns [5]
print(word_lengths(""))                      # returns []


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
print(reverse_words("the quick brown fox"))   # returns "fox brown quick the"
print(reverse_words("hello"))                 # returns "hello"
print(reverse_words("a b c"))                 # returns "c b a"


def letter_counts(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts
print(letter_counts("hello"))         # returns {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(letter_counts("Mississippi"))   # returns {'m': 1, 'i': 4, 's': 4, 'p': 2}
print(letter_counts("a a a"))         # returns {'a': 3}


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # print(pig_latin("banana"))                    # ananabay
    # print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    # print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()

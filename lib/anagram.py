# your code goes here!

#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)
        # Initialize an empty list to store matching anagrams
        matches = []
        # Iterate over each word in the provided word list
        for word in word_list:
            # If the sorted letters of the current word match the sorted original word, it is an anagram
            if sorted(word) == sorted_word:
                matches.append(word)
        # Return the list of matching anagrams
        return matches

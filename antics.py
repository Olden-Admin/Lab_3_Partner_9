# CIS-117 Lab3
# Write a description of your module here
# Group 9
# Angela Wu, Kiyale Olden, Yasi Yavari-Behrouz 

def is_abecedarian(word_in):
    """Return True if the letters in word_in are in alphabetical order, False otherwise."""
    word = word_in.lower()
    previous = word[0]
    for i in word:
        if i < previous:
            return False
        previous = i
    return True

def is_dobloon(word):
   """Return True if word is a doobloon, False otherwise."""
   for i in word:
      count = 1
      for j in word[1:]:
         if i == j:
            count += 1
            if count > 2:
               return False
      if count == 1:
         return False
   return True
    
def is_isogram(word):
    letter_counts = {}

    for letter in word:
        if letter in letter_counts:
            return False
        else:
            letter_counts[letter] = 1
    return True

def is_pangram(sentence):
   """Return True if sentence is a pangram, False otherwise."""
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   for char in alphabet:
       if char not in sentence.lower():
           return False
              
def is_pangram(sentence):
         """Return True if sentence is a pangram, False otherwise."""
         alphabet = 'abcdefghijklmnopqrstuvwxyz'
         for char in alphabet:
            if char not in sentence.lower():
               return False
         return True

def is_palindrome(word):
   """Return True if word is a palindrome, False otherwise."""
   return word == word[::-1]

def is_tautogram(text):
    words = text.split()
    first_letter = words[0][0].lower()

    for word in words:
        if word[0].lower() != first_letter:
            return False
    return True
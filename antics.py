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
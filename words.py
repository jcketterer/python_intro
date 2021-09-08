def print_upper_words(words):
  """this will take the the words in the list and make them all uppercase"""
  for word in words: 
    print(word.upper())

def print_upper_words2(words):
  """prints out only words that start with the letter "e" """

  for word in words:
    if word.startswith('e') or word.startswith('E'):
      print(word.upper())

def print_upper_words3(words, starts_with):
  """prints words that start with one of the given letters"""

  for word in words: 
    for letter in starts_with:
      if word.startswith(letter):
        print(word.upper())
        break



print_upper_words(["hello", "hey", "goodbye", "yo", "yes","ello!"])
print_upper_words2(["hello", "hey", "goodbye", "yo", "yes","ello!"])
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes","ello!"], starts_with=('e','g'))
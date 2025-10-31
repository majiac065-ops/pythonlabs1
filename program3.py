def get_vowels_list(word):
  """
  Extracts all vowels from a given word using a list comprehension.

  Args:
    word: The input string.

  Returns:
    A list containing all the vowels found in the word.
  """
  vowels = 'aeiou'
  return [char for char in word.lower() if char in vowels]


word = "hy maji"
vowel_list = get_vowels_list(word)
print(f"The word is: '{word}'")
print(f"The vowels are: {vowel_list}")

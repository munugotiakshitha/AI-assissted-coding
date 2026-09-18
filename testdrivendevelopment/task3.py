def run_tests():
	# Required test cases
	assert is_anagram("listen", "silent") == True
	assert is_anagram("hello", "world") == False
	assert is_anagram("Dormitory", "Dirty Room") == True

	# Edge-case tests
	assert is_anagram("", "") == True
	assert is_anagram("python", "python") == True
	assert is_anagram("The eyes!", "They see") == True


def is_anagram(str1, str2):
	# Keep letters and numbers, ignore case, spaces, and punctuation.
	cleaned_str1 = "".join(character.lower() for character in str1 if character.isalnum())
	cleaned_str2 = "".join(character.lower() for character in str2 if character.isalnum())

	# Anagrams contain the same characters in a different order.
	return sorted(cleaned_str1) == sorted(cleaned_str2)


run_tests()
print("All Task 3 tests passed!")

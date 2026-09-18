def run_tests():
	# Required test cases
	assert is_strong_password("Abcd@123") == True
	assert is_strong_password("abcd123") == False
	assert is_strong_password("ABCD@1234") == False

	# Edge-case tests
	assert is_strong_password("Abc@123 ") == False  # Contains a space
	assert is_strong_password("Abc@1234") == True  # Exactly 8 characters


def is_strong_password(password):
	# Check each password-strength requirement.
	if len(password) < 8 or " " in password:
		return False

	has_uppercase = any(character.isupper() for character in password)
	has_lowercase = any(character.islower() for character in password)
	has_digit = any(character.isdigit() for character in password)
	has_special_character = any(
		not character.isalnum() and character != " " for character in password
	)

	return (
		has_uppercase
		and has_lowercase
		and has_digit
		and has_special_character
	)


run_tests()
print("All Task 1 tests passed!")

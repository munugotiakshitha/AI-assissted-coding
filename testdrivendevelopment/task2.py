def run_tests():
	# Required test cases
	assert classify_number(10) == "Positive"
	assert classify_number(-5) == "Negative"
	assert classify_number(0) == "Zero"

	# Boundary and invalid-input tests
	assert classify_number(1) == "Positive"
	assert classify_number(-1) == "Negative"
	assert classify_number("10") == "Invalid"
	assert classify_number(None) == "Invalid"


def classify_number(n):
	# Only integers and decimal numbers are valid inputs.
	if not isinstance(n, (int, float)) or isinstance(n, bool):
		return "Invalid"

	# Check the number against each possible classification.
	classifications = [
		(n > 0, "Positive"),
		(n < 0, "Negative"),
		(n == 0, "Zero"),
	]

	for condition, result in classifications:
		if condition:
			return result

	return "Invalid"


run_tests()
print("All Task 2 tests passed!")

# Prompt
# Fix this Python program so that it safely handles a missing file:
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

print(read_file("nonexistent.txt"))
# Corrected Code
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except OSError:
        return "Error: Invalid file path."


print(read_file("nonexistent.txt"))
# # Output for Missing File
# Error: File not found.
# 3 Test Scenarios

# 1. File exists

# Input: test.txt
# Output: Contents of the file

# 2. File is missing

# Input: nonexistent.txt
# Output: Error: File not found.

# 3. Invalid path

# Input: invalid/path/test.txt
# Output: Error: Invalid file path.
# Explanation

# try-except prevents the program from crashing. FileNotFoundError handles a missing file, while OSError handles other file/path-related errors.
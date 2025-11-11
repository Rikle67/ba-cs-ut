# test_functions.py

from functions import is_valid_score
# --- Tests for is_valid_score ---
print("Running Tests for Tests for is_valid_score()")

# Test 1: Valid score (Expected: True)
print("Running Test 1...")
assert is_valid_score(75) == True, "Test 1 Failed: Valid score check failed."
print("Test 1 Passed.")

# Test 2: Maximum valid score (Expected: True)
print("Running Test 2...")
assert is_valid_score(100) == True, "Test 2 Failed: Boundary test for 100 failed."
print("Test 2 Passed.")

# Test 3: Minimum valid score (Expected: True)
print("Running Test 3...")
assert is_valid_score(0) == True, "Test 3 Failed: Boundary test for 0 failed."
print("Test 3 Passed.")

# Test 4: Invalid negative score (Expected: False)
print("Running Test 4...")
assert is_valid_score(-5) == False, "Test 4 Failed: Negative number check failed."
print("Test 4 Passed.")

print("\n--- Testing Complete ---")
print("If you see this message and no 'AssertionError' messages, your functions are correct!")
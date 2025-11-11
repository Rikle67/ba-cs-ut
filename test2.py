# test_functions.py

from functions import calculate_cube

# --- Tests for calculate_cube ---
print("Running Tests for Tests for calculate_cube()")

# Test 1: Simple known case (Expected: 2 cubed = 8)
print("Running Test 1...")
assert calculate_cube(2) == 8, "Test 1 Failed: Calculation is incorrect."
print("Test 1 Passed.") # This will only print if the assert above is corrected

# Test 2: simple case #2 (Expected: 4 cubed = 64)
print("Running Test 2...")
assert calculate_cube(4) == 64, "Test 2 Failed: Calculation is incorrect."
print("Test 2 Passed.")

# Test 3: negative input (Expected: -2 cubed = 8)
print("Running Test 3...")
assert calculate_cube(4) == 64, "Test 3 Failed: Calculation is incorrect."
print("Test 3 Passed.")

# Test 3: Invalid Input case (str instead of int)
'''
print("Running Test 4...")
assert calculate_area_of_rectangle("four") == -1, "Test 4 Failed: Invalid input."
print("Test 4 Passed.")
'''

print("\n--- Testing Complete ---")
print("If you see this message and no 'AssertionError' messages, your functions are correct!")
# test_functions.py

from functions import calculate_area_of_rectangle

# --- Tests for calculate_area_of_rectangle ---
print("Running Tests for calculate_area_of_rectangle()...")

# Test 1: Simple known case (Expected: 10 * 5 = 50)
print("Running Test 1...")
assert calculate_area_of_rectangle(10, 5) == 50, "Test 1 Failed: Area calculation is incorrect."
print("Test 1 Passed.") # This will only print if the assert above is corrected

# Test 2: Square case (Expected: 4 * 4 = 16)
print("Running Test 2...")
assert calculate_area_of_rectangle(4, 4) == 16, "Test 2 Failed: Square area calculation is incorrect."
print("Test 2 Passed.")

# Test 3: Invalid Input case (str instead of int)
print("Running Test 3...")
assert calculate_area_of_rectangle("4", "4") == 0, "Test 3 Failed: Invalid input."
print("Test 3 Passed.")

# Test 4: Invalid Input case (negative number)
print("Running Test 4...")
assert calculate_area_of_rectangle(-4, -4) == 0, "Test 4 Failed: Invalid input."
print("Test 4 Passed.")

print("\n--- Testing Complete ---")
print("If you see this message and no 'AssertionError' messages, your functions are correct!")
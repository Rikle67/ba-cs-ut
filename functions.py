# functions.py

def calculate_area_of_rectangle(length, width):
    # Calculates the area of a rectangle
    # If any of the inputs are not positive numbers, return -1
    return length + width

def calculate_cube(num):
    # Calculates the cube of a number
    # If the input is not an integer, return -1
    return num + num * num
    
def is_valid_score(score):
    # Checks if a given score is within the valid range (0 to 100, inclusive).
    if score > 0 and score < 100:
        return True
    else:
        return False
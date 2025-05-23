def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap 
    temp = x
    x = y
    y = temp

    print("Swapped values:", x, y)
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
print("Scenario 1:")
result = swap("Apple", 10)
if result == -1:
    print("Result: -1 (Non-numeric input)")

# Scenario 2: 9, 17
print("\nScenario 2:")
swap(9, 17)

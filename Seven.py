def div_by_seven(num):
    return num % 7 == 0  # Return True if num is divisible by 7

def squares_of_numbers(n):
    # Iterate through numbers 1 to n
    for num in range(1, n + 1):
        if div_by_seven(num):  # Check if the number is divisible by 7
            print(num)  # Print the number if it is divisible by 7

# Call the function to check numbers from 1 to 300
squares_of_numbers(300)


def sum_of_squares(start, end):
    """
    Calculate the sum of squares of integers in the specified range.
    
    >>> sum_of_squares(1, 5)
    55
    >>> sum_of_squares(3, 3)
    9
    >>> sum_of_squares(0, 0)
    0
    >>> sum_of_squares(1, 10)
    385
    """
    total = 0
    for num in range(start, end + 1):
        total += num ** 2  # or total += num * num
    return total

# Main program
if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    result = sum_of_squares(start, end)
    print(f"The sum of squares from {start} to {end} is {result}.")
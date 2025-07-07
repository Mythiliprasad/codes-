def count_digit_in_number(N, D):
    # Convert N to a string to easily count the occurrences of D
    return str(N).count(str(D))

# Input from user
N = int(input("Enter an integer N: "))
D = int(input("Enter a single-digit number D: "))

# Validate D to be a single-digit number
if D < 0 or D > 9:
    print("Please enter a valid single-digit number for D (0-9).")
else:
    count = count_digit_in_number(N, D)
    print(f"The digit {D} appears {count} times in {N}.")

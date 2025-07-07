# Function to print vowels in a given string
def print_vowels(s):
    vowels = "aeiouAEIOU"  # Consider both lowercase and uppercase vowels
    vowels_in_string = [char for char in s if char in vowels]
    return ''.join(vowels_in_string)

# Input from the user
s = input("Enter a string: ")

# Printing the vowels present in the string
vowels_in_s = print_vowels(s)
print(f"The vowels in the string are: {vowels_in_s}")

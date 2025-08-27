"""
question -1 : Write a Python program to reverse a string without using built-in functions.
"""
# # NAIVE ONE
# def reversal(str1):
#     rstr1=""
#     for i in range(len(str1),0,-1):
#         rstr1+=str1[i-1]
#     return rstr1
# str1=input("Enter a string: ")
# print("The original string is: ",str1)
# print("The reversed string is: ",reversal(str1))



# optimal one
def reverse_string(s: str) -> str:
    # Convert string to list (since strings are immutable in Python)
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Join list back to string
    return "".join(chars)

# Example
text = "DataEngineer"
print("Original:", text)
print("Reversed:", reverse_string(text))

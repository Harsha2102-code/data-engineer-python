# Implement a function to check if a string is a palindrome
def check_palindrome(st1):
    # st1=st1.lower()
    st1 = ''.join(ch.lower() for ch in st1 if ch.isalnum()) # Normalize the string
    print(st1)
    left,right=0,len(st1)-1
    while left<=right:
        if st1[left]==st1[right]:
            left+=1
            right-=1
            continue
        else:
            return False
    return True
st1=input("enter string:")
if check_palindrome(st1):
    print("Yes!! its a palindrome")
else:
    print ("No!! itsnot a palindrome")
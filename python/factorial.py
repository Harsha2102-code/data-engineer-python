#  Implement a function to find the factorial of a number using recursion.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        # 3*factorial(2)
        # 3*2*factorial(1)
        # 3*2*1
    
num=int(input("enter number to find factorial:"))
print(factorial(num))

#  Write a Python program to count the frequency of each character in a string.
# 
def frequency(st1):
    st1=st1.lower()
    freq={}
    for i in st1:
        if i.isalnum() :
            freq[i]=freq.get(i,0)+1
    print(freq)
st1=input("Enter string:")
frequency(st1)
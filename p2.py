# Check weather string is Plainrome or not
# Plainrome is a string which is same when read from left to right and right to left
# Example: "madam" is plainrome, "madam" is not plainrome
# Input: "madam"
# Output: True
def isPlainrome(s):
    return s == s[::-1]
s=input("Enter a String to check: ")
print(isPlainrome(s))


# Sum of digit entered by user
# Input: 1234
# Output: 10
def sumOfDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
n=int(input("Enter a number: "))
print(sumOfDigit(n))



# Give Simple problem statemaent as above programs
# Write a program to check whether a given number is a prime number or not
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n=int(input("Enter a number: "))
print(isPrime(n))


# Find vowels in string
# Input: "madam"
# Output: a, a, a, m, m
def findVowels(s):
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            print(i, end=" ")
s=input("Enter a String: ")
findVowels(s)


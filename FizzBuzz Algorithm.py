"""
If the integer (n) is divisible by 3, the output must be replaced by “Fizz”.
If the integer (n) is divisible by 5, the output must be replaced by “Buzz”.
If the integer (n) is divisible by 3 and 5, the output should be replaced by “FizzBuzz”.
"""

def FizzBuzz(n):
    if not n%3 and not n%5:
        print("FizzBuzz")
    elif not n%3:
        print("Fizz")
    elif not n%5:
        print("Buzz")
    else:
        print(n)

n=int(input("Enter the integer number: "))
FizzBuzz(n)
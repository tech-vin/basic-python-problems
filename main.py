'''
Reverse a String
Write a function reverse_str(s: str) -> str that returns the reverse of the input string.
'''

def reverseString(string):
    new_string = ''
    for ch in string:
        new_string = ch + new_string
    return new_string
    
'''
Palindrome Checker
Implement is_palindrome(s: str) -> bool that returns True if s is a palindrome (ignoring case and non-alphanumeric characters).
'''
def isPalindrome(string):
    temp = string
    result = reverseString(temp)
    return result == string

testcases = ["vineet", "priya", "chunniya", "maam"]

print([reverseString(i) for i in testcases])
print([isPalindrome(i) for i in testcases])



'''
Factorial (Loop & Recursion)
Loop version: fact_loop(n: int) -> int
Recursive version: fact_rec(n: int) -> int
Compare their time and space complexities.
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


def factUsingLoop(num):
    result = 1
    for n in range(1, num + 1):
        result = n * result
    return result

def factUsingRec(num):
    if num == 1 or num <= 0:
        return 1
    return num * factUsingRec(num - 1)

testcases = [5, 1, -1, 0, 6]

print([factUsingLoop(i) for i in testcases])
print([factUsingRec(i) for i in testcases])

'''
All Positive?
Given a list of numbers, use the all() built-in to check if all elements are positive.
'''
def checkPositive(num):
    return all(n > 0 for n in num)

testcases = [[1, 1, 2, 4], [1, 0, 1, 1]]
print([checkPositive(i) for i in testcases])
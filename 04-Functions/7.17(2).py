palindrome='rader'

def f(palindrome):
    if palindrome==palindrome[::-1]:
        return True
    return False

print(f(palindrome))
num = input("What is your number? ")

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome(num))

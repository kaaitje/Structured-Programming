def palindrome(string1):
    if string1 == string1[::-1]:
        return string1 + ' is a palindrome.'
    else:
        return string1 + ' is not a palindrome.'


x = 'radar'
print(palindrome(x))
x = 'palindrome'
print(palindrome(x))


def my_palindrome(string1):
    # If nothing is left it means its a palindrome
    if len(string1) < 2:
        return 'It is a palindrome'
    # compares first and last letter
    if string1[0] != string1[-1]:
        return 'It is not a palindrome'
    # calls its self until its less than 2
    return my_palindrome(string1[1:-1])


x = 'radar'
print(my_palindrome(x))
x = 'palindrome'
print(my_palindrome(x))

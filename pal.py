


def is_palindrome(s):
    reversed_s = s[::-1]
    print(f"Reversed String: {reversed_s}")
    if s == reversed_s:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

user_input=input("enter the string: ")
is_palindrome(user_input)


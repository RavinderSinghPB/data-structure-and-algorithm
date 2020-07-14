""" Read
Given a string, check if it can be rotated to form a palindrome.
"""


def isPalindrome(string):
    # Start from leftmost and rightmost corners of str
    l = 0
    h = len(string) - 1

    # Keep comparing characters while they are same
    while h > l:
        l += 1
        h -= 1
        if string[l - 1] != string[h + 1]:
            return False

    # If we reach here, then all characters were matching
    return True


# Function to check if a given string is a rotation of a
# palindrome.
def isRotatedPalindrome(string):
    # If string itself is palindrome
    if isPalindrome(string):
        return True

    # Now try all rotations one by one
    n = len(string)
    for i in range(n - 1):
        string1 = string[i + 1:n]
        string2 = string[0:i + 1]

        # Check if this rotation is palindrome
        string1 += string2
        if isPalindrome(string1):
            return True

    return False


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        str = input()

        if isRotatedPalindrome(str):
            print(1)
        else:
            print(0)

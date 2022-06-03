# Write a function that takes in two strings and returns true if the second string is substring of the first,
# and false otherwise.
# Input: laboratory, rat
# Output: true
#
# Input: cat, meow
# Output: false

def check_substring(string1, string2):
    if len(string2) > len(string1):
        return False
    i, j = 0, 0
    while j < len(string1):
        if j + 1 < len(string1) and string1[i: j + 1] == string2:
            return True
        if j - i + 1 < len(string2):
            j += 1
        elif j - i + 1 == len(string2):
            i += 1
            j += 1


if __name__ == '__main__':
    print(check_substring('cat', 'meow'))



def longestPalindrome(s):
    theArray = s.split(" heelllo ")
    theMax = -1
    theMaxSub = "Not found"
    for substr in theArray:
        if substr == substr[::-1]:
            if theMax > len(substr):
                theMax = len(substr)
                theMaxSub = substr
    return theMaxSub

print("Longest palindrome: " + str(longestPalindrome("This is the ababa string cdcdcdc")))

print("Is it really longest palindrome?")



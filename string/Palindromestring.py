def isPalindrome(s):
    left = 0  # left starts at the beginning of the string 
    right = len(s) - 1 # right starts at the end of the string.
    while left < right: 
        #isalnjum check if the character is alphanumeric (letter or digit)
        if not s[left].isalnum():
            left += 1  #if left is not alphanumeric, move teh lft pointer one strp to the right 
        elif not s[right].isalnum(): #if right is not alphanumeric , move the right pointer one step to the left.
            right -=1
        # convert the left and right to lower
        elif s[left].lower() != s[right].lower():
            return False # if not equal return False.
        else: 
            left +=1 # if character match , move left one step right 
            right -=1 #right one step left to continue comparing to next pair of characters. 
    return True #If the loop completes without finding a mismatch, return True, indicating the string is a palindrome.

if __name__ == "__main__":   
    str = "ABCCBA"
    ans = isPalindrome(str)

    if ans == True:       
        print("palindrome")
    else: 
        print("not palindrome")           
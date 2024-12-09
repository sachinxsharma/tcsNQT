# check if numbe is palindrome or not 
# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

# alogrithm :
'''
We then compare the reversed number with 
the original number. If they are equal, the original number is a palindrome. If they are not equal the original number is not a palindrome.

alogithm :
step 1 - initalize an integrer revNum to 0. this variable store the reverse of the number.
step 2 - Make a duplicate of the original number and store it in an integer dup for later comparison.
step 3 -  Run a while loop with the condition n>0 to reverse the number and at each iteration:
et the last digit of n by using the modulus operator % with 10 and store it in a temporary variable ld.
Update the revNum by multiplying it by 10 and adding the last digit ld.
Update n by integer division with 10 effectively removing the last digit.
Step 4: After the loop, check if the original number dup is equal to the reversed number revNum.

If they are equal, return true indicating the number is a palindrome.
If they are not equal, return false indicating that the number is not a palindrome.


'''
# code 
def palindrome(n):
    revNum = 0
    # craete a duplicate variable to store a original num
    dup = n

    # iterate through the each digiit off number untill it become 0
    while n > 0:
        lastdigit = n % 10
        revNum = (revNum * 10 ) + lastdigit
        n = n // 10
    # check if original number is  equal to reverse
    if dup == revNum:
        return True
    else:
        return False

def main():
    number = 4554

    if palindrome(number):
        print(number , "is a palindrom")
    else: 
        print(number, "is not palindrome.")

if __name__ == "__main__":
    main()                    
    
def checkPalindrome(num):
    rev = 0
    temp = num
    while (num != 0):
        rev = (rev * 10) + (num % 10)
        num = num // 10
    if rev == temp:
        return True

num = int(input())
isPalindrome = checkPalindrome(num)
if isPalindrome:
    print("true")
else:
    print("false")

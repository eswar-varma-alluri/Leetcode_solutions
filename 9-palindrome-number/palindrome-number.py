
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        xx=x
        if x<0:
            return False
        s=0
        while xx>0:
            p=xx%10
            s=s*10+p
            xx=xx//10
        if s==x or x==0:
            return True
        else :
            return False

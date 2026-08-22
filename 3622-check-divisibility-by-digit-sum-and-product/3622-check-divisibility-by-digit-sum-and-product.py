class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        k=n
        if n<10:
            return False
        while n!=0:
            l=n%10
            s+=l
            p*=l
            n=n//10
        if k%(s+p)==0:
            return True
        else:
            return False
        
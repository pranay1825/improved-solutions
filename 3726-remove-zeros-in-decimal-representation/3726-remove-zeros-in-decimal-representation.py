class Solution:
    def removeZeros(self, n: int) -> int:
        n=str(n)
        s=""
        for i in n:
            if i!='0':
                s+=i
        return int(s)
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if k not in nums:
            return k
        maxi=0
        for num in nums:
            if num>maxi:
                maxi=num
        for i in range(1,maxi+2):
            ans=k*i
            if ans not in nums:
                return ans
                
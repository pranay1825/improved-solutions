class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        averages=set()
        while len(nums)!=0:
            maxi=max(nums)
            mini=min(nums)
            idx1=nums.index(maxi)
            idx2=nums.index(mini)
            if idx1>idx2:
                nums.pop(idx1)
                nums.pop(idx2)
            else:
                nums.pop(idx2)
                nums.pop(idx1)
            averages.add((maxi+mini)/2)
        return len(averages)
            

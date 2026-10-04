class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=[]
        while len(nums)!=0:
            mini=min(nums)
            idx1=nums.index(mini)
            maxi=max(nums)
            idx2=nums.index(maxi)
            if idx1>idx2:
                nums.pop(idx1)
                nums.pop(idx2)
            else:
                nums.pop(idx2)
                nums.pop(idx1)
            averages.append((mini+maxi)/2)
        return min(averages)


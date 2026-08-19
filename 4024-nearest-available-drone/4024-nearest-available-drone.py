class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        dic={}
        ans=0
        minimum=float('inf')
        for i in range(len(drones)):
            distance=0
            for j in range(len(drones[i])-1):
                distance+=abs(drones[i][j]-target[j])
            if distance<=drones[i][-1]:
                dic[i]=distance
        if dic=={}:
            return -1
        for key,value in dic.items():
            if value<minimum:
                minimum=value
                ans=key
        return ans




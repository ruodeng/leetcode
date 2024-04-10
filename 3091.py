class Solution:
    minStep = float('inf')
    def minOperations(self, k: int) -> int:
        j = k
        m = float('inf')
        while j > 0:
            i=0
            while i < k/j+1:
                if (i+1)*j >= k:
                    if i+j-1 < m:
                        m = i+j-1
                i += 1
            j -=1
        return m

    # def minOperations(self, k: int) -> int:
    #     nums=[1]
    #     mem={}
    #     def dfs(nums,step):
    #         if step >= self.minStep:
    #             return float('inf')
    #         if nums is None:
    #             return float('inf')
    #         if tuple(nums) in mem:
    #             return mem[tuple(nums)]
    #
    #         if sum(nums) >= k:
    #             return step
    #         # pick num in nums, then switch
    #         ans=[]
    #         ans.append(dfs(nums+[nums[0]],step+1))
    #         ans.append(dfs([nums[0]+1]+nums[1:],step+1))
    #         # for i in range(len(nums)):
    #         #     ans.append(dfs(nums+[nums[i]], step + 1))
    #         #     ans.append(dfs(nums[:i]+[nums[i]+1]+nums[i+1:],step+1))
    #         m =  min(ans)
    #         mem[tuple(nums)] = m
    #         self.minStep = min(self.minStep,m)
    #         return m
    #     return dfs(nums,0)
s = Solution()
print(s.minOperations(79))
print(s.minOperations(30))
print(s.minOperations(11))
print(s.minOperations(3))
print(s.minOperations(2))
print(s.minOperations(1))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)

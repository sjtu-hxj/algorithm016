class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums, trace):
            if not nums:
                res.append(trace)
            visited = set()
            for i in range(len(nums)):
                if nums[i] in visited: continue
                backtrace(nums[:i] + nums[i + 1:], trace + [nums[i]])
                visited.add(nums[i])

        res = []
        backtrace(nums, [])
        return res

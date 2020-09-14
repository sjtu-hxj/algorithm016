class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


        # for n in nums[:]:
        #     if nums.count(n) > 1:
        #         nums.remove(n)
        # return len(nums)
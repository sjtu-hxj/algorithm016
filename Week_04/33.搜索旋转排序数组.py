class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:  # 如果中间值是目标，直接返回
                return mid
            if nums[mid] < nums[right]:  # 证明 mid 到 right 之间是升序的
                if nums[mid] < target <= nums[right]:  # 如果 target 在这个升序区间内
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 即nums[mid]>nums[right]的情况，因为各元素不同，因为 nums 是升序序列旋转得到，所以旋转点左右依然有序
                # nums[right] 肯定是某一段的最大值，nums[mid]>nums[right]代表旋转点在mid右侧，也就是说mid左侧现在是有序的
                if nums[left] <= target < nums[mid]:  # 如果target在左侧有序区间
                    right = mid - 1
                else:
                    left = mid + 1
        return left if nums[left] == target else -1
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row , col = len(matrix) , len(matrix[0])
        res = float("-inf")
        for left in range(col):
            sums = [0] * row
            for right in range(left,col):
                for j in range(row):
                    sums[j] += matrix[j][right]
                lst = [0]
                cur = 0
                for num in sums:
                    cur += num
                    loc = bisect.bisect_left(lst,cur-k)
                    if loc < len(lst):
                        res = max(cur-lst[loc],res)
                    bisect.insort(lst,cur)
        return res
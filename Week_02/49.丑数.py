# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         uglys = [1]
#         a, b, c = 0, 0, 0
#         for i in range(n-1):
#           newugly = min(uglys[a] * 2, uglys[b] * 3, uglys[c] * 5)
#           uglys.append(newugly)

#           if newugly == uglys[a] * 2: a += 1
#           if newugly == uglys[b] * 3: b += 1
#           if newugly == uglys[c] * 5: c += 1
#         return uglys[-1]
class Ugly:
    def __init__(self):
        seen = {1, }
        hp = []
        heapq.heappush(hp, 1)
        self.nums = []
        for _ in range(1690):
            cur_ugly = heapq.heappop(hp)
            self.nums.append(cur_ugly)
            for i in [2, 3, 5]:
                new = cur_ugly * i
                if new not in seen:
                    seen.add(new)
                    heapq.heappush(hp, new)


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n - 1]
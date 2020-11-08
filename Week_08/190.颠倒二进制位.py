#    用annaconda跑一下，看一下各个环节的输出

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32)[::-1]:
            ret = ret | (((n >> (31 - i)) & 1) << i)
        return ret
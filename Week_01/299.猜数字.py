import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        print("hello2")
        A = sum(s == g for s, g in zip(secret, guess))
        B = sum((collections.Counter(secret) & collections.Counter(guess)).values()) - A  ##取交集 key取交，value取小
        print("hello2")
        print(collections.Counter(secret) & collections.Counter(guess))
        return "{A}A{B}B".format(A=A, B=B)


a = Solution()
print("hello1")
print(a.getHint("1807", "7810"))
print("hello3")

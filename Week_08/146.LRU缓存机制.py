from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self: return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)
        if len(self) > self.size:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
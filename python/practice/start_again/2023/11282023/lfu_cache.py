# #   https://leetcode.com/problems/lfu-cache/ ( Last Frequency Used Key)
# 460. LFU Cache
# Hard
# 5.4K
# 321
# Companies
# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[4,3], cnt(4)=2, cnt(3)=3
 
from collections import defaultdict, deque, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._items = defaultdict(int)
        self._freqs = defaultdict(OrderedDict)
        self._minFreq=0
    def _update_freq( self, key: int, value: int = None) -> int:
        freq=self._items[key]
        v=self._freqs[freq].pop(key)
        if value is not None:
            v=value
        self._freqs[freq + 1][key] = v
        self._items[key] +=1
        if self._minFreq == freq:
            self._minFreq +=1
        return v
    def get (self, key: int )-> int:
        if key not in self._items:
            return -1 
        return self._update_freq(key)
    
    def put (self, key: int, value: int ) -> None:
        if not self.capacity:
            return 
        if key in self._items:
            self._update_freq(key, value)
        else:
            if len(self._items) == self.capacity:
                self._items.pop(self._freqs[self._minFreq].popitem(last=False)[0])
            self._minFreq = 1
            self._items[key] = 1
            self._freqs[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
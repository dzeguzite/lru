import time


class Lru:

    def __init__(self, size):
        self._size = size
        self._keyvalue = {}
        self._tskey = {}

    def put(self, item):
        # print(item.keys())
        currenttime = time.time()
        if list(item.keys())[0] in list(self._keyvalue.keys()):
            del self._keyvalue[list(item.keys())[0]]
            for kk, vl in self._tskey.items():
                if vl == list(item.keys())[0]:
                    del self._tskey[kk]
                    break
        self._keyvalue[list(item.keys())[0]] = list(item.values())[0]
        self._tskey[currenttime] = list(item.keys())[0]

        if len(self._keyvalue) > self._size:
            oldest = list(self._tskey.keys())
            oldest.sort()
            del self._keyvalue[self._tskey[oldest[0]]]
            del self._tskey[oldest[0]]

    def get(self, key):
        currenttime = time.time()
        print(currenttime)
        for i, j in self._tskey.items():
            print(i, j)
            if j == key:
                self._tskey[currenttime] = j
                del self._tskey[i]
                return self._keyvalue[j]


    def print(self):
        print(f"Size: {self._size}")
        print(f"Key-Value Dictionary: {self._keyvalue}")
        print(f"TimeStamp - key Dictionary: {self._tskey}")

mylru = Lru(3);

mylru.put({"a": "aaa"})
mylru.put({"b": "bbb"})
mylru.put({"a": "aab"})
mylru.put({"c": "ddd"})
print(mylru.get("a"))
mylru.put({"d": "ddd"})
mylru.put({"b": "bba"})
print(mylru.get("d"))
mylru.put({"c": "ccd"})
mylru.put({"a": "aee"})




mylru.print()


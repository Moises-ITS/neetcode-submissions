class TimeMap:

    def __init__(self):
        self.storage = {} #{key: [value, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        #want to keep in order
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        #binary search in here
        res, values = "", self.storage.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values [m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

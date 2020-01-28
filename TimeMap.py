class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_ls = []
        self.val_ls = []
        self.timestamp_ls = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_ls.append(key)
        self.val_ls.append(value)
        self.timestamp_ls.append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key_ls:
            i = len(self.key_ls) - 1
            while i > -1:
                if self.key_ls[i] == key:
                    if self.timestamp_ls[i] <= timestamp:
                        return self.val_ls[i]
                i -= 1
            return ""

        else:
            return None

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
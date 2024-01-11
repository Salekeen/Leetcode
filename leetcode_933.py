class RecentCounter:

    def __init__(self):
        self.requests = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1
        while self.requests and not (t - 3000 <= self.requests[0] <= t):
            self.requests.pop(0)
            self.counter -= 1
        return self.counter


if __name__ == '__main__':
    # Your RecentCounter object will be instantiated and called as such:
    obj = RecentCounter()
    param_1 = obj.ping(4)
    param_2 = obj.ping(4000)
    param_3 = obj.ping(4001)
    param_4 = obj.ping(4003)

    print(obj.counter)

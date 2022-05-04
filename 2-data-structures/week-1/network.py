# python3
class Buffer:
    def __init__(self, size):
        self.size = size
        self.data = []

    def add(self, finish_time):
        self.data.append(finish_time)

    def pop(self):
        self.data.pop(0)

    def full(self):
        return len(self.data) == self.size

    def empty(self):
        return len(self.data) == 0

    def last(self):
        return self.data[len(self.data) - 1]

    def first(self):
        return self.data[0]


buffer_size, packets = [int(i) for i in input().split(' ')]
buffer = Buffer(buffer_size)
start_time = []

for j in range(0, packets):
    arrival, processing = [int(i) for i in input().split(' ')]

    # remove processed packages
    while (not buffer.empty()) and (arrival >= buffer.first()):
        buffer.pop()

    if not buffer.empty():
        if buffer.full():
            start_time.append(-1)
        else:
            start = buffer.last()
            finish = start + processing
            buffer.add(finish)
            start_time.append(start)
    else:
        start = arrival
        finish = start + processing
        buffer.add(finish)
        start_time.append(start)

for k in start_time:
    print(k)

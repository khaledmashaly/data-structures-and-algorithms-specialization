# python3
from math import floor


def parent(i):
    return floor((i - 1) / 2)


def left_child(i):
    return (2 * i) + 1


def right_child(i):
    return (2 * i) + 2


def sift_down(i, count, swaps):
    while True:
        max_index = i
        l = left_child(i)
        if (l < n) and (a[l] < a[max_index]):
            max_index = l
        r = right_child(i)
        if (r < n) and (a[r] < a[max_index]):
            max_index = r
        if max_index is not i:
            a[i], a[max_index] = a[max_index], a[i]
            count += 1
            swaps.extend([i, max_index])
            i = max_index
            continue
        else:
            return [count, swaps]


def build_heap():
    i_max = int(floor(n / 2 - 1))
    count = 0
    swaps = []
    for i in range(i_max, -1, -1):
        count, swaps = sift_down(i, count, swaps)
    return [count, swaps]


n = int(input())
a = input().split(' ')
a = [int(i) for i in a]
swaps_no, swaps_ops = build_heap()

print(swaps_no)
for i in range(0, len(swaps_ops), 2):
    print(swaps_ops[i], swaps_ops[i + 1])

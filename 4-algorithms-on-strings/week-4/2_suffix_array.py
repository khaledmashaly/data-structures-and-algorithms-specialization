# python3


def sort_chars(s):
    alphabet = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    count = [0] * len(alphabet)
    order = [0] * len(s)
    for k in range(len(s)):
        c = alphabet[s[k]]
        count[c] += 1
    for l in range(1, len(count)):
        count[l] += count[l-1]
    for m in reversed(range(len(s))):
        c = alphabet[s[m]]
        count[c] -= 1
        order[count[c]] = m
    return order


def compute_char_class(s, order):
    classes = [0] * len(s)
    classes[order[0]] = 0
    for k in range(1, len(s)):
        if s[order[k]] == s[order[k-1]]:
            classes[order[k]] = classes[order[k-1]]
        else:
            classes[order[k]] = classes[order[k-1]] + 1
    return classes


def sort_doubled(s, L, order, classes):
    new_order = [0] * len(s)
    count = [0] * len(s)
    for k in range(len(s)):
        count[classes[k]] += 1
    for l in range(1, len(count)):
        count[l] += count[l-1]
    for m in reversed(range(len(s))):
        start = (order[m] - L + len(s)) % len(s)
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, classes, L):
    n = len(new_order)  # sequence size
    new_classes = [0] * n
    for k in range(1, n):
        cur = new_order[k]
        prev = new_order[k-1]
        mid = (cur + L) % n
        mid_prev = (prev + L) % n
        if classes[cur] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]
    return new_classes


def build_suffix_array(s):
    order = sort_chars(s)
    classes = compute_char_class(s, order)
    L = 1

    while L < len(s):
        order = sort_doubled(s, L, order, classes)
        classes = update_classes(order, classes, L)
        L *= 2

    return order


if __name__ == '__main__':
    text = input()
    suffix_array = build_suffix_array(text)
    print(*suffix_array)

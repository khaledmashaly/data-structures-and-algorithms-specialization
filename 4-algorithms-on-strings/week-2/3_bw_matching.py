# python3


def main():
    bwt = input()
    bwt_len = len(bwt)
    _ = int(input())
    patterns = [list(i) for i in input().split()]
    first_column = ''.join(sorted(bwt))
    char_map = {
        '$': 0,
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }
    local_count = [0] * 5
    count = [[0] * 5] * (bwt_len + 1)
    first_occurrence = [-1] * 5
    for i in range(bwt_len):
        ascii_code = char_map[bwt[i]]
        local_count[ascii_code] += 1
        count[i + 1] = local_count[:]
        ascii_code = char_map[first_column[i]]
        if first_occurrence[ascii_code] == -1:
            first_occurrence[ascii_code] = i

    for pattern in patterns:
        top = 0
        bottom = bwt_len - 1
        while top <= bottom:
            if len(pattern) > 0:
                symbol = pattern.pop()
                ascii_code = char_map[symbol]
                top = first_occurrence[ascii_code] + count[top][ascii_code]
                bottom = first_occurrence[ascii_code] + count[bottom + 1][ascii_code] - 1
            else:
                print(bottom - top + 1, end=' ')
                break
        else:
            print(0, end=' ')


if __name__ == '__main__':
    main()

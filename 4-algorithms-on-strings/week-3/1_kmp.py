# python3


def compute_prefix(p: 'prefix of text') -> list:
    p_len = len(p)
    s = [0] * p_len
    border = 0
    for i in range(1, p_len):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def main():
    pattern = input()
    len_p = len(pattern)
    genome = input()
    text = pattern + '$' + genome
    s = compute_prefix(text)
    matches = []
    for i in range(len_p + 1, len(text)):
        if s[i] == len_p:
            matches.append(i - 2 * len_p)
    print(*matches, sep=' ')


if __name__ == '__main__':
    main()

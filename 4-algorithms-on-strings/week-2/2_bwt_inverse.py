# python3


def main():
    """ adapted from https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform """
    bwt = input()
    bwt_len = len(bwt)
    original = [''] * bwt_len
    first_column = ''.join(sorted(bwt))
    char_count = [0] * 256
    char_first_index = [None] * 256
    char_relative_index = [None] * bwt_len
    for i in range(bwt_len):
        ascii_code = ord(bwt[i])
        char_relative_index[i] = char_count[ascii_code]
        char_count[ascii_code] += 1
        ascii_code = ord(first_column[i])
        if char_first_index[ascii_code] is None:
            char_first_index[ascii_code] = i

    next_index = bwt.index('$')
    for i in range(bwt_len):
        next_char = bwt[next_index]
        original[bwt_len - i - 1] = next_char
        ascii_code = ord(next_char)
        next_index = char_first_index[ascii_code] + char_relative_index[next_index]

    print(''.join(original))

if __name__ == '__main__':
    main()

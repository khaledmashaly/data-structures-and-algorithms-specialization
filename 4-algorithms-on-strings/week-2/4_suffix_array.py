# python3


def main():
    text = input()
    text_len = len(text)
    suffix_dict = {}

    for i in reversed(range(text_len)):
        suffix = text[i:text_len]
        suffix_dict[suffix] = i

    suffix_array = [suffix_dict[suffix] for suffix in sorted(suffix_dict)]
    print(*suffix_array)


if __name__ == '__main__':
    main()

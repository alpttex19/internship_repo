def replace_repeated_chars(s, k):
    window = []
    set_window = set()
    res = []
    for c in s:
        if c in set_window:
            res.append('-')
        else:
            res.append(c)
            window.append(c)
            set_window.add(c)
            if len(window) > k:
                set_window.remove(window.pop(0))
    return ''.join(res)


def main():
    a, b = input().split()
    print(replace_repeated_chars(a, int(b)))  # Output: abcdef-x-

if __name__ == "__main__":
    main()
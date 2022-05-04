# python3
def poly_hash(string):
    n = len(string)
    p = 1000000007
    x = 263
    digest = 0
    for i in reversed(range(n)):
        digest = (digest * x + ord(string[i])) % p
    return digest


def precompute_hashes(t, len_t, len_p):
    n = len_t - len_p
    h = [None] * (n + 1)
    s = t[n:len_t]
    h[n] = poly_hash(s)
    y = 1
    x = 263
    p = 1000000007
    for i in range(len_p):
        y = (y * x) % p
    for i in reversed(range(n)):
        h[i] = (x * h[i+1] + ord(t[i]) - y * ord(t[i+len_p])) % p
    return h


def rabin_karp_search(t, p):
    len_p = len(p)
    len_t = len(t)
    p_hash = poly_hash(p)
    t_hashes = precompute_hashes(t, len_t, len_p)
    n = len_t - len_p
    matches = []
    for i in range(n+1):
        if p_hash != t_hashes[i]:
            continue
        elif p == t[i:i + len_p]:
            matches.append(i)
    print(*matches)


def get_input():
    p = input()
    t = input()
    rabin_karp_search(t, p)


get_input()

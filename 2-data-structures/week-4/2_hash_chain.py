# python3
def poly_hash(string):
    n = len(string)
    p = 1000000007
    x = 263
    m = poly_hash.m
    digest = 0
    for i in reversed(range(n)):
        digest = (digest * x + ord(string[i])) % p
    digest %= m
    return digest


def chain_search(chain, string):
    if chain.length == 0:
        return False
    element = chain.head
    while element is not None:
        if element.key == string:
            return True
        element = element.next_node
    return False


class HashTable:
    def __init__(self, m):
        self.table = [[] for _ in range(m)]

    def add(self, key):
        string_exists, digest = self.find(key)
        if not string_exists:
            self.table[digest].insert(0, key)

    def delete(self, key):
        digest = poly_hash(key)
        try:
            self.table[digest].remove(key)
        except ValueError:
            return

    def find(self, key):
        digest = poly_hash(key)
        return self.table[digest].count(key), digest

    def check(self, i):
        chain = self.table[i]
        print(*[key for key in chain])


def process_queries(queries, m):
    bucket = HashTable(m)
    for query in queries:
        if query[0] == 'add':
            bucket.add(query[1])
        elif query[0] == 'del':
            bucket.delete(query[1])
        elif query[0] == 'check':
            chain_no = int(query[1])
            bucket.check(chain_no)
        else:
            if bucket.find(query[1])[0]:
                print('yes')
            else:
                print('no')


def get_input():
    m = int(input())
    poly_hash.m = m
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(input().split(' '))
    process_queries(queries, m)


get_input()

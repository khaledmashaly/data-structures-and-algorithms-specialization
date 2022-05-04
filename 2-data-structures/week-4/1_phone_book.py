# python3
class PhoneBook:
    def __init__(self):
        self.names = {}

    def add(self, number, name):
        self.names[number] = name

    def delete(self, number):
        if number in self.names:
            del self.names[number]

    def find(self, number):
        return self.names.get(number, 'not found')


def process_queries(queries):
    contacts = PhoneBook()
    for query in queries:
        if query[0] == 'add':
            contacts.add(*query[1:])
        elif query[0] == 'del':
            contacts.delete(query[1])
        else:
            contact = contacts.find(query[1])
            print(contact)


def get_input():
    n = int(input())
    queries = []
    for i in range(0, n):
        queries.append(input().split(' '))
    process_queries(queries)


if __name__ == '__main__':
    get_input()

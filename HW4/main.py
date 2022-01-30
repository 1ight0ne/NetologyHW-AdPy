class FlatIterator:

    def __init__(self, input_list):
        self.input_list = input_list
        self.cursor = -1
        self.flat_list = []

    def __iter__(self):
        self.flat_list = sum(self.input_list, [])
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.cursor]


def flat_generator(in_list):
    cnt = 0
    flat_list = sum(in_list, [])
    while cnt < len(flat_list):
        yield flat_list[cnt]
        cnt += 1


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)

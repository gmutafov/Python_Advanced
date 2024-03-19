class sequence_repeat:
    def __init__(self, element, count):
        self.element = element
        self.count = count
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count - 1:
            raise StopIteration

        self.index += 1
        return self.element[self.index % len(self.element)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

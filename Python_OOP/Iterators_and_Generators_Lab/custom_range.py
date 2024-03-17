class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.curr_index = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_index += 1
        if self.curr_index <= self.end:
            return self.curr_index
        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

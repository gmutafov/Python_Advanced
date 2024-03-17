class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
        self.index = -1
        self.vowels_values = [char for char in self.string if char.lower() in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

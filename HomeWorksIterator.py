class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start > end:
            self.i = end - 1
            end = start
        else:
            self.i = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == self.end:
            raise StopIteration()
        if self.i % 2 == 0:
            return self.i
        return 0
en = EvenNumbers(10, 25)
for i in en:
    if i == 0:
        pass
    else:
        print(i)
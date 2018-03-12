class FieldElement:

    def __init__(self, num, prime):
        if num < 0 or num >= prime:
            raise ValueError('num should be between 0 and {}-1'.format(prime))
        self.num = num
        self.prime = prime

    def __eq__(self, other):
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not self.__eq__(other)


a = FieldElement(7, 13)
b = FieldElement(7, 13)

# print(a == b)
print(a != b)
print("hello world")

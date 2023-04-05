class String(str):
    def __add__(self, other):
        return String(super().__add__(str(other)))

    def __sub__(self, other):
        other = str(other)
        index = self.find(other)
        if index == -1:
            return self
        return String(self[:index] + self[index+len(other):])


s = String('New') + String(890)
print(s)
print(type(s))

s = String(1234) + 5678
print(s)
print(type(s))

s = String('New') + 'castle'
print(s)
print(type(s))

s = String('New') + 77
print(s)
print(type(s))

s = String('New') + True
print(s)
print(type(s))

s = String('New') + ['s', ' ', 23]
print(s)
print(type(s))

s = String('New') + None
print(s)
print(type(s))

s = String('New bala7nce') - 7
print(s)
print(type(s))

s = String('New balance') - 'bal'
print(s)
print(type(s))

s = String('New balance') - 'Bal'
print(s)
print(type(s))

s = String('pineapple apple pine') - 'apple'
print(s)
print(type(s))

s = String('New balance') - 'apple'
print(s)
print(type(s))

s = String('NoneType') - None
print(s)
print(type(s))

s = String(55678345672) - 7
print(s)
print(type(s))

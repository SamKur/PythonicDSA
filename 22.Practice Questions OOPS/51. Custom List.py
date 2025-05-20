import ctypes


class CustomList:
    def __init__(self):
        self.newA = None
        self.capacity = 1  # max capacity of list
        self.size = 0  # currently how many items currently present
        self.A = self.__make_array(self.capacity)  # A -> ctype array

    def __make_array(self, capacity):
        # creates a ctype array (static, referential) with defined capacity
        return (capacity * ctypes.py_object)()  # Why not self.capacity - should be reusable for any size,
        # not bound to current capacity

    def __len__(self):
        return self.size

    def __resize(self, new_capacity):
        newA = self.__make_array(new_capacity)
        for i in range(self.size):
            newA[i] = self.A[i]
        self.A = newA
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:  # make double and copy existing
            self.__resize(2*self.capacity)
        self.A[self.size] = value  # core functionality
        self.size += 1

    def __str__(self):  # must return string representation
        result = ""
        for i in range(self.size):
            result = result + str(self.A[i]) + ', '
        return '[' + result[:-2] + ']'

    def pop(self):
        if self.size == 0:
            raise IndexError('pop from an empty list')
        popped_item = self.A[self.size - 1]
        # self.A[self.size - 1] = None # Not needed
        self.size -= 1
        return popped_item

    def __getitem__(self, index):
        return self.A[index]

    def clear(self):
        self.size = self.capacity = 0

    def insert(self, index, value):  # refer once
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        # Resize if array is full
        if self.size >= self.capacity:
            self.__resize(self.capacity*2)
        for i in range(self.size, index, -1):
            self.A[i] = self.A[i - 1]  # adjust space
        self.A[index] = value
        self.size += 1

    def remove(self, element):
        found = False
        newA = self.__make_array(self.capacity)

        j = 0  # index for newA
        for i in range(self.size):
            if not found and self.A[i] == element:
                found = True  # Skip this element (don't copy to newA)
                continue
            newA[j] = self.A[i]
            j += 1

        if not found:
            raise ValueError("Element not found")

        self.A = newA
        self.size -= 1


li = CustomList()
print(len(li))
li.append(435)
li.append(34)
li.append(34)
li.append(34)
li.append(334)
print(len(li))

print(li)
print(li.pop())
print(li)
print(li.pop())
print(li.pop())
# print(li.pop())
# print(li.pop())
print(li)
print(li.pop())  # index error

print(li[1])

# li.clear()
print(li)

li.insert(0, 2222)
print(li)
# l1 = [13,434,5]
# print(l1.clear())
# print(l1)

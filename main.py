from DList import *

a = DList()

a.insert(5, 4)

a.insert(4, 2)

a.insert(1, 3)

a.insert(-3, 10)

a.insert(6, 7)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print("\n")

del a[2]
print(a[0])
print(a[1])
print(a[2])
print(a[3])


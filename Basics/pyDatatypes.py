# Numbers

a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1 + 3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1 + 3j, complex))


# Sequence Type

str = "string using double quotes"
print(type(str))

list1  = [1, "hi", "Python", 2]
print(type(list1))

tup  = ("hi", "Python", 2)
print (type(tup))

d = {1: 'Jimmy',
     2: 'Alex',
     3: 'john',
     4: 'mike'
     }

print(type(d))


# Boolean

print(type(True))
print(type(False))
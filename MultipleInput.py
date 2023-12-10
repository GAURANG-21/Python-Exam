# x = list(map(str,input("Enter values: ").split(" ")))
# print(x)

# x = list(x for x in input("Enter values").split())
# print(x)

x = [i+j for i in "abc" for j in "xyz"]
print(x)

y = [[i+j for i in "abc"] for j in "xyz"]
print(y)

name = "!! Gaurang !!"
print(name.rstrip("!").center(50))


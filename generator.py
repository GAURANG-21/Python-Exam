def fib(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b, a+b
        
# t = fib(5)
# for i in t:
#     print(i)
    
# k = "Vivekananda"
# print(k[1::-1])

# set1 = set(("Geeks", "for", "Geeks"))
# set2 = set(("Geek1", "for", "Geeks"))
# print(set2.symmetric_difference(set1))

x=3
l1 = [2,4,5]
print(id(l1))
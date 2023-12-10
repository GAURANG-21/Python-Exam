li = {(2,3),(3,5)}

def dummy_map(val):
     return (val%2==0)
 
func = lambda x: x[0]%2==0 and x[1]%2==1

t = list(filter(
    func,
    li
))

print(li)
print(t)



def check():
    for i in range(10):
        if(i%2):
            yield i
t = check()
for it in t:
    print(it)
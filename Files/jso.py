import json
L = [1,2,3,4,5,3]

f = open("ok.txt","w")
json.dump(L,f)
f.close()

f = open("ok.txt","r")
t = json.load(f)
print(t)

f.close()
f = open("ok.txt","w")
f.write("Gaurang Agarwal\nSagnik Taraphdar")
f.close()

# f= open("ok.txt", "r")
# print(f.read(2))
# print(f.read())
# f.close()

f = open("ok.txt","r")
print(f.readlines())
# line = f.readlines()
# while line:
#     print(line)
#     line = f.readline()
f.close();

f = open("ok.txt","a")
f.writelines(["Python","\n","is",'\n',"good"])
f.close()

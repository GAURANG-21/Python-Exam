take = 1
def printName(val):
    print(val,"gaurang", sep=":",end=":\n\n\n")
    print(locals())
printName("Gaurang")
if(__name__ == "__main__"):
    print("Checkdone")
else:
    print("called from other file")
class name:
    def check(val):
        print("Class is successfully created\n")
pl = name();
pl.check()
print(globals() ,end="\n\n")
print(locals())
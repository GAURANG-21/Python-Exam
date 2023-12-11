#When multiple inputs are sent from user side

def fun(*args):
    for i in args:
        print(i*i, end=" ")
        
fun(1,2,3,4)

#When it's on sender side

def func(var1, var2, var3):
    print(var1, var2, var3)
x = ("Gaurang","Agarwal","Sagnik")
func(*x)
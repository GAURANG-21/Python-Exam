def cube(**kwargs):
    print(kwargs['time'])
    # print(type(args))
    for i in kwargs.values():
        print(i*i)
        
cube(value=1, time=2)
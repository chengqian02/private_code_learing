

def a(*args, **kwargs):
    print(args)
    print(kwargs)

def b(d):
    a(**d)

s= {"c":2}
b(s)

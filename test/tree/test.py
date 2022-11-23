


def a(*args, **kwargs):
    print(type(kwargs))
    if len(args)>0:
        c = "".join(args)
        print(c)

    for k,v in kwargs.items():
        print(k,v)
b = "1"
a("23", b=b)
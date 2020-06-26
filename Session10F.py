# Args and Kwargs together

def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(10, 20, 30, 40, 50, name="john", email="john@example.com", password="pass123")
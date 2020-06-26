# Dictionary Arguments or Keyword Arguments

# kwargs can be any name of your choice
def register(**kwargs):
    print(kwargs, type(kwargs))


register(name="John", email="john@example.com", password="pass123")
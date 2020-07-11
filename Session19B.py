def data_generator():

    file = open("points.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line

result = data_generator()
data = next(result)
data = data.split(",")
print(data[0])

data = next(result)
data = data.split(",")
print(data[1])

"""
    Image is a collection of Pixels
    Pixel is RGB Value [ranges from 0 to 255]
    For rgb colors reference: https://www.w3schools.com/colors/colors_picker.asp?colorhex=ff0c14
"""
#           R   G   B
pixel1 = [120, 50, 90]
pixel2 = [235, 50, 90]
pixel3 = [128, 45, 90]
pixel4 = [180, 50, 90]
pixel5 = [175, 32, 12]
pixel6 = [220, 50, 67]
pixel7 = [212, 22, 123]
pixel8 = [129, 50, 90]
pixel9 = [191, 11, 113]

image = [
    [pixel1, pixel2, pixel3],
    [pixel4, pixel5, pixel6],
    [pixel7, pixel8, pixel9],
]

# Implement Pixel Rotation
# 1. Rotate an Image
#     1.1 90 degrees to the right
#     1.2 90 degrees to the left
#     1.3 180 degrees to the right
#     1.4 180 degrees to the left
# 2. Gray Scale an Image:
#    pixel1:[120, 50, 90] => 120+50+90//3 = 200
#    pixel1:[200, 200, 200]


# Discussion for tomorrow => String, Set, Dictionary
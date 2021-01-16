from PIL import Image, ImageDraw
import numpy as np
import math

SIZE = 70                   # px dimentions of the circles
FILE = "CircleColor5.csv"   # csv to open
EXT = ".png"                # file extension
NAME = "Circle"             # file name suffix

# open csv
file = open(FILE)
data = np.genfromtxt(file, delimiter=",")
data = np.delete(data, (0), axis = 0)   # delete the top row
index = 1   # for naming

# loop through each color
for dat in data:
    # the rgb won't accept floats, so i rounded the data up
    r = math.ceil(dat[0])
    g = math.ceil(dat[1])
    b = math.ceil(dat[2])

    # create image
    circle = Image.new(mode = "RGB", size = (SIZE, SIZE))
    circle.paste((r, g, b), [0, 0, circle.size[0], circle.size[1]])

    # draw an alpha mask
    alpha = Image.new("L", circle.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse((0,0, alpha.size[0] - 1, alpha.size[1] - 1), fill = 255)
    circle.putalpha(alpha)

    # save and increment the naming index
    circle.save(NAME + str(index) + EXT)
    index += 1
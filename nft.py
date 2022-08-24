# import sys
# sys.path.append("pixray")
# import pixray
# input_list = ["Okapi", "Fossa", "The Maned Wolf", "The Blue Dragon", "Slow Loris",
#               "Angora Rabbit", "Pacu Fish", "Axolotl", "Blobfish"]

# for animal in input_list:
#   print(animal)
#   pixray.run(
#       animal,
#       quality = "best",
#       custom_loss = "aesthetic",
#       display_clear= True
#   )
  

# import matplotlib.pyplot as plt
# from samila import GenerativeImage
# from samila import Projection
# import random
# import math
# def f1(x, y):
#     result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
#     return result
# def f2(x, y):
#     result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
#     return result
# g = GenerativeImage(f1, f2)
# g.generate()
# g.seed
# g.plot(color="red", bgcolor="black", projection=Projection.POLAR)
# g.plot()
# plt.show()

from turtle import*
import random

setup(1000,1000)
goto(100,100)

exitonclick()

# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


#Importing the libraries.
import numpy as np
import matplotlib.pyplot as plt

#Function to normalise a vector.

def normalise(vector):
    return vector / np.linalg.norm(vector)

#Defining Screen size.

width = 640
height = 480

#Defining camera and screen.

camera = np.array([0,0,1])
ratio = float(width/height)
screen = (-1,1/ratio,1,-1/ratio) #Sccreen perfectly fits the camera.

#Declares Scene Objects.

objects = [
    { 'center': np.array([2, 0, 1]), 'radius': 1 }
]

#Dividing the screen in parts
image = np.zeros((height,width,3))
for i,y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j,x in enumerate(np.linspace(screen[0], screen[2], width)):
        pixel = np.array([x,y,0])
        origin = camera
        direction = normalise(pixel - origin)
        print("Current Progress is %d out of %d rows." % (i + 1, height))
        
plt.imsave("render.png", image) #Saves the final render.
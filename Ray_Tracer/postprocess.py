import cv2
#Using OpenCV to anti-alias the render from raytracing.py.
#I should implement samples in the main loop instead.

n = input("Do you want a blur effect with higher resoultion or downsampling? (b / d)")
if n == 'b':
    image = cv2.imread('C://Users//rhyth//Downloads//Test\College Projects//Python//render.png')
    Gaussian = cv2.GaussianBlur(image, (3, 3), 0)
    filename = 'render_post.png'
    cv2.imwrite(filename, Gaussian)
elif n == 'd':
    image = cv2.imread('C://Users//rhyth//Downloads//Test\College Projects//Python//render.png')
    image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
    filename = 'render_post.png'
    cv2.imwrite(filename, image)
else:
    print("Using no Post process.")
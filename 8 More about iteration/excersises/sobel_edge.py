import cImage
import math
import sys

# Code adapted from http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/image-processing/edge_detection.html
# Licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.

# this algorithm takes some time for larger images - this increases the amount of time
# the program is allowed to run before it times out
#sys.setExecutionLimit(20000)

img = cImage.Image("luther.jpg")
newimg = cImage.EmptyImage(img.getWidth(), img.getHeight())
win = cImage.ImageWin()

for x in range(1, img.getWidth()-1):  # ignore the edge pixels for simplicity (1 to width-1)
    for y in range(1, img.getHeight()-1): # ignore edge pixels for simplicity (1 to height-1)

        # initialise Gx to 0 and Gy to 0 for every pixel
        Gx = 0
        Gy = 0

        # top left pixel
        p = img.getPixel(x-1, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        # intensity ranges from 0 to 765 (255 * 3)
        intensity = r + g + b

        # accumulate the value into Gx, and Gy
        Gx += -intensity
        Gy += -intensity

        # remaining left column
        p = img.getPixel(x-1, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += -2 * (r + g + b)

        p = img.getPixel(x-1, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += -(r + g + b)
        Gy += (r + g + b)

        # middle pixels
        p = img.getPixel(x, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gy += -2 * (r + g + b)

        p = img.getPixel(x, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gy += 2 * (r + g + b)

        # right column
        p = img.getPixel(x+1, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += (r + g + b)
        Gy += -(r + g + b)

        p = img.getPixel(x+1, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += 2 * (r + g + b)

        p = img.getPixel(x+1, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += (r + g + b)
        Gy += (r + g + b)

        # calculate the length of the gradient (Pythagorean theorem)
        length = math.sqrt((Gx * Gx) + (Gy * Gy))

        # normalise the length of gradient to the range 0 to 255
        length = length / 4328 * 255

        length = int(length)

        # draw the length in the edge image
        newpixel = cImage.Pixel(length, length, length)
        newimg.setPixel(x, y, newpixel)

newimg.draw(win)
win.exitonclick()

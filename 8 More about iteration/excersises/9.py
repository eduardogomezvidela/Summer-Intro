#black and white

import cImage

img = cImage.Image("luther.jpg")        #Get the image

w = img.getWidth()                                  #Get width and height
h = img.getHeight()

win = cImage.ImageWin(img, w, h)        #Create a window

img.draw(win)                                           #Draw image in window

for col in range (w):                           #Nested iteration
    for row in range (h):
        pixel = img.getPixel(col,row)           #Get pixel

        red = pixel.getRed()
        green = pixel.getGreen()
        blue = pixel.getBlue()

        average = (red+green+blue) / 3
        average = int(average)

        if (average > 255/2):
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255

        else:
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 0            

        img.setPixel(col,row,pixel)         #Apply 0 red to pixel

img.draw(win)                                       #Draw image again

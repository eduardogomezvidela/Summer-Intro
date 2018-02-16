#Write a general pixel mapper function that will take an image and a pixel mapping function as parameters.
#The pixel mapping function should perform a manipulation on a single pixel and return a new pixel.


import cImage

###########################

def mapper(img, manipulator):
    manipulator(img)



def black_white(pic):
    
    img = cImage.Image(pic)        #Get the image
    w = img.getWidth()                                  #Get width and height
    h = img.getHeight()

    img2= cImage.EmptyImage(w,h)

    win = cImage.ImageWin(img, w, h)        #Create a window
    win2 = cImage.ImageWin(img2, w, h)        #Create a window

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

            img2.setPixel(col,row,pixel)         #Apply 0 red to pixel

    img2.draw(win2)                                       #Draw image again

    win2.exitonclick()
    win.exitonclick()
#########################

img = "luther.jpg"

mapper(img, black_white)



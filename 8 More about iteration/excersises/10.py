#Sepia Tone

#newR = (R × 0.393 + G × 0.769 + B × 0.189)
#newG = (R × 0.349 + G × 0.686 + B × 0.168)
#newB = (R × 0.272 + G × 0.534 + B × 0.131)

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

        newR = (red * 0.393 + green * 0.769 + blue *0.189)          #Sepia function
        newG = (red * 0.349 + green * 0.686 + blue * 0.168)
        newB = (red * 0.272 + green * 0.534 + blue* 0.131)

        if (newR > 255):                                                                    #Makes sure that no color will be  beyond 255
            newR = 255
        if (newG > 255):
            newG = 255
        if (newB > 255):
            newB = 255

        newR=int(newR)                              #Convert to int
        newG=int(newG)
        newB=int(newB)

        pixel.red = newR                        #Assign pixel it's color values
        pixel.green = newG
        pixel.blue = newB


        img.setPixel(col,row,pixel)         #Apply 0 red to pixel

img.draw(win)                                       #Draw image again

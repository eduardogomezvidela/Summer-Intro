import cImage
import random

#This program makes the image quality shittier

image = cImage.Image("Golden.jpg")           #Creates image object using the golden pic

w=image.getWidth()                                      #Get height and width
h=image.getHeight()

window =cImage.ImageWin("Golden.jpg",w,h)   #Makes a window for the pic to show up in

image.draw(window)              #Draw the image in

for col in range (w):                   #Nested iteration to cover all pixels
    for row in range (h):
        pixel = image.getPixel(col,row)         #Get pixel
        red = pixel.getRed()                                #Get each color value of the pixel
        green = pixel.getGreen()
        blue = pixel.getBlue()

        if (red < 177):                                                                     #Change each color value of the pixel
            pixel.red = red+random.randrange(0,80)          
        if(green < 177):
            pixel.green = green + random.randrange(0,80)
        if(blue < 177):
            pixel.blue = blue + random.randrange(0,80)
        image.setPixel(col,row,pixel)                                           #Apply the new color value to the pixel


new_window =cImage.ImageWin("Golden.jpg",w,h)   #Makes a new window for the new pic to show up in

image.draw(new_window)  #Draw image with shitty quality

window.exitOnClick()                        #Must close window before closing new_window
new_window.exitOnClick()

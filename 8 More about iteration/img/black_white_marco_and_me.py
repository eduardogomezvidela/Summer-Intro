import cImage
import random

#This program makes the image black&white

def black_white (picture):
    image = cImage.Image(picture)           #Creates image object using the golden pic

    w=image.getWidth()                                      #Get height and width
    h=image.getHeight()

    window =cImage.ImageWin(picture,w,h)   #Makes a window for the pic to show up in

    image.draw(window)              #Draw the image in

    for col in range (w):                   #Nested iteration to cover all pixels
        for row in range (h):
            pixel = image.getPixel(col,row)         #Get pixel
            red = pixel.getRed()                                #Get each color value of the pixel
            green = pixel.getGreen()
            blue = pixel.getBlue()
            average = (red+green+blue)/3                    #Get the average so it will be black and white
            average = int(average)                                      #Convert float to int
            
            pixel.red = average                                                 #Change each color value of the pixel
            pixel.green = average
            pixel.blue = average
            image.setPixel(col,row,pixel)                                           #Apply the new color value to the pixel


    new_window =cImage.ImageWin(picture,w,h)   #Makes a new window for the new pic to show up in

    image.draw(new_window)  #Draw image with shitty quality

black_white("marco.jpg")

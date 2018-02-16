#POP ART Andy Warhol

import cImage


#MONROE

pic = cImage.Image("monroe.jpg")

w = pic.getWidth()
h = pic.getHeight()

window0 = cImage.ImageWin(pic,w,h)

pic.draw(window0)

#RED MONROE
pic = cImage.Image("monroe.jpg")

w = pic.getWidth()
h = pic.getHeight()

window = cImage.ImageWin(pic,w,h)
for col in range (w):
    for row in range (h):
        pixel = pic.getPixel(col,row)

        if(pixel.red > 200 and pixel.green > 200 and pixel.blue > 200):     #TEETH
            pixel.red = 255
            pixel.green = 255
            pixel.blue=255
            
        elif (pixel.blue < 80):                                                                         #HAIR
            pixel.red = pixel.red
            pixel.green = pixel.green
        else:
            pixel.red = 256 - (256 - pixel.red)                                         #EVERYTHING ELSE
            pixel.green = 0
            pixel.blue = 0

        pic.setPixel(col,row,pixel)

pic.draw(window)

#GREEN MONROE
pic = cImage.Image("monroe.jpg")

w = pic.getWidth()
h = pic.getHeight()

window2 = cImage.ImageWin(pic,w,h)


for col in range (w):
    for row in range (h):
        pixel = pic.getPixel(col,row)

        if(pixel.red > 200 and pixel.green > 200 and pixel.blue > 200):
            pixel.red = 255
            pixel.green = 255
            pixel.blue=255

        elif (pixel.blue < 80 and pixel.green > 180):
            pixel.red = 255
            pixel.green = 144
            pixel.blue=46
        else:
            pixel.green = 256 - (256 - pixel.green)
            pixel.red = 0
            pixel.blue = 0

        pic.setPixel(col,row,pixel)

pic.draw(window2)

#ORANGE MONROE
pic = cImage.Image("monroe.jpg")

w = pic.getWidth()
h = pic.getHeight()

window2 = cImage.ImageWin(pic,w,h)


for col in range (w):
    for row in range (h):
        pixel = pic.getPixel(col,row)

        if(pixel.red > 197 and pixel.green > 197 and pixel.blue > 197):
            pixel.red = 255
            pixel.green = 255
            pixel.blue=255

        elif (pixel.blue < 80 and pixel.green > 180):
            pixel.red = 37
            pixel.green = 21
            pixel.blue=255
        else:
            pixel.green = 255 - (255 - pixel.green)
            pixel.red = 150
            #pixel.red = 255 - (255 - pixel.red)
            pixel.blue = 0

        pic.setPixel(col,row,pixel)

pic.draw(window2)

#BLUE MONROE
pic = cImage.Image("monroe.jpg")

w = pic.getWidth()
h = pic.getHeight()

window2 = cImage.ImageWin(pic,w,h)


for col in range (w):
    for row in range (h):
        pixel = pic.getPixel(col,row)

        if(pixel.red > 200 and pixel.green > 200 and pixel.blue > 200):
            pixel.red = 255
            pixel.green = 60
            pixel.blue=60

        elif (pixel.blue < 80 and pixel.green > 180):
            pixel.red = 180
            pixel.green = 180
            pixel.blue=0
        else:
            pixel.green =0
            pixel.red = 0 
            pixel.blue = 255 - (255-pixel.blue)

        pic.setPixel(col,row,pixel)

pic.draw(window2)

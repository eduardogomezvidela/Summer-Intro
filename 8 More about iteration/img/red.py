#Red image

import cImage

pic = cImage.Image("bird.jpg")

w = pic.getWidth()
h = pic.getHeight()

window = cImage.ImageWin(pic,w,h)

pic.draw(window)

for col in range (w):
    for row in range (h):
        pixel = pic.getPixel(col,row)

        #blue=pixel.getBlue()
        #green=pixel.getGreen()
       # if (pixel.red < 200):
            #pixel.red = pixel.red + 50
        pixel.blue = 20
        pixel.green = 20

        pic.setPixel(col,row,pixel)

pic.draw(window)

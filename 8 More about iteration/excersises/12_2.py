import cImage

import enlarge

img=enlarge.enlarge_image("luther.jpg")



#img = cImage.Image("luther.jpg")

w = img.getWidth()
h = img.getHeight()


img_blur = cImage.EmptyImage(w,h)

win_blur = cImage.ImageWin(img_blur,w,h)

for col in range(w):
    for row in range(h):

        pixel = img.getPixel(col, row)

        if (col > 0 and col < w-1 and row > 0 and row < h-1):

            pU = img.getPixel(col, row -1)              #Get pixels around the original pixel
            pR = img.getPixel(col + 1, row)
            pD = img.getPixel(col, row + 1)
            pL = img.getPixel(col - 1,row)

            red =(pixel.getRed()+pU.getRed() + pR.getRed() + pD.getRed() + pL.getRed()) / 5                   #Gets the average colors of the pixels around the original pixel
            green =(pixel.getGreen()+pU.getGreen()+pR.getGreen()+pD.getGreen()+pL.getGreen())/5
            blue =(pixel.getBlue()+pU.getBlue()+pR.getBlue()+pD.getBlue()+pL.getBlue())/5

            red=int(red)                #Turns floats to ints
            green=int(green)
            blue=int(blue)

            pixel.setRed(red)                                                           #Gives the pixel its new average color
            pixel.setGreen(green)
            pixel.setBlue(blue)

            img_blur.setPixel(col,row,pixel)                                #Puts pixel in the img_blur

img_blur.draw(win_blur)                                 #Draws new blurry image

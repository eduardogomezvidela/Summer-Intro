import cImage

import enlarge

img=enlarge.enlarge_image("luther.jpg")

def intensity(pixel):
    red = pixel.getRed()
    green=pixel.getGreen()
    blue=pixel.getBlue()

    x=red+green+blue

    return x
    
#img = cImage.Image("luther.jpg")

width = img.getWidth()
height = img.getHeight()


img_blur = cImage.EmptyImage(width,height)

win_blur = cImage.ImageWin(img_blur,width,height)

for col in range(width):
    for row in range(height):



        pixel = img.getPixel(col, row)


        if (col > 0 and col < width-1 and row > 0 and row < height-1):

            a = img.getPixel(col-1, row -1)              #Get kernel
            b = img.getPixel(col , row-1)
            c = img.getPixel(col+1, row -1)
            d = img.getPixel(col - 1,row)
            e = img.getPixel(col ,row)
            f = img.getPixel(col+1 ,row)
            g = img.getPixel(col-1, row+1)
            h = img.getPixel(col ,row+1)
            i = img.getPixel(col +1,row+1)

            average= (intensity(a)*1 +intensity(b)*2+intensity(c)*1+intensity(d)*2+intensity(e)*4+intensity(f)*2+intensity(g)*1+intensity(h)*2+intensity(i)*1)/16
            average=average/3

            average= int(average)
            
            pixel.setRed(average)
            pixel.setGreen(average)
            pixel.setBlue(average)


        img_blur.setPixel(col,row,pixel)                                #Puts pixel in the img_blur

    img_blur.draw(win_blur)                                 #Draws new blurry image

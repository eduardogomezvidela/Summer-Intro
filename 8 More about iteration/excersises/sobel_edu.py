#Sobel Edge Detection Algorithm

import cImage
import math
import enlarge

img=cImage.Image("edu.jpg")


#img=enlarge.enlarge_image("golden.jpg")

def intensity(pixel):
    red = pixel.getRed()
    green=pixel.getGreen()
    blue=pixel.getBlue()

    x=red+green+blue

    return x

    
#img = cImage.Image("luther.jpg")

width = img.getWidth()
height = img.getHeight()

win = cImage.ImageWin(img,width,height)
img.draw(win)

img_blur = cImage.EmptyImage(width,height)

win_blur = cImage.ImageWin(img_blur,width,height)


for col in range(width):
    for row in range(height):

        pixel = img.getPixel(col, row)


        if (col > 0 and col < width-1 and row > 0 and row < height-1):

            a = img.getPixel(col-1, row -1)              #Get x kernel
            b = img.getPixel(col , row-1)
            c = img.getPixel(col+1, row -1)
            d = img.getPixel(col - 1,row)
            e = img.getPixel(col ,row)
            f = img.getPixel(col+1 ,row)
            g = img.getPixel(col-1, row+1)
            h = img.getPixel(col ,row+1)
            i = img.getPixel(col +1,row+1)

            Gx= (intensity(a)*(-1) +intensity(b)*0+intensity(c)*1+intensity(d)*(-2)+intensity(e)*0+intensity(f)*2+intensity(g)*(-1)+intensity(h)*0+intensity(i)*1)

            Gx=abs(Gx/3)

            Gx= int(Gx)
            if (Gx > 255):
                Gx = 255

            
            a = img.getPixel(col-1, row -1)              #Get y kernel
            b = img.getPixel(col , row-1)
            c = img.getPixel(col+1, row -1)
            d = img.getPixel(col - 1,row)
            e = img.getPixel(col ,row)
            f = img.getPixel(col+1 ,row)
            g = img.getPixel(col-1, row+1)
            h = img.getPixel(col ,row+1)
            i = img.getPixel(col +1,row+1)

            Gy= (intensity(a)*(-1) +intensity(b)*(-2)+intensity(c)*(-1)+intensity(d)*(0)+intensity(e)*0+intensity(f)*0+intensity(g)*(1)+intensity(h)*2+intensity(i)*1)

            Gy=abs(Gy/3)

            Gy= int(Gy)
            if (Gy > 255):
                Gy = 255


            G = math.sqrt((Gx**2) + (Gy**2))

            G = int(G)

            if(G < 90):
                G = 0

            if (G > 255):
                G = 255
                
            pixel.setRed(G)
            pixel.setGreen(G)
            pixel.setBlue(G)

                
        img_blur.setPixel(col,row,pixel)                                #Puts pixel in the img_blur



    img_blur.draw(win_blur)                                 #Draws new blurry image

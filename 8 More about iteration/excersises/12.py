import cImage

#newim = image.EmptyImage(oldw * 2, oldh * 2)

#get image
img1 = cImage.Image("luther.jpg")        #Get the image

#make window1
w = img1.getWidth()                                  #Get width and height
h = img1.getHeight()
win = cImage.ImageWin(img1, w, h)

img2 = cImage.EmptyImage((w*2),(h*2))        #Get the image
w2=w*2
h2=h*2

print(w2,h2)

#draw on window1
img1.draw(win)

#make double sized window2
win2 = cImage.ImageWin(img1, w*2, h*2)        #Create a window
win3 = cImage.ImageWin(img1, w*2, h*2)        #Create a third window that won't be blurry

#something

for row in range (h):                   #Nested iteration
    for col in range (w):

        pixel = img1.getPixel(col,row)

        img2.setPixel(2*col,2*row,pixel)
        img2.setPixel(2*col,2*row+1,pixel)
        img2.setPixel(2*col+1,2*row,pixel)
        img2.setPixel(2*col+1,2*row+1,pixel)

img2.draw(win3)         #Will draw a non-blurry big version of original image

        
for row in range ((h*2)-1):                                 #Nested iteration for the new image2
    for col in range ((w*2)-1):
        
        if(col > 0 and col < 800 and row > 0 and row < 488):                                                                           #Averages pixels around to create a blur
            pixelR = img2.getPixel(col+1,row)
            pixelD = img2.getPixel(col, row+1)
            pixelL = img2.getPixel(col-1,row)
            pixelU = img2.getPixel(col,row-1)
            
            averageR=(pixelR.red+pixelD.red+pixelL.red+pixelU.red)/4
            averageG=(pixelR.green+pixelD.green+pixelL.green+pixelU.green)/4
            averageB=(pixelR.blue+pixelD.blue+pixelL.blue+pixelU.blue)/4

            pixel.red = int(averageR)
            pixel.green=int(averageG)
            pixel.blue=int(averageB)

            img2.setPixel(col,row,pixel)
            
            
#draw double sized image on window 2 and window 3
img2.draw(win2)

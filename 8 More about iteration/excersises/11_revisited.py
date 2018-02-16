import cImage

#newim = image.EmptyImage(oldw * 2, oldh * 2)

#get image
img1 = cImage.Image("luther.jpg")        #Get the image

#make window1
w = img1.getWidth()                                  #Get width and height
h = img1.getHeight()
win = cImage.ImageWin(img1, w, h)

img2 = cImage.EmptyImage((w*2),(h*2))        #Get the image
w2=img2.getWidth()
h2=img2.getHeight()
#draw on window1
img1.draw(win)

#make double sized window2
win2 = cImage.ImageWin(img1, w*2, h*2)        #Create a window

#something
for row in range (h):
    for col in range (w):

        pixel = img1.getPixel(col,row)

        img2.setPixel(2*col,2*row,pixel)
        img2.setPixel(2*col,2*row+1,pixel)
        img2.setPixel(2*col+1,2*row,pixel)
        img2.setPixel(2*col+1,2*row+1,pixel)


#draw double sized image on window 2
img2.draw(win2)

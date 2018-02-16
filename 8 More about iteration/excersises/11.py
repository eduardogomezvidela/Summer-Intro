#Enlarge image

import cImage

img = cImage.Image("luther.jpg")        #Get the image

w = img.getWidth()                                  #Get width and height
h = img.getHeight()

print(w,h)


for i in range(0,11,3):
    print(i)



win = cImage.ImageWin(img, w, h)
img2 = cImage.EmptyImage((w*2),(h*2))        #Get the image
win2 = cImage.ImageWin(img, w*2, h*2)        #Create a window

img.draw(win)                                           #Draw image in window

for row in range (h):                           #Nested iteration
    for col in range (w):
        
        pixel = img.getPixel(col,row)           #Get pixel

        img2.setPixel(2*col,2*row,pixel)
        img2.setPixel(2*col,2*row+1,pixel)
        img2.setPixel(2*col+1,2*row,pixel)
        img2.setPixel(2*col+1,2*row+1,pixel)


img2.draw(win2)                                       #Draw image again

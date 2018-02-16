import cImage

img = cImage.Image("luther.jpg")

w = img.getWidth()
h = img.getHeight()


img_large = cImage.EmptyImage(w*2,h*2)              #Make new large image

win_large = cImage.ImageWin(img_large, w*2, h*2)        #Make window for new large image

for col in range (w):                   #Nested iteration
    for row in range (h):
        
        pixel = img.getPixel(col,row)       #Get pixel

        img_large.setPixel(col*2, row*2, pixel)             #Set same pixel on 4 different spots next to
        img_large.setPixel(col*2+1, row*2, pixel)       #each other on the large image
        img_large.setPixel(col*2, row*2+1, pixel)
        img_large.setPixel(col*2+1, row*2+1, pixel)

img_large.draw(win_large)                                           #Draw large image on large window


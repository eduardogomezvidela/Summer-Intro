
from PIL import Image

image1=Image.open('Golden.jpg')     #open the golden picture and assign it

image1.show()                   #open pic so we can see it

image1.save('Golden.png')       #save pic as .png

image1.rotate(45).show()        #rotates pic 45 degrees and shows it

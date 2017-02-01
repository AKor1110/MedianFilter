from PIL import Image

#Image Size = (495, 557)
'''
To make a new image:
im = Image.open("dead_parrot.jpg") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
print pix[x,y] #Get the RGBA Value of the a pixel of an image
pix[x,y] = value # Set the RGBA Value of the image (tuple)
''' 

def Pixels():
    pixels = [(x,y) for y in range(558) for x in range(496)] #276,768 pixels; 276,767 indices
    return pixels
    
def ImagesRGB():
    pixels = Pixels()
    rgb = []
        
    img1 = Image.open("1.png").convert('RGB')
        
    img2 = Image.open("2.png").convert('RGB')
        
    img3 = Image.open("3.png").convert('RGB')
        
    img4 = Image.open("4.png").convert('RGB')
        
    img5 = Image.open("5.png").convert('RGB')
        
    img6 = Image.open("6.png").convert('RGB')
        
    img7 = Image.open("7.png").convert('RGB')
        
    img8 = Image.open("8.png").convert('RGB')
        
    img9 = Image.open("9.png").convert('RGB')
    
    print img1.getpixel((0,0))
    
        
        
        
ImagesRGB()
            
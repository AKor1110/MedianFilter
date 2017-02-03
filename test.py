from PIL import Image
img1 = Image.open("1.png").convert('RGB')
img2 = Image.open("2.png").convert("RGB")
img3 = Image.open("3.png").convert("RGB")
img4 = Image.open("4.png").convert("RGB")
img5 = Image.open("5.png").convert("RGB")
img6 = Image.open("6.png").convert("RGB")
img7 = Image.open("7.png").convert("RGB")
img8 = Image.open("8.png").convert("RGB")
img9 = Image.open("9.png").convert("RGB")
rgb = []
for y in range(img1.size[1]):
    for x in range(img1.size[0]):
        r = []
        g = []
        b = []
        r.append(img1.getpixel((x,y))[0])
        g.append(img1.getpixel((x,y))[1])
        b.append(img1.getpixel((x,y))[2])
        
        r.append(img2.getpixel((x,y))[0])
        g.append(img2.getpixel((x,y))[1])
        b.append(img2.getpixel((x,y))[2])
        
        r.append(img3.getpixel((x,y))[0])
        g.append(img3.getpixel((x,y))[1])
        b.append(img3.getpixel((x,y))[2])
            
        r.append(img4.getpixel((x,y))[0])
        g.append(img4.getpixel((x,y))[1])
        b.append(img4.getpixel((x,y))[2])
            
        r.append(img5.getpixel((x,y))[0])
        g.append(img5.getpixel((x,y))[1])
        b.append(img5.getpixel((x,y))[2])
            
        r.append(img6.getpixel((x,y))[0])
        g.append(img6.getpixel((x,y))[1])
        b.append(img6.getpixel((x,y))[2])
            
        r.append(img7.getpixel((x,y))[0])
        g.append(img7.getpixel((x,y))[1])
        b.append(img7.getpixel((x,y))[2])
            
        r.append(img8.getpixel((x,y))[0])
        g.append(img8.getpixel((x,y))[1])
        b.append(img8.getpixel((x,y))[2])
        
        r.append(img9.getpixel((x,y))[0])
        g.append(img9.getpixel((x,y))[1])
        b.append(img9.getpixel((x,y))[2])
            
        r_med = sorted(r)[len(r)/2]
        g_med = sorted(g)[len(g)/2]
        b_med = sorted(b)[len(b)/2]
        rgb.append((r_med,g_med,b_med))
result = Image.new("RGB", (img1.size[0], img1.size[1]))
result.putdata(rgb)
result.save("test.png")

'''
import os
import time

class MedianFilter:
    def __init__(self):
        self.png = []
        for filename in os.listdir('/home/ubuntu/workspace/Project'):
            if filename.endswith(".png"):
                self.png.append(filename)
        self.png = sorted(self.png)
        self.image_amount = len(self.png)
        self.img_width = Image.open(self.png[0]).size[0]
        self.img_height = Image.open(self.png[0]).size[1]

    def Pixels(self):
        pixels = [(x,y) for y in range(self.img_height) for x in range(self.img_width)] #275,715 pixels; 275,714 indices
        return pixels
    
    def ImagesRGB(self):
        img1 = Image.open(self.png[0]).convert('RGB')
        img2 = Image.open(self.png[1]).convert('RGB')
        img3 = Image.open(self.png[2]).convert('RGB')
        img4 = Image.open(self.png[3]).convert('RGB')
        img5 = Image.open(self.png[4]).convert('RGB')
        img6 = Image.open(self.png[5]).convert('RGB')
        img7 = Image.open(self.png[6]).convert('RGB')
        img8 = Image.open(self.png[7]).convert('RGB')
        img9 = Image.open(self.png[8]).convert('RGB')
        pixels = self.Pixels()
        rgb_average = []
        for pixel in pixels:
            r = []
            g = []
            b = []
            r.append(img1.getpixel(pixel)[0])
            g.append(img1.getpixel(pixel)[1])
            b.append(img1.getpixel(pixel)[2])
            
            r.append(img2.getpixel(pixel)[0])
            g.append(img2.getpixel(pixel)[1])
            b.append(img2.getpixel(pixel)[2])
            
            r.append(img3.getpixel(pixel)[0])
            g.append(img3.getpixel(pixel)[1])
            b.append(img3.getpixel(pixel)[2])
            
            r.append(img4.getpixel(pixel)[0])
            g.append(img4.getpixel(pixel)[1])
            b.append(img4.getpixel(pixel)[2])
            
            r.append(img5.getpixel(pixel)[0])
            g.append(img5.getpixel(pixel)[1])
            b.append(img5.getpixel(pixel)[2])
            
            r.append(img6.getpixel(pixel)[0])
            g.append(img6.getpixel(pixel)[1])
            b.append(img6.getpixel(pixel)[2])
            
            r.append(img7.getpixel(pixel)[0])
            g.append(img7.getpixel(pixel)[1])
            b.append(img7.getpixel(pixel)[2])
            
            r.append(img8.getpixel(pixel)[0])
            g.append(img8.getpixel(pixel)[1])
            b.append(img8.getpixel(pixel)[2])
            
            r.append(img9.getpixel(pixel)[0])
            g.append(img9.getpixel(pixel)[1])
            b.append(img9.getpixel(pixel)[2])
            
            r_med = sorted(r)[len(r)/2]
            g_med = sorted(g)[len(g)/2]
            b_med = sorted(b)[len(b)/2]
            rgb_average.append((r_med,g_med,b_med))
        return rgb_average
    
    def MakePicture(self):
        rgb_average = self.ImagesRGB()
        new_image = Image.new('RGB',(self.img_width, self.img_height))
        new_image.putdata(rgb_average)
        new_image.save("test.png")
        print "Your new picture is ready!"

Filter = MedianFilter()
start = time.time()
Filter.MakePicture()
print "This code took: " + str(time.time()-start) + " seconds."
'''
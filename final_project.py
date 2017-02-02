from PIL import Image
import os
import time

class MedianFilter:
    def __init__(self, png):
        self.png = sorted(png)
        self.image_amount = len(self.png)
        self.img_width = Image.open(self.png[0]).size[0]
        self.img_height = Image.open(self.png[0]).size[1]
        self.pixels = [(x,y) for y in range(self.img_height) for x in range(self.img_width)]

    def ImagesRGB(self):
        rgb = []
        img1 = Image.open(self.png[0]).convert('RGB')
        img2 = Image.open(self.png[1]).convert('RGB')
        img3 = Image.open(self.png[2]).convert('RGB')
        img4 = Image.open(self.png[3]).convert('RGB')
        img5 = Image.open(self.png[4]).convert('RGB')
        img6 = Image.open(self.png[5]).convert('RGB')
        img7 = Image.open(self.png[6]).convert('RGB')
        img8 = Image.open(self.png[7]).convert('RGB')
        img9 = Image.open(self.png[8]).convert('RGB')
        
        for coor in self.pixels:
            rgb.append([img1.getpixel(coor),
                        img2.getpixel(coor),
                        img3.getpixel(coor),
                        img4.getpixel(coor),
                        img5.getpixel(coor),
                        img6.getpixel(coor),
                        img7.getpixel(coor),
                        img8.getpixel(coor),
                        img9.getpixel(coor)
                        ])
        return rgb
        
    def PixelAverage(self):
        rgb = self.ImagesRGB()
        rgb_average = []
        for pixel in rgb:
            r = []
            g = []
            b = []
            for tup in pixel:
                r.append(tup[0])
                g.append(tup[1])
                b.append(tup[2])
            r_med = sorted(r)[len(r)/2]
            g_med = sorted(g)[len(g)/2]
            b_med = sorted(b)[len(b)/2]
            rgb_average.append((r_med,g_med,b_med))
        return rgb_average
    
    def MakePicture(self):
        rgb_average = self.PixelAverage()
        new_image = Image.new('RGB',(self.img_width, self.img_height))
        new_image.putdata(rgb_average)
        new_image.save("final.png")
        print "Your new picture is ready!"

png = []
for filename in os.listdir('/home/ubuntu/workspace/Project'):
    if filename.endswith(".png") and filename[0].isdigit():
        png.append(filename)
        
Filter = MedianFilter(png)
start = time.time()
Filter.MakePicture()
print "This code took: " + str(time.time()-start) + " seconds."
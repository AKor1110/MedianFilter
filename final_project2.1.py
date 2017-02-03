from PIL import Image
import os
import time

class MedianFilter:
    def __init__(self, png):
        self.png = sorted(png)
        self.image_amount = len(png)
        self.img_width = Image.open(self.png[0]).size[0]
        self.img_height = Image.open(self.png[0]).size[1]
        self.pixels = [(x,y) for y in range(self.img_height) for x in range(self.img_width)]
    
    def ImagesRGB(self):
        rgb = {}
        img1 = Image.open(self.png[0]).load()
        img2 = Image.open(self.png[1]).load()
        img3 = Image.open(self.png[2]).load()
        img4 = Image.open(self.png[3]).load()
        img5 = Image.open(self.png[4]).load()
        img6 = Image.open(self.png[5]).load()
        img7 = Image.open(self.png[6]).load()
        img8 = Image.open(self.png[7]).load()
        img9 = Image.open(self.png[8]).load()
        
        for coor in self.pixels:
            rgb[coor] = [img1[coor[0],coor[1]],
                        img2[coor[0],coor[1]],
                        img3[coor[0],coor[1]],
                        img4[coor[0],coor[1]],
                        img5[coor[0],coor[1]],
                        img6[coor[0],coor[1]],
                        img7[coor[0],coor[1]],
                        img8[coor[0],coor[1]],
                        img9[coor[0],coor[1]]
        return rgb
        
    def PixelAverage(self):
        rgb = self.MakeDictionary()
        rgb_average = []
        for coor in self.pixels:
            r = []
            g = []
            b = []
            r.append(rgb[coor][0][0])
            g.append(rgb[coor][0][1])
            b.append(rgb[coor][0][2])
            
            r.append(rgb[coor][1][0])
            g.append(rgb[coor][1][1])
            b.append(rgb[coor][1][2])
            
            r.append(rgb[coor][2][0])
            g.append(rgb[coor][2][1])
            b.append(rgb[coor][2][2])
            
            r.append(rgb[coor][3][0])
            g.append(rgb[coor][3][1])
            b.append(rgb[coor][3][2])
            
            r.append(rgb[coor][4][0])
            g.append(rgb[coor][4][1])
            b.append(rgb[coor][4][2])
            
            r.append(rgb[coor][5][0])
            g.append(rgb[coor][5][1])
            b.append(rgb[coor][5][2])
            
            r.append(rgb[coor][6][0])
            g.append(rgb[coor][6][1])
            b.append(rgb[coor][6][2])
            
            r.append(rgb[coor][7][0])
            g.append(rgb[coor][7][1])
            b.append(rgb[coor][7][2])
            
            r.append(rgb[coor][8][0])
            g.append(rgb[coor][8][1])
            b.append(rgb[coor][8][2])
            
            r_med = sorted(r)[len(r)/2]
            g_med = sorted(g)[len(g)/2]
            b_med = sorted(b)[len(b)/2]
            
            rgb_average.append((r_med,g_med,b_med))
        return rgb_average
    
    def MakePicture(self):
        rgb_average = self.PixelAverage()
        new_image = Image.new('RGB',(self.img_width, self.img_height))
        new_image.putdata(rgb_average)
        new_image.save("final_project2.1.png")
        print "Your new picture is ready!"

png = []
for filename in os.listdir('/home/ubuntu/workspace/Project'):
    if filename.endswith(".png") and filename[0].isdigit():
        png.append(filename)
        
Filter = MedianFilter(png)
start = time.time()
Filter.MakePicture()
print "This code took: " + str(time.time()-start) + " seconds."
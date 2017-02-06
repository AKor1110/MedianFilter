from PIL import Image
import os

class MedianFilter:
    def __init__(self, png):
        self.png = sorted(png)
        self.image_amount = len(self.png)
        self.img_width = Image.open(self.png[0]).size[0]
        self.img_height = Image.open(self.png[0]).size[1]
        self.pixels = [(x,y) for y in range(self.img_height) for x in range(self.img_width)]

    def ImagesRGB(self):
        img1 = Image.open(self.png[0]).load()
        img2 = Image.open(self.png[1]).load()
        img3 = Image.open(self.png[2]).load()
        img4 = Image.open(self.png[3]).load()
        img5 = Image.open(self.png[4]).load()
        img6 = Image.open(self.png[5]).load()
        img7 = Image.open(self.png[6]).load()
        img8 = Image.open(self.png[7]).load()
        img9 = Image.open(self.png[8]).load()
        
        rgb = [[img1[coor[0], coor[1]], img2[coor[0], coor[1]], img3[coor[0], coor[1]],
                img4[coor[0], coor[1]], img5[coor[0], coor[1]], img6[coor[0], coor[1]],
                img7[coor[0], coor[1]], img8[coor[0], coor[1]], img9[coor[0], coor[1]]]
                for coor in self.pixels]
        return rgb
        
    def PixelAverage(self):
        rgb = self.ImagesRGB()
        rgb_average = []
        for pixel in rgb:
            r = [tup[0] for tup in pixel]
            g = [tup[1] for tup in pixel]
            b = [tup[2] for tup in pixel]
            r_med = sorted(r)[len(r)/2]
            g_med = sorted(g)[len(g)/2]
            b_med = sorted(b)[len(b)/2]
            rgb_average.append((r_med,g_med,b_med))
        return rgb_average
    
    def MakePicture(self):
        rgb_average = self.PixelAverage()
        new_image = Image.new('RGB',(self.img_width, self.img_height))
        new_image.putdata(rgb_average)
        new_image.save("final_project.png")

png = []
for filename in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if filename.endswith(".png") and filename[0].isdigit():
        png.append(filename)

Filter = MedianFilter(png)
Filter.MakePicture()
from PIL import Image
import os
# https://github.com/CSUMB-SP17-CST205/team6-akor-project1
#-------------------------------------------------------------------------------
class MedianFilter:
    def __init__(self, png):
        self.png = sorted(png)
        self.image_amount = len(self.png)
        self.img_width, self.img_height = Image.open(self.png[0]).size

    def ImagesRGB(self):
        pixels = [(x,y) for y in range(self.img_height) for x in range(self.img_width)]
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
                img7[coor[0], coor[1]], img8[coor[0], coor[1]], img9[coor[0], coor[1]]
                ] for coor in pixels]
        return rgb
        
    def PixelAverage(self):
        rgb = self.ImagesRGB()
        rgb_average = []
        for pixel in rgb:
            r = sorted([tup[0] for tup in pixel])
            g = sorted([tup[1] for tup in pixel])
            b = sorted([tup[2] for tup in pixel])
            rgb_average.append((r[len(r)/2], g[len(g)/2], b[len(b)/2]))
        return rgb_average
    
    def MakePicture(self):
        rgb_average = self.PixelAverage()
        new_image = Image.new('RGB',(self.img_width, self.img_height))
        new_image.putdata(rgb_average)
        new_image.save("final_project.png")
#-------------------------------------------------------------------------------
png = []
for filename in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if filename.endswith(".png") and filename[0].isdigit():
        png.append(filename)
MedianFilter(png).MakePicture()
#-------------------------------------------------------------------------------
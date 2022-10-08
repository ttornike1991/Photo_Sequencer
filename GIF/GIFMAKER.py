
from PIL import Image, ImageDraw
import os

images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8


for k in os.listdir(r'C:\Users\User\Desktop\project\GIF'):
     if k.endswith('.png'):


        im = Image.open(k)
        '''kn , kext =os.path.splitext(k)
        print(kn)'''
        images.append(im)
 

images[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)
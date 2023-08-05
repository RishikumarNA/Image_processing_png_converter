import sys
import os
from PIL import Image

__new__='__main__'
image=sys.argv[1]
new=sys.argv[2]
print (image,new)
if not os.path.exists(new):
    os.makedirs(new)
    
for i in os.listdir(image):
    img=Image.open(f'{image}{new}')
    clean_img=os.path.splitext(image)[0]
    img.save(f'{new}{clean_img}.png','png')
    print("image converted")
    
    
'''import os
from os import listdir
from PIL import Image, ImageFilter
 
# get the path or directory
folder_dir = "C:\Users\Administrator\OneDrive\Documents\python resume projects\JPG to PNG converter\jpg"
for images in os.listdir(folder_dir):
    img=Image.open(images)
    filtered_img=img.filter(ImageFilter.BLUR)
    filtered_img.save("images.png","png")
    print("image converted")
    '''
import os
from PIL import Image
from resizeimage import resizeimage

path = 'C:\\Users\\59011189\\Desktop\\pre_dataset'
for fname in os.listdir(path):
    paths = path + '\\' + str(fname)
    for iname in os.listdir(paths):
        pathss = paths + '\\' +str(iname)
        print(pathss) 
                
        with open(pathss, 'r+b') as f:
                with Image.open(f) as image:
                        cover = resizeimage.resize_cover(image, [100, 100])
                        cover.save(pathss, image.format)

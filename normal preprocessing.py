from PIL import Image
import os, sys

filestr = ''
for i in range (1, 1342):
    filestr = 'NORMAL (' + str(i) + ').png'
    im = Image.open(filestr)
    newpixel = 224
    new_size = im.resize((newpixel, newpixel), Image.ANTIALIAS)
    newname = 'resized ' + filestr
    new_size.save(newname, 'PNG', quality = 90)

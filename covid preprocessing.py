from PIL import Image
import os, sys

filestr = ''
for i in range (1, 134):
    filestr = 'COVID-19 (' + str(i) + ').png'
    im = Image.open(filestr)
    newpixel = 224
    new_size = im.resize((newpixel, newpixel), Image.ANTIALIAS)
    newname = 'resized ' + filestr
    new_size.save(newname, 'PNG', quality = 90)

# Note that from COVID-19(134).png there is no space between COVID-19 and (...)
for i in range (134, 220):
    filestr = 'COVID-19(' + str(i) + ').png'
    im = Image.open(filestr)
    newpixel = 224
    new_size = im.resize((newpixel, newpixel), Image.ANTIALIAS)
    newname = 'resized ' + filestr
    new_size.save(newname, 'PNG', quality = 90)

#save as text decompressed image into bytes
for filename in os.listdir(imagePath):
    if filename!='.DS_Store' and filename[-3:]=='jpg':
        b = imread(filename,flatten=0).flatten()
        print b.shape
        out = ','.join('%d'%i for i in b)+'\n'
        print len(out)
        with open(savepath+'trainMatrix2.txt','a') as fut:
            fut.write(out)
            fut.close()            
////////////////////////////////////////////////////
from __future__ import with_statement
from PIL import Image
 
im = Image.open('Pictures/300x300.png') #relative path to file
 
#load the pixel info
pix = im.load()
 
#get a tuple of the x and y dimensions of the image
width, height = im.size
 
#open a file to write the pixel data
with open('output_file.csv', 'w+') as f:
  f.write('R,G,B\n')
 
  #read the details of each pixel and write them to the file
  for x in range(width):
    for y in range(height):
      r = pix[x,y][0]
      g = pix[x,x][1]
      b = pix[x,x][2]
      f.write('{0},{1},{2}\n'.format(r,g,b))

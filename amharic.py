from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import os.path as path
#configuration
font_size=36
width=32
height=32
back_ground_color=(255,255,255)
font_size=22
font_color=(0,0,0)

"""
Data Augmentation Techniques:
1. Noise
	1.1 dots, clutter
	1.2 Scanner noise
2. Shearing, Affine Transformation
3. Different fonts
   - As MUCH AS POSSIBLE, USE ALLL OF THE 
"""
#font_name = "jirret"
#font_name = "fantuwua"
#font_name = "goffer"
#font_name = "Hiwua"
#font_name = "Tint"
#font_name = "washrabold"
#font_name = "Washrasemibold"
#font_name = "wookianos"
#font_name = "Yebse"
#font_name = "Yigezu"
font_name = "Zelan"
font_ttf = "/home/tesfay/Documents/Thesis/thesis_day to day/codes/washra_fonts-4.1/zelan.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/yigezubisratgothic.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/yebse.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/wookianos.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/washrasb.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/washrab.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/tint.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/hiwua.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/goffer.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/jiret.ttf"
#font_ttf = "/home/tesfay/Desktop/washra_fonts-4.1/fantuwua.ttf"
folder_name = font_name + "files"
os.system("mkdir " + folder_name)

lastletter = u'\u1200'
# Fist Group, 432
cntr = 0
for i in range(432):
	print("First Round: ", i)
	#l.append(unichr(ord(lastletter) + i))
	unicode_text = unichr(ord(lastletter) + i)
	im  =  Image.new ( "RGB", (width,height), back_ground_color )
	draw  =  ImageDraw.Draw ( im )
	unicode_font = ImageFont.truetype(font_ttf, font_size)
	draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )
	if True:#np.mean(im)!=255:
		cntr += 1 
		file_name = path.join(folder_name, str(cntr))
		im.save(file_name + ".jpg")
"""
lastletter = u'\u2D80'

for i in range(0):
	print("Second Round: ", i)
	unicode_text = unichr(ord(lastletter) + i)
	im  =  Image.new ( "RGB", (width,height), back_ground_color )
	draw  =  ImageDraw.Draw ( im )
	unicode_font = ImageFont.truetype(font_ttf, font_size)
	draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )
	if True:#np.mean(im)!=255:
		cntr += 1 
		file_name = path.join(folder_name, str(cntr))
		im.save(file_name + ".jpg")
"""

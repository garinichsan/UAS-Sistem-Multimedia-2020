# import required classes
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
 
# create Image object with the input image
foto = Image.open('foto.png')
W, H =  foto.size
 
# initialise the drawing context with
# the foto object as background
draw = ImageDraw.Draw(foto)

# create font object with the font file and specify
# desired size
font = ImageFont.truetype('Montserrat-Regular.ttf', size=30)
#spicify the color
color = 'rgb(255, 255, 255)' # white color
 
# create the text for watermark
identitas = "18218050 - Garin Ichsan Nugraha"
w1, h1 = draw.textsize(identitas, font=font)

timestamp = str(datetime.now())
w2, h2 = draw.textsize(timestamp, font=font)

#create rectangle image for the watermark backgroung image
Hrec = round(h1+h2+(h1+h2)/2) #cuztomize the rectangle hight first
rectangle = Image.new('RGB', (W, (Hrec)), "black")

#create drawable image of the rectangle to draw the text over
watermark = ImageDraw.Draw(rectangle)

# spicify the position for identitas text
(x, y) = ( round((W-w1)/2), round((0.5*h1)))
# draw the text on the rectangle image
watermark.text((x, y), identitas, fill=color, font=font)

# spicify the position for identitas text
(x, y) = ( round((W-w2)/2), round((1.5*h1)))
# draw the text on the rectangle image
watermark.text((x, y), timestamp, fill=color, font=font)

foto.paste(rectangle,(0,H-Hrec))

# save the watermark image
foto.save('watermarked.png')

#get the original file again to create the gif
original = Image.open('foto.png')

#create and save the gif
original.save('soal1.gif', save_all=True, append_images=[foto], optimize=False, duration=500, loop=0)
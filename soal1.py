# import required classes
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
 
# create Image object with the input image
image = Image.open('background.png')
W, H =  image.size

original = Image.open('background.png')
 
# initialise the drawing context with
# the image object as background
draw = ImageDraw.Draw(image)

# create font object with the font file and specify
# desired size
font = ImageFont.truetype('Montserrat-Regular.ttf', size=30)
 
# starting position of the text
identitas = "18218050 - Garin Ichsan Nugraha"
w1, h1 = draw.textsize(identitas, font=font)
(x, y) = ((W-w1)/2, H - (3*h1))
color = 'rgb(255, 255, 255)' # black color

# draw the text on the background
draw.text((x, y), identitas, fill=color, font=font)

timestamp = str(datetime.now())
w2, h2 = draw.textsize(timestamp, font=font)
(x, y) = ((W-w2)/2, H - (2*h1))
color = 'rgb(255, 255, 255)' # black color
draw.text((x, y), timestamp, fill=color, font=font)
 
# save the edited image
image.save('soal1.png')

original.save('soal1.gif', save_all=True, append_images=[image], optimize=False, duration=500, loop=0)
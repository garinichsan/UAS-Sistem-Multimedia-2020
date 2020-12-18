# import required classes
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
 
# create Image object with the input image
pemandangan = Image.open('pemandangan.png')
W, H =  pemandangan.size
 
# initialise the drawing context with
# the image object as background
draw = ImageDraw.Draw(pemandangan)

# create font object with the font file and 
# specify desired size
font = ImageFont.truetype('Montserrat-Regular.ttf', size=30)
# specify desired color
color = 'rgb(0, 0, 0)' # black color

# create the text
identitas = "18218050 - Garin Ichsan Nugraha"
timestamp = str(datetime.now())

# starting position of the text
w1, h1 = draw.textsize(identitas, font=font)
(x1, y1) = ((W-w1)/2, (h1))
w2, h2 = draw.textsize(timestamp, font=font)
(x2, y2) = ((W-w2)/2, (2*h1))

# draw the text on the background
draw.text((x1, y1), identitas, fill=color, font=font)
draw.text((x2, y2), timestamp, fill=color, font=font)

# save the watermarked pemandangan
pemandangan.save('soal3.png')

# get the foto
foto = Image.open('foto.png')
resizedFoto = foto.resize((W, H))

# blend with aplpha value
alpha2 = Image.blend(pemandangan, resizedFoto, alpha=.2)
alpha5 = Image.blend(pemandangan, resizedFoto, alpha=.5)
alpha8 = Image.blend(pemandangan, resizedFoto, alpha=.8)

# save the edited image
alpha2.save('soal3-alpha2.png')
alpha5.save('soal3-alpha5.png')
alpha8.save('soal3-alpha8.png')

# Importing Image and ImageFont, ImageDraw module from PIL package  
from PIL import Image, ImageDraw  

from Textoinator import Textoinator

# This prepares the text for the image processing
font_size = 14
font_processor = Textoinator(r'font\\RobotoMono-Regular.ttf', font_size)
text = 'Sometimes \ngrass is grenner\n where we are not, but this does not mean you can do what you\n want anywhere :D, do what you can in the present moment. \n As that\'s the only thing you can control.'
processed_text = font_processor.process_text(text)

print(processed_text)

# creating a image object with pillow of width 384 and height of font size * number of lines
image = Image.new('RGB', (384, font_size * len(processed_text)), color = 'white')
draw = ImageDraw.Draw(image)

# writing the processed_text array to the image each iteration is a new line
for i in range(len(processed_text)):
    draw.text((5, font_size * i), processed_text[i], font = font_processor.font, align ="left")

# Display the image
image.show()

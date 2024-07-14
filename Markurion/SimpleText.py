from PIL import Image, ImageDraw  
from Textoinator import Textoinator

# This prepares the text for the image processing
font_size = 15
font_processor = Textoinator(r'font\\RobotoMono-Regular.ttf', font_size)
text =  'And this still does not work as expected. And this a meabe not don\'t really know still does not work as expected. \nAnd this still does not work as expected. And this still does not work as expected.'
processed_text = font_processor.process_text(text)

# Split text into array of new lines \n
processed_text = text.splitlines()

# Create an image object with pillow of width 384 and height of font size * number of lines
print_width = 384
print_height = font_size * len(processed_text) + 6
image = Image.new('RGB', (print_width, print_height), color = 'white')
draw = ImageDraw.Draw(image)

# writing the processed_text array to the image each iteration is a new line
for i in range(len(processed_text)):
    draw.text((5, font_size * i), processed_text[i], font = font_processor.getFont(), align="center", fill="black")

# Save the image
image.show()
image.save('text.png')
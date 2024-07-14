from PIL import ImageFont
class Textoinator:
    def __init__(self, font_path, font_size):
        self.font_size = font_size
        self.font_path = font_path
        self.font = ImageFont.truetype(self.font_path, self.font_size)
    
    def getFont(self):
        return self.font
        
    def process_text(self, text): 
        aray = text.split(' ')
        fin = []

        def loop():
            # One iteration
            internal_counter = 0
            temp = []

            # Check the length of entire word
            for x in range(len(aray)):
                iter = aray[x]
                temp.append(iter)
                single_size = self.font.getlength(iter)
                internal_counter += single_size

                # If words reach 280 reset the counter and stop this for
                if internal_counter > 240:
                    internal_counter = 0
                    break

            # Take temp array and remove existing words from original array
            text_temp = ''
            for x in range(len(temp)):
                aray.remove(temp[x])
                text_temp += temp[x] + ' '

            # Append left text to the final array
            fin.append(text_temp)

        while len(aray) > 0:
            loop()

        print("Check the final array")
        # Check if there are any new line characters and split
        # For each occurance of \n split the text and insert it to the final array
        
        # brand_new = []
        # for x in range(len(fin)):
        #     if '\n' in fin[x]:
        #         # Handle multiple new lines
        #         temp = fin[x].split('\n')
        #         for t in temp:
        #             brand_new.append(t)
        #     else:
        #         brand_new.append(fin[x])
                
        # return brand_new
        return fin

# Example usage
if __name__ == '__main__':
    font_processor = Textoinator(r'font\\RobotoMono-Regular.ttf', 14)
    text = 'Sometimes grass is grenner where we are not, but this does not mean you can do what you want anywhere :D, do what you can in the present moment. As that\'s the only thing you can control.'
    processed_text = font_processor.process_text(text)
    print(processed_text)
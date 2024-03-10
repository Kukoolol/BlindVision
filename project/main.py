

from PIL import Image
import pytesseract
import pyfirmata
import time




# Path to Tesseract executable (change this if needed)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
class TextExtractor:
    def __init__(self, image_path):
        self.image_path = image_path
    
    def open_image(self):
        return Image.open(self.image_path)
    
    def extract_text(self, image):
        return pytesseract.image_to_string(image)
    
    def clean_text(self, text):
        return text.strip()
    
    def print_text(self, text):
        print("Extracted Text:")
        print(text)


def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        return text.strip()

# Path to the image file
image_path = '/Users/naren/project/optical-character-recognition-ocr.jpeg'

# Extract text from the image
extracted_text = extract_text_from_image(image_path)
text_list = [char for char in extracted_text]
print(text_list)
#Print hte extracted text

def char_to_braille(char):
    braille_dict = {
        'a': [[1, 0], [0, 0], [0, 0]],
        'b': [[1, 0], [1, 0], [0, 0]],
        'c': [[1, 0], [0, 1], [0, 0]],
        'd': [[1, 0], [0, 1], [1, 0]],
        'e': [[1, 0], [0, 0], [1, 0]],
        'f': [[1, 0], [1, 1], [0, 0]],
        'g': [[1, 0], [1, 1], [1, 0]],
        'h': [[1, 0], [1, 0], [1, 0]],
        'i': [[0, 1], [1, 0], [0, 0]],
        'j': [[0, 1], [1, 0], [1, 0]],
        'k': [[1, 1], [0, 0], [0, 0]],
        'l': [[1, 1], [1, 0], [0, 0]],
        'm': [[1, 1], [0, 1], [0, 0]],
        'n': [[1, 1], [0, 1], [1, 0]],
        'o': [[1, 1], [0, 0], [1, 0]],
        'p': [[1, 1], [1, 1], [0, 0]],
        'q': [[1, 1], [1, 1], [1, 0]],
        'r': [[1, 1], [1, 0], [1, 0]],
        's': [[0, 1], [1, 1], [0, 0]],
        't': [[0, 1], [1, 1], [1, 0]],
        'u': [[1, 1], [0, 0], [1, 1]],
        'v': [[1, 1], [1, 0], [1, 1]],
        'w': [[0, 1], [1, 0], [1, 1]],
        'x': [[1, 1], [0, 1], [1, 1]],
        'y': [[1, 1], [0, 1], [1, 1]],
        'z': [[1, 1], [0, 0], [1, 1]],
        '0': [[0, 1], [1, 0], [1, 1]],
        '1': [[1, 0], [0, 0], [0, 1]],
        '2': [[1, 0], [1, 0], [0, 1]],
        '3': [[1, 0], [0, 1], [0, 1]],
        '4': [[1, 0], [0, 1], [1, 1]],
        '5': [[1, 0], [0, 0], [1, 1]],
        '6': [[1, 0], [1, 1], [0, 1]],
        '7': [[1, 0], [1, 1], [1, 1]],
        '8': [[1, 0], [1, 1], [0, 1]],
        '9': [[0, 1], [1, 0], [0, 1]],
        '!': [[0, 0], [1, 1], [0, 1]],
        '?': [[0, 0], [1, 1], [1, 0]],
        ',': [[0, 0], [0, 1], [0, 0]],
        '.': [[0, 0], [1, 0], [1, 0]],
        ' ': [[0, 0], [0, 0], [0, 0]]
    }
    return braille_dict.get(char.lower(), [[0, 0], [0, 0], [0, 0]])

def text_to_braille(text):
    result = []
    for char in text:
        result.append(char_to_braille(char))
    return result

def print_braille(braille):
    for i in range(3):
        line = ''
        for cell in braille:
            line += '1' if cell[i][0] else '0'
            line += '1' if cell[i][1] else '0'
            line += '\n'
        print(line+'\n')


braille_representation = text_to_braille(extracted_text)




import serial

try:
    SerialObj = serial.Serial('/dev/cu.usbmodem11101') # COMxx  format on Windows
                    
    SerialObj.baudrate = 9600  # set Baud rate to 9600
    SerialObj.bytesize = 8   # Number of data bits = 8
    SerialObj.parity  ='N'   # No parity
    SerialObj.stopbits = 1   # Number of Stop bits = 1
    time.sleep(5)
    for letter in text_list:
        SerialObj.write(letter.lower().encode())    #transmit 'A' (8bit) to micro/Arduino
        time.sleep(1)
except:
    print("\nBraille representation:")
    braille_dict = {
        'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑',
        'F': '⠋', 'G': '⠛', 'H': '⠓', 'I': '⠊', 'J': '⠚',
        'K': '⠅', 'L': '⠇', 'M': '⠍', 'N': '⠝', 'O': '⠕',
        'P': '⠏', 'Q': '⠟', 'R': '⠗', 'S': '⠎', 'T': '⠞',
        'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭', 'Y': '⠽',
        'Z': '⠵',
        
        '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
        '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
        
        '.': '⠲', ',': '⠂', ';': '⠆', '?': '⠦', '!': '⠖',
        "'": '⠄', '"': '⠐⠄', '-': '⠤', '(': '⠐⠣', ')': '⠐⠜',
        '[': '⠦⠴', ']': '⠦⠦', '*': '⠔', '/': '⠸⠌', '&': '⠯'
    }


    
    braille_text = ''.join(braille_dict.get(char.upper(), char) for char in extracted_text)
    print(braille_text)
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nConnection to Arduino Failure: Try Checking Port Number / Reconnect\n\n\n\n\n\n\n\n")
    raise
    



    
    

# board = pyfirmata.Arduino('/dev/cu.usbmodem11101')



# while True:

#     for braille in braille_representation:
#         board.digital[2].write(braille[0][0])
#         board.digital[3].write(braille[0][1])
#         board.digital[4].write(braille[1][0])
#         board.digital[5].write(braille[1][1])
#         board.digital[6].write(braille[2][0])
#         board.digital[7].write(braille[2][1])

    

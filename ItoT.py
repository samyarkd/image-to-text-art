from pywhatkit import image_to_ascii_art
import os

x = 0
while x == 0:

    image= input('image path: ')
    if os.path.exists(image):
        x = 1
    else: print('No such file or dir !! Try agin')
    
text = 'art.txt'

image_to_ascii_art(image, text)

file = open('art.txt', 'r')
x = file.read()
print(x)

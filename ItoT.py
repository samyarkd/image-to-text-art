from pywhatkit import image_to_ascii_art
    

image= input('image path: ')
text = 'art.txt'

image_to_ascii_art(image, text)

file = open('art.txt', 'r')
x = file.read()
print(x)
import os
from os import listdir

folder_dir = "/home/alex_gray/VS COde/MTGCards_tesseract-ocr-main"

for images in os.listdir("/home/alex_gray/VS COde/image/"):
    if (images.endswith(".jpg")):
        print (images)
        command = ('tesseract image/' + images + ' title')
        os.system(command)
        with open('title.txt') as f:
            title = f.readline()
        output = open("output.txt", "a")
        output.write(title)
        output.close()
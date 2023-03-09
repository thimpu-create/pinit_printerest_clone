import os
from PIL import Image
from pathlib import Path
res = []

res = [file for file in os.listdir('pins') if not file.find('m4v') > 0] 
    # res.append(file)

# print(res)
for img in res:
    pic = Image.open('pins/' + img)
    size = (500, 500)
    pic.thumbnail(size, Image.ANTIALIAS)
    pic.save('pins/' + img)
print('done')
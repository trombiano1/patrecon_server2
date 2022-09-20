import numpy as np
import sys
from PIL import Image

# print numpy array in full
# np.set_printoptions(threshold=sys.maxsize)

# set width and height 
w, h = 1024, 1024

result = []

for i in range (1, 201):
    if i % 4 != 0:
        continue

    filename = 'ct_no_tumor_phantom/001/1-001-0%s.img' % f'{i:03}'

    with open(filename, 'rb') as f: 
        # Seek backwards from end of file by 2 bytes per pixel 
        f.seek(-w*h*2, 2) 
        img = np.fromfile(f, dtype=np.uint16).reshape((h,w)) 

    img = Image.fromarray(img)
    img = img.convert("F")
    img = img.resize((128,128), Image.ANTIALIAS)
    if len(result) < 46:
        result.append(np.array(img))

np.array(result).astype('float32').tofile('ct_no_tumor_phantom.bin')
print(len(result))
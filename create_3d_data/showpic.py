import os
import numpy as np
import matplotlib.pyplot as plt

model_path = os.path.join('3D_CT2.bin')
ct3d = np.fromfile(model_path, dtype=np.float32)
ctslices = np.reshape(ct3d, (-1, 128, 128))

print(ctslices)
gt = ctslices[20, :, :]

plt.imshow(gt, interpolation='none', cmap='gray')
plt.savefig('test.png')
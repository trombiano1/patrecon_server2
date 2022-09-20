import os
import numpy as np
import matplotlib.pyplot as plt

model_path = os.path.join('./exp/data/3D_CT.bin')
ct3d = np.fromfile(model_path, dtype=np.float32)
ctslices = np.reshape(ct3d, (-1, 128, 128))

gt = ctslices[100, :, :]

plt.imshow(gt, interpolation='none', cmap='gray')
plt.savefig('test.png')
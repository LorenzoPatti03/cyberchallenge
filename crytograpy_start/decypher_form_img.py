import numpy as np
from PIL import Image
import os

folder = "/home/lorenzopatti/Scaricati/"


c1 = np.array(Image.open(os.path.join(folder, "flag_enc.png")).convert('L'))
c2 = np.array(Image.open(os.path.join(folder, "notflag_enc.png")).convert('L'))

diff = np.bitwise_xor(c1, c2)

Image.fromarray(diff).save('P1_xor_P2.png')
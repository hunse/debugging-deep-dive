import datetime

import numpy as np

# print(f"Time 0: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

a = np.random.uniform(-1, 1, size=(1000, 1000))

AA = a @ a.T

u, s, v = np.linalg.svd(a)

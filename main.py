import numpy as np
import random
import matplotlib.pyplot as plt
from sequence_gen import *
from state_gen import *


n_features=10
n_states=20
spacing_between_shapes = 2


x,y, z = sequence_gen(n_features, n_states, spacing_between_shapes)
xx,yy,zz = state_gen(n_features)
print(x)
print(y)
print(z)
plt.plot(x)
plt.plot(z)
plt.show()
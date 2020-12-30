# This function randomly generates different states for our environment
# 0 = trinagle, 1 = rectangle and 2 = curve
import numpy as np
from make_shapes import *

def state_gen(n_features):

    label = [0]
    state = [0]
    full_len_label = np.zeros((n_features,1), dtype=int)
    shape_type = np.random.choice(['triangle', 'rectangle', 'curve'])
    if shape_type == 'triangle':
        state = create_triangle(n_features, slope = 0.5)
        label = 0
    elif shape_type == 'rectangle':
        state = create_rectangle(n_features, height = n_features / 2)
        label = 1
    elif shape_type == 'curve':
        state = create_curve(n_features, radius = n_features / 2)
        label = 2
    else:
        print('non-defined shape type')
        print('we have {} features'.format(n_features))

    for j in range(n_features):
        full_len_label[j][0] = label

    #print(state)
    #rint(label)
    #print(full_len_label)
    return(np.transpose(state), label, full_len_label)


# This function randomly generates different states for our environment
# 0 = trinagle, 1 = rectangle and 2 = curve
import numpy as np
from make_shapes import *

def sequence_gen(n_features, n_states, spacing_between_shapes):
    states = np.zeros((n_states,n_features), dtype=float)
    labels = np.zeros((n_states,1), dtype=float)
    states_sequence = []
    full_len_labels = np.zeros(((n_features*n_states)+(n_states*spacing_between_shapes), 1), dtype=float)
    s = 0
    for i in range(n_states):
        shape_type = np.random.choice(['triangle', 'rectangle', 'curve'])
        if shape_type == 'triangle':
            states [i] = create_triangle(n_features, slope = 0.5)
            labels[i][0] = 0
            for j in range(n_features):
                full_len_labels[j+(i*n_features)+(s*spacing_between_shapes)][0] = labels[i]
                if j == (n_features-1):
                    s += 1
        elif shape_type == 'rectangle':
            states[i] = create_rectangle(n_features, height = n_features/2)
            labels[i][0] = 1
            for j in range(n_features):
                full_len_labels[j+(i*n_features)+(s*spacing_between_shapes)][0] = labels[i]
                if j == (n_features-1):
                    s += 1
        elif shape_type == 'curve':
            states[i] = create_curve(n_features, radius = n_features/2)
            labels[i][0] = 2
            for j in range(n_features):
                full_len_labels[j+(i*n_features)+(s*spacing_between_shapes)][0] = labels[i]
                if j == (n_features-1):
                    s += 1
        else:
            print('non-defined shape type')
            print('we have {} features'.format(n_features))

    # Number 2 in range parenthesis is the blank space between states in a sequence for better visualization
    # to show the sequence as the output, uncomment the code below and change the return variable to states_sequence

        for k in range(n_features + spacing_between_shapes):
            if k < n_features:
                states_sequence.append(states[i][k])
            else:
                states_sequence.append(0)





    #print(states)
    #print(labels)
    #print(states_sequence)
    return(states_sequence , labels, full_len_labels)


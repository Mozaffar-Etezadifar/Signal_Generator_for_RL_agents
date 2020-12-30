# This function creates the shape of the triangle, rectangle and curve with the length of n_features and returns its values

import numpy as np
import math

def create_triangle(n_features, slope):
    values = np.zeros((1,n_features),dtype=float)
    for j in range(n_features):
        values [0][j] = j * slope
    return (values)

def create_rectangle(n_features, height):
    values = np.zeros((1,n_features),dtype=float)
    for j in range(n_features):
        values [0][j] = height
    return (values)

def create_curve(n_features, radius):
    values = np.zeros((1,n_features),dtype=float)
    for j in range(n_features):
        values [0][j] = math.sqrt((radius**2)-(abs((j)-(n_features/2))**2))
    return (values)
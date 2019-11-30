import numpy as np
import pylab as pb

from math import pi
from scipy.spatial.distance import cdist

W = np.array([0.5, -1.5])
# W = np.transpose([W])

X = np.linspace(-1.0, 1.0, num=201)
X = np.vstack([X, np.ones_like(X)])
# X = np.transpose(X)

f = np.dot(W, X)
# f = np.dot(X, W)
# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""
import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    poly = np.ones(x.shape[0])
    for deg in range(1, degree+1):
        poly = np.c_[poly, x**deg]
    return poly

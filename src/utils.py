"""工具函数"""
import numpy as np

def calculate_2d_distance(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calculate_rms(errors):
    return np.sqrt(np.mean(errors**2))

def calculate_cep(errors_x, errors_y, percentile=0.95):
    radial_errors = np.sqrt(errors_x**2 + errors_y**2)
    return np.percentile(radial_errors, percentile * 100)}
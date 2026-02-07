"""RTK定位模拟器"""
import numpy as np
from enum import Enum
import random

class RTKStatus(Enum):
    FIXED = 4
    FLOAT = 5
    SINGLE = 1
    NO_SIGNAL = 0

class RTKSimulator:
    def __init__(self, fixed_accuracy_h=0.02, fixed_accuracy_v=0.03,
                 float_accuracy_h=0.5, single_accuracy_h=2.5,
                 fixed_rate=0.98, update_rate=10.0):
        self.fixed_accuracy_h = fixed_accuracy_h
        self.fixed_accuracy_v = fixed_accuracy_v
        self.float_accuracy_h = float_accuracy_h
        self.single_accuracy_h = single_accuracy_h
        self.fixed_rate = fixed_rate
        self.update_rate = update_rate
        self.dt = 1.0 / update_rate
        self.current_status = RTKStatus.FIXED
        
    def add_positioning_error(self, true_position, status=None):
        if status is None:
            status = self._simulate_status()
        
        x, y, z = true_position
        
        if status == RTKStatus.FIXED:
            error_x = np.random.normal(0, self.fixed_accuracy_h)
            error_y = np.random.normal(0, self.fixed_accuracy_h)
            error_z = np.random.normal(0, self.fixed_accuracy_v)
        elif status == RTKStatus.FLOAT:
            error_x = np.random.normal(0, self.float_accuracy_h)
            error_y = np.random.normal(0, self.float_accuracy_h)
            error_z = np.random.normal(0, self.float_accuracy_h * 1.5)
        elif status == RTKStatus.SINGLE:
            error_x = np.random.normal(0, self.single_accuracy_h)
            error_y = np.random.normal(0, self.single_accuracy_h)
            error_z = np.random.normal(0, self.single_accuracy_h * 2)
        else:
            return (np.nan, np.nan, np.nan)
        
        if random.random() < 0.05:
            bias = np.random.uniform(0.1, 0.3)
            error_x += bias
            error_y += bias
        
        return (x + error_x, y + error_y, z + error_z)
    
    def _simulate_status(self):
        if self.current_status == RTKStatus.FIXED:
            if random.random() > self.fixed_rate:
                self.current_status = RTKStatus.FLOAT
        elif self.current_status == RTKStatus.FLOAT:
            if random.random() < 0.7:
                self.current_status = RTKStatus.FIXED
            elif random.random() < 0.1:
                self.current_status = RTKStatus.SINGLE
        elif self.current_status == RTKStatus.SINGLE:
            if random.random() < 0.5:
                self.current_status = RTKStatus.FLOAT
        return self.current_status

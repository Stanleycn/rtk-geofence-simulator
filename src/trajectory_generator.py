"""轨迹生成器"""
import numpy as np
import math

class TrajectoryGenerator:
    def __init__(self, start_position=(0, 0)):
        self.start_position = start_position
        
    def generate_straight_line(self, length, speed, dt=0.1, angle=0):
        duration = length / speed
        num_points = int(duration / dt)
        angle_rad = math.radians(angle)
        dx = speed * dt * math.cos(angle_rad)
        dy = speed * dt * math.sin(angle_rad)
        
        trajectory = []
        x, y = self.start_position
        
        for i in range(num_points):
            t = i * dt
            trajectory.append((x, y, t))
            x += dx
            y += dy
        return trajectory
    
    def generate_boundary_crossing(self, boundary_point, crossing_angle, 
                                   speed, total_distance=50.0, dt=0.1):
        bx, by = boundary_point
        angle_rad = math.radians(crossing_angle)
        start_x = bx - (total_distance / 2) * math.cos(angle_rad)
        start_y = by - (total_distance / 2) * math.sin(angle_rad)
        self.start_position = (start_x, start_y)
        return self.generate_straight_line(total_distance, speed, dt, crossing_angle)
"""电子围栏引擎"""
import numpy as np
from shapely.geometry import Point, Polygon
from enum import Enum

class GeofenceEvent(Enum):
    INSIDE = 0
    OUTSIDE = 1
    CROSSING_IN = 2
    CROSSING_OUT = 3

class GeofenceEngine:
    def __init__(self, boundary_points):
        self.boundary_points = boundary_points
        self.polygon = Polygon(boundary_points)
        self.last_status = None
        
    def check_point(self, point):
        p = Point(point[0], point[1])
        return self.polygon.contains(p)
    
    def detect_crossing(self, point):
        is_inside = self.check_point(point)
        distance = self.distance_to_boundary(point)
        event = GeofenceEvent.INSIDE if is_inside else GeofenceEvent.OUTSIDE
        
        if self.last_status is not None:
            if self.last_status and not is_inside:
                event = GeofenceEvent.CROSSING_OUT
            elif not self.last_status and is_inside:
                event = GeofenceEvent.CROSSING_IN
        
        self.last_status = is_inside
        return event, distance
    
    def distance_to_boundary(self, point):
        p = Point(point[0], point[1])
        distance = p.distance(self.polygon.boundary)
        if self.polygon.contains(p):
            return distance
        else:
            return -distance
import math


def calculate_angle(p1x, p1y, p2x, p2y, p3x, p3y):
    numerator = p2y * (p1x - p3x) + p1y * (p3x - p2x) + p3y * (p2x - p1x)
    denominator = (p2x - p1x) * (p1x - p3x) + (p2y - p1y) * (p1y - p3y)
    ratio = numerator / denominator

    angle_rad = math.atan(ratio)
    angle_deg = (angle_rad * 180) / math.pi;

    if(angle_deg < 0):
        angle_deg = 180 + angle_deg

    return angle_deg
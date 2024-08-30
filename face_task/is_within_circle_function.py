# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:21:45 2024

@author: bsms9zh8
"""

# Function to check if the cross is within the circle
def is_within_circle(cross_pos, circle_radius):
    return (cross_pos[0]**2 + cross_pos[1]**2) <= circle_radius**2
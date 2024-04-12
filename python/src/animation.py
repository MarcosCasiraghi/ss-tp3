import math

import cv2

from src.util import *
import numpy as np


def draw_new_frame(particle_data: [], obstacle_data: [], height: int, width: int, particle_radius: int,
                   obstacle_radius: int, size_multiplier: int):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255
    for particle in particle_data:
        cv2.circle(frame, (int(particle[X] * size_multiplier), int(particle[Y] * size_multiplier)),
                   radius=particle_radius,
                   color=(0, 0, 255), thickness=-1)
    for obstacle in obstacle_data:
        cv2.circle(frame, (int(obstacle[X] * size_multiplier), int(obstacle[Y] * size_multiplier)),
                   radius=obstacle_radius,
                   color=(0, 255, 0), thickness=-1)
    return frame


def animate(particle_filename: str, static_data_filename: str, size_multiplier: int):
    particle_data = get_particle_data(particle_filename)
    static_data = get_static_data(static_data_filename)

    fps = 30

    particle_radius, obstacle_radius = int(static_data['pr'] * size_multiplier), int(
        static_data['or'] * size_multiplier)
    width, height = int(static_data['l'] * size_multiplier), int(static_data['l'] * size_multiplier)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('../animations/simulation_video.mp4', fourcc, fps, (width, height))

    for pd in particle_data:
        frame = draw_new_frame(pd[PARTICLES], pd[OBSTACLES], height, width, particle_radius, obstacle_radius, size_multiplier)
        out.write(frame)

    out.release()

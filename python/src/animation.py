import cv2

from src.util import *
import numpy as np


def generate_intermediate_positions(prev: [], post: [], steps: int):        # TODO: ver como hacerlo accurate
    resp = [[] for _ in range(steps)]
    for past, present in zip(prev, post):
        dx = (present[X] - past[X]) / steps
        dy = (present[Y] - past[Y]) / steps

        for i in range(steps):
            resp[i].append([past[X] + i * dx, past[Y] + i * dy])

    return resp


def draw_new_frame(particle_data: [], obstacle_data: [], height: int, width: int, size_multiplier: int):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255
    for particle in particle_data:
        cv2.circle(frame, (int(particle[X] * size_multiplier), int(particle[Y] * size_multiplier)), radius=4,  # TODO: CHANGE
                   color=(0, 0, 255), thickness=-1)
    for obstacle in obstacle_data:
        cv2.circle(frame, (int(obstacle[X] * size_multiplier), int(obstacle[Y] * size_multiplier)), radius=20,  # TODO: CHANGE
                   color=(0, 255, 0), thickness=-1)
    return frame

def animate(particle_filename: str, static_data_filename: str, size_multiplier: int):
    particle_data = get_particle_data(particle_filename)
    static_data = get_static_data(static_data_filename)

    fps = 30
    steps = 4
    screen_size = int(static_data['l'])
    width, height = screen_size * size_multiplier, screen_size * size_multiplier
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('../animations/simulation_video.mp4', fourcc, fps, (width, height))

    i = 0
    while i + 1 < len(particle_data):

        particle_intermediate_range = generate_intermediate_positions(particle_data[i][PARTICLES], particle_data[i+1][PARTICLES], steps)
        obstacle_intermediate_range = generate_intermediate_positions(particle_data[i][OBSTACLES], particle_data[i+1][OBSTACLES], steps)

        for p_i, o_i in zip(particle_intermediate_range, obstacle_intermediate_range):
            frame = draw_new_frame(p_i, o_i, height, width, size_multiplier)
            out.write(frame)

        i += 1

    out.release()

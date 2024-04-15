import cv2

from src.util import *
import numpy as np
from src.collisions import count_collisions, COUNT_ONCE, COUNT_MANY


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

    fps = 60

    particle_radius, obstacle_radius = int(static_data['pr'] * size_multiplier), int(
        static_data['or'] * size_multiplier)
    width, height = int(static_data['l'] * size_multiplier), int(static_data['l'] * size_multiplier)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('../animations/simulation_video.mp4', fourcc, fps, (width, height))

    for pd in particle_data:
        frame = draw_new_frame(pd[PARTICLES], pd[OBSTACLES], height, width, particle_radius, obstacle_radius, size_multiplier)
        out.write(frame)

    out.release()


def animate_with_collisions(particle_filename: str, static_data_filename: str, size_multiplier: int, collision_type: int):
    particle_data = get_particle_data(particle_filename)
    static_data = get_static_data(static_data_filename)

    fps = 60
    particle_radius, obstacle_radius = int(static_data['pr'] * size_multiplier), int(
        static_data['or'] * size_multiplier)
    width, height = int(static_data['l'] * size_multiplier), int(static_data['l'] * size_multiplier)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('../animations/simulation_video.mp4', fourcc, fps, (width, height))

    collision_times, collision_ids = count_collisions(particle_data, collision_type)
    particle_ids = set()
    collision_amount = 0
    for pd in particle_data:

        if collision_times.__contains__(pd[TIME]):
            collision_amount += 1
            index = collision_times.index(pd[TIME])
            particle_ids.add(collision_ids[index])

        frame = draw_new_frame_with_collisions(pd[PARTICLES], pd[OBSTACLES], height, width, particle_radius,
                                               obstacle_radius, size_multiplier, collision_amount, particle_ids, collision_type)
        out.write(frame)

    out.release()


def draw_new_frame_with_collisions(particle_data: [], obstacle_data: [], height: int, width: int,
                                   particle_radius: int, obstacle_radius: int, size_multiplier: int,
                                   collision_amount: int, collision_ids: set, collision_type):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255
    for idx, particle in enumerate(particle_data):
        if collision_type == COUNT_ONCE and collision_ids.__contains__(idx):
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        cv2.circle(frame, (int(particle[X] * size_multiplier), int(particle[Y] * size_multiplier)),
                   radius=particle_radius,
                   color=color, thickness=-1)
    for obstacle in obstacle_data:
        cv2.circle(frame, (int(obstacle[X] * size_multiplier), int(obstacle[Y] * size_multiplier)),
                   radius=obstacle_radius,
                   color=(0, 255, 0), thickness=-1)
    text = f'Cantidad de colisiones: {collision_amount}'
    cv2.putText(frame, text, (int(width / 2) - len(text) * 7, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                2, cv2.LINE_AA)
    return frame


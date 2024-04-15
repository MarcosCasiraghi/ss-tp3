import math

from src.collisions import find_collision_with_wall_or_obstacle, is_wall_collision
from util import *


def get_collision_velocities(particle_data: []):
    wall_collision_times = []
    wall_collision_velocities = []

    obstacle_collision_times = []
    obstacle_collision_velocities = []

    i = 0
    while i + 1 < len(particle_data):
        time = particle_data[i][TIME]
        prev = particle_data[i][PARTICLES]
        post = particle_data[i + 1][PARTICLES]

        index = find_collision_with_wall_or_obstacle(prev, post)

        if index is not None:  # Es colision de pared o de obstaculo
            particle_pre = prev[index]
            particle_post = post[index]

            # Caso: colisiono de particula con pared
            if is_wall_collision(particle_pre, particle_post):
                wall_collision_times.append(time)
                wall_collision_velocities.append(get_collision_speed_with_wall(particle_pre, particle_post))

            # Caso: colisiono de particula con el obstaculo
            else:
                obstacle_collision_times.append(time)
                obstacle_collision_velocities.append(get_collision_speed_with_obstacle(particle_pre))

        i = i + 1

    return wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities


def get_collision_speed_with_wall(particle_pre: [float], particle_post: [float]) -> float:
    if particle_pre[VX] == - particle_post[VX]:
        return abs(particle_pre[VX])
    else:
        return abs(particle_pre[VY])


def get_collision_speed_with_obstacle(particle_pre: [float]) -> float:
    # Calculamos la velocidad normal al choque
    return math.sqrt(particle_pre[VX] ** 2 + particle_pre[VY] ** 2)  # TODO: CHEEEECK!


def generate_pressure_bins(collision_times: [], collision_velocities: [], delta_t: float, particle_mass: float, length: float):
    pressures = []

    impulse_accumulator = 0
    delta_t_accumulated = delta_t
    for v, vt in zip(collision_velocities, collision_times):
        impulse_accumulator += v
        if vt > delta_t_accumulated:
            pressures.append(
                (impulse_accumulator * particle_mass) / (delta_t * length))  # TODO: check pq dice por unidad de area
            impulse_accumulator = 0
            delta_t_accumulated += delta_t

    return pressures


def average_pressure(collision_times: [], collision_velocities: [], particle_mass: float, length: float) -> float:
    impulse_accumulator = 0
    for v in collision_velocities:
        impulse_accumulator += v

    return (impulse_accumulator * particle_mass) / (collision_times[-1] * length)

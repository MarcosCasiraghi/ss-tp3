import math
from util import *


def get_collision_velocities(particle_filename: str):
    particle_data = get_particle_data(particle_filename)

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

        if index:  # Es colision de pared o de obstaculo
            particle_pre = prev[index]
            particle_post = post[index]

            # Caso: colisiono de particula con pared
            if is_wall_collision(particle_pre, particle_post):
                wall_collision_times.append(time)
                wall_collision_velocities.append(get_collision_with_wall(particle_pre, particle_post))

            # Caso: colisiono de particula con el obstaculo
            else:
                obstacle_collision_times.append(time)
                obstacle_collision_velocities.append(get_collision_with_obstacle(particle_pre))

        i = i + 1

    return wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities


def is_wall_collision(particle_pre: [float], particle_post: [float]) -> bool:
    # TODO check: esto es suficiente para ver si es colision
    return ((particle_pre[VX] == - particle_post[VX] and particle_pre[VY] == particle_post[VY]) or
            (particle_pre[VX] == particle_post[VX] and particle_pre[VY] == - particle_post[VY]))


def find_collision_with_wall_or_obstacle(prev_array: [float], post_array: [float]) -> [int]:
    idx = None
    count = 0
    for i, (prev, post) in enumerate(zip(prev_array, post_array)):
        # Si alguna de las velocidades es distinta, es porque colisiono
        if prev[VX] != post[VX] or prev[VY] != post[VY]:
            idx = i
            count += 1

    return idx if count == 1 else None


def get_collision_with_wall(particle_pre: [float], particle_post: [float]) -> float:
    if particle_pre[VX] == - particle_post[VX]:
        return abs(particle_pre[VX])
    else:
        return abs(particle_pre[VY])


def get_collision_with_obstacle(particle_pre: [float]) -> float:
    # Calculamos la velocidad normal al choque
    return math.sqrt(particle_pre[VX] ** 2 + particle_pre[VY] ** 2)     # TODO: CHEEEECK!


def calculate_pressure(delta_t, collision_times, collision_velocities):
    num_samples = len(collision_times)
    pressures = []
    current_pressure = 0

    delta_t_accumulated = delta_t

    for i in range(num_samples):
        # Se fija los valores dentro del rango delta t
        if collision_times[i] <= delta_t_accumulated:
            # Todo: revisar si es * 2 o no
            current_pressure += collision_velocities[i] * 2
        else:
            pressures.append(current_pressure / delta_t)
            current_pressure = collision_velocities[i]
            delta_t_accumulated += delta_t

        if i == num_samples - 1:
            pressures.append(current_pressure / delta_t)

    return pressures

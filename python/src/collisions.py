from src.util import *

COUNT_ONCE = 0
COUNT_MANY = 1


def count_collisions(particle_data: [], collision_type: int) -> []:
    collision_ids = set()

    collision_times = []    # cada vez que hay una colision, se registra el tiempo

    i = 0
    while i + 1 < len(particle_data):
        time = particle_data[i][TIME]
        prev = particle_data[i][PARTICLES]
        post = particle_data[i + 1][PARTICLES]

        index = find_collision_with_wall_or_obstacle(prev, post)

        if index and not is_wall_collision(prev[index], post[index]):
            if collision_type == COUNT_ONCE:
                if index not in collision_ids:
                    collision_times.append(time)
                    collision_ids.add(index)
            else:
                collision_times.append(time)

        i = i + 1

    return collision_times


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


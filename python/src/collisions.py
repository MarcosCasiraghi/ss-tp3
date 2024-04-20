from src.util import *
from temperature import calculate_temperature, average_temperature
from matplotlib import pyplot as plt
from graphs import TEMP_UNITS

COUNT_ONCE = 0
COUNT_MANY = 1


def count_collisions(particle_data: [], collision_type: int) -> []:
    collision_ids = set()

    collision_times = []    # cada vez que hay una colision, se registra el tiempo
    ids = []

    i = 0
    while i + 1 < len(particle_data):
        time = particle_data[i][TIME]
        prev = particle_data[i][PARTICLES]
        post = particle_data[i + 1][PARTICLES]

        index = find_collision_with_wall_or_obstacle(prev, post)

        if index is not None and not is_wall_collision(prev[index], post[index]):
            if collision_type == COUNT_ONCE:
                if index not in collision_ids:
                    collision_times.append(time)
                    collision_ids.add(index)
                    ids.append(index)
            else:
                collision_times.append(time)
                ids.append(index)

        i = i + 1

    return collision_times, ids


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


def time_to_collisions_multiple_velocities(particle_files, static_files, percentage_to_reach):
    time_taken_array = []
    temperatures_array = []
    for particle_file, static_file in zip(particle_files, static_files):
        particle_data = get_particle_data(particle_file)
        static_file = get_static_data(static_file)

        temperature_times, temperatures = calculate_temperature(particle_data)

        single_collisions, idx = count_collisions(particle_data, COUNT_ONCE)
        collisions = 0

        time_taken = 0
        for collision_time in single_collisions:
            collisions += 1
            if collisions > static_file['n'] * percentage_to_reach:
                time_taken = collision_time
                break

        index = 0
        for idx, temperature_time in enumerate(temperature_times):
            if temperature_time == time_taken:
                index = idx
                break

        temperature_at_time = temperatures[index]

        time_taken_array.append(time_taken)
        temperatures_array.append(temperature_at_time)

    plt.scatter(temperatures_array, time_taken_array, marker='o', color='blue')
    plt.xlabel(f'Temperatura {TEMP_UNITS}')
    plt.ylabel('Tiempo en alcanzar ' + str(int(percentage_to_reach * 100)) + '% de colisiones unicas (s)')
    plt.grid(True)

    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0), useMathText=True)

    plt.show()


def gradient_against_temperature(particle_files, static_files):
    gradients = []
    temperatures = []
    for particle_file, static_file in zip(particle_files, static_files):
        particle_data = get_particle_data(particle_file)
        static_file = get_static_data(static_file)

        average_temperature_value = average_temperature(particle_data)

        collision_times, ids = count_collisions(particle_data, COUNT_MANY)
        collision_amount = [i for i in range(len(collision_times))]

        xysum = 0
        xsum = 0
        ysum = 0
        xsquaredsum = 0

        for x, y in zip(collision_times, collision_amount):
            xysum += x * y
            xsum += x
            ysum += y
            xsquaredsum += x * x

        n = static_file['n']
        gradient = (n * xysum - xsum * ysum) / (n * xsquaredsum - xsum * xsum)

        gradients.append(gradient)
        temperatures.append(average_temperature_value)

    plt.scatter(temperatures, gradients, marker='o', color='blue')
    plt.xlabel(f'Temperatura {TEMP_UNITS}')
    plt.ylabel('Colisión con obstáculo por unidad de tiempo')
    plt.grid(True)

    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0), useMathText=True)

    plt.show()



import math
from src.dcm import calculate_dcm, calculate_incline
from src.collisions import count_collisions, COUNT_ONCE, COUNT_MANY, time_to_collisions_multiple_velocities, gradient_against_temperature
from src.graphs import *
from src.temperature import average_temperature, calculate_temperature
from src.util import get_all_files, get_static_data, get_particle_data
from src.pressure import get_collision_velocities, generate_pressure_bins, average_pressure
from animation import animate, animate_with_collisions


def ej_1_1():
    static_data = get_static_data(get_all_files('../output-files/static-data')[0])
    particle_data = get_particle_data(get_all_files('../output-files/particle')[0])

    delta_t = 0.03
    wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities = get_collision_velocities(particle_data)

    binned_wall_pressure = generate_pressure_bins(wall_collision_times, wall_collision_velocities, delta_t, static_data['pm'], 4 * static_data['l'])
    binned_obstacle_pressure = generate_pressure_bins(obstacle_collision_times, obstacle_collision_velocities, delta_t, static_data['pm'], 2 * math.pi * static_data['or'])

    pressure_plot(binned_wall_pressure, binned_obstacle_pressure,  delta_t)


def ej_1_2():
    average_pressures = []
    average_stds = []
    average_temperatures = []
    for d_filename, s_filename in zip(get_all_files('../output-files/particle'), get_all_files('../output-files/static-data')):
        static_data = get_static_data(s_filename)
        particle_data = get_particle_data(d_filename)

        wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities = get_collision_velocities(particle_data)

        wall_and_obstacle_pressure = []
        wall_and_obstacle_stds = []

        wall_average_pressure, wall_std = average_pressure(wall_collision_times, wall_collision_velocities, static_data['pm'], 4 * static_data['l'])

        wall_and_obstacle_pressure.append(wall_average_pressure)
        wall_and_obstacle_stds.append(wall_std)

        obstacle_average_pressure, obstacle_std = average_pressure(obstacle_collision_times, obstacle_collision_velocities, static_data['pm'], 2 * math.pi * static_data['or'])

        wall_and_obstacle_pressure.append(obstacle_average_pressure)
        wall_and_obstacle_stds.append(obstacle_std)

        average_pressures.append(wall_and_obstacle_pressure)
        average_stds.append(wall_and_obstacle_stds)
        average_temperatures.append(average_temperature(particle_data))

    temp_pressure_plot(average_temperatures, average_pressures, average_stds)


def ej_1_3():
    # particle_data = get_particle_data(get_all_files('../output-files/particle')[0])
    #
    # single_collisions, ids = count_collisions(particle_data, COUNT_ONCE)
    # collisions_plot(single_collisions)

    time_to_collisions_multiple_velocities(get_all_files('../output-files/particle'), get_all_files('../output-files/static-data'), 0.5)

    # multi_collisions, ids = count_collisions(particle_data, COUNT_MANY)
    # collisions_plot(multi_collisions)
    #
    # gradient_against_temperature(get_all_files('../output-files/particle'), get_all_files('../output-files/static-data'))


def ej_1_4():
    delta_t = 0.01

    dcms_times, avg_dcms = calculate_dcm(
        get_all_files('../output-files/particle'),
        get_all_files('../output-files/static-data'),
        delta_t
    )

    dcm_average_plot(dcms_times, avg_dcms)

    print(f'Slope incline: {calculate_incline(avg_dcms, dcms_times, 0.5)}')


if __name__ == "__main__":
    # ej_1_4()
    ej_1_2()
    # ej_1_3()
    # animate(get_all_files('../output-files/particle')[-1], get_all_files('../output-files/static-data')[-1], 10000)




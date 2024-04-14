import math

from src.graphs import pressure_plot, temperature_plot
from src.temperature import calculate_temperature
from src.util import get_all_files, get_static_data, get_particle_data
from src.pressure import get_collision_velocities, calculate_pressure

if __name__ == "__main__":
    static_data = get_static_data(get_all_files('../output-files/static-data')[-1])
    particle_data = get_particle_data(get_all_files('../output-files/particle')[-1])

    delta_t = 0.05
    wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities = get_collision_velocities(particle_data)

    wall_pressure = calculate_pressure(delta_t, wall_collision_times, wall_collision_velocities, 4 * static_data['l'])
    pressure_plot(wall_pressure, delta_t)

    obstacle_pressure = calculate_pressure(delta_t, obstacle_collision_times, obstacle_collision_velocities, 2 * math.pi * static_data['or'])
    pressure_plot(obstacle_pressure, delta_t)

    temperature_times, temperature = calculate_temperature(particle_data)

    temperature_plot(temperature_times, temperature)



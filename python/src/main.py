import math

from src.dcm import calculate_dcm
from src.graphs import pressure_plot, temperature_plot, dcm_plot, temp_pressure_plot
from src.temperature import calculate_temperature, generate_temperature_bins
from src.util import get_all_files, get_static_data, get_particle_data
from src.pressure import get_collision_velocities, generate_pressure_bins

if __name__ == "__main__":
    static_data = get_static_data(get_all_files('../output-files/static-data')[-1])
    particle_data = get_particle_data(get_all_files('../output-files/particle')[-1])

    delta_t = 0.05
    wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities = get_collision_velocities(particle_data)

    binned_wall_pressure = generate_pressure_bins(wall_collision_times, wall_collision_velocities, delta_t, 4 * static_data['l'], static_data['pm'])
    pressure_plot(binned_wall_pressure, delta_t)

    binned_obstacle_pressure = generate_pressure_bins(delta_t, obstacle_collision_times, obstacle_collision_velocities, 2 * math.pi * static_data['or'])
    pressure_plot(binned_obstacle_pressure, delta_t)

    temperature_times, temperature = calculate_temperature(particle_data)
    temperature_plot(temperature_times, temperature)

    binned_temperature = generate_temperature_bins(temperature_times, temperature, delta_t)

    temp_pressure_plot(binned_temperature, binned_wall_pressure)

    dcm_times, dcms = calculate_dcm(particle_data, static_data['l'])
    dcm_plot(dcm_times, dcms)

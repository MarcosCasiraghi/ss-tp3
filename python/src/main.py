from src.graphs import pressure_plot
from src.util import get_all_files
from src.pressure import get_collision_velocities, calculate_pressure

if __name__ == "__main__":
    delta_t = 0.05
    wall_collision_times, wall_collision_velocities, obstacle_collision_times, obstacle_collision_velocities = get_collision_velocities(get_all_files('../output-files/particle')[-1])

    wall_pressure = calculate_pressure(delta_t, wall_collision_times, wall_collision_velocities)
    pressure_plot(wall_pressure, delta_t)

    obstacle_pressure = calculate_pressure(delta_t, obstacle_collision_times, obstacle_collision_velocities)
    pressure_plot(obstacle_pressure, delta_t)




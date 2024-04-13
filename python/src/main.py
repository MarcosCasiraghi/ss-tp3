from src.animation import animate
from src.util import get_all_files
from src.pressure import get_collision_velocities, calculate_pressure, pressure_plot

if __name__ == "__main__":
    wall_times, wall_velocities, object_times, object_velocities = get_collision_velocities(get_all_files('../output-files/particle')[-1], get_all_files('../output-files/static')[-1])
    wall_pressure = calculate_pressure(0.001, wall_times, wall_velocities)
    pressure_plot(wall_pressure, 0.001)
    # animate(get_all_files('../output-files/particle')[-1], get_all_files('../output-files/static')[-1], 10000)


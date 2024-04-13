from src.graphs import pressure_plot
from src.util import get_all_files
from src.pressure import get_collision_velocities, calculate_pressure

if __name__ == "__main__":
    collision_times, collision_velocities = get_collision_velocities(get_all_files('../output-files/particle')[-1], get_all_files('../output-files/static')[-1])
    wall_pressure = calculate_pressure(0.05, collision_times, collision_velocities)
    pressure_plot(wall_pressure, 0.05)



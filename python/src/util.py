import csv
import glob

TIME = 0
PARTICLES = 1
OBSTACLES = 2
X = 0
Y = 1
VX = 2
VY = 3


def get_particle_data(filename):
    data = []
    current_time = None
    current_timeframe_particles = []
    current_timeframe_obstacles = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].startswith('t:'):
                if current_time:
                    data.append((current_time, current_timeframe_particles, current_timeframe_obstacles))

                current_time = float(row[0].split(':')[1])
                current_timeframe_particles = []
                current_timeframe_obstacles = []
            elif row[0].startswith('par:'):
                x = float(row[1])
                y = float(row[2])
                x_velocity = float(row[3])
                y_velocity = float(row[4])
                current_timeframe_particles.append([x, y, x_velocity, y_velocity])
            elif row[0].startswith('obs:'):
                x = float(row[1])
                y = float(row[2])
                current_timeframe_obstacles.append([x, y])
    return data


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_static_data(file_name: str):
    data = {}

    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            key = row[0]

            if row[1].isdigit():
                value = int(row[1])
            elif is_float(row[1]):
                value = float(row[1])
            else:
                value = True if row[1] == 'true' else False

            data[key] = value
    return data


def get_all_files(prefix: str) -> [str]:
    pattern = f"{prefix}-*.csv"
    return glob.glob(pattern)

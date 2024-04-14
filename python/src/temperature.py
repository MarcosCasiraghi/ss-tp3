import math

from src.util import *


def calculate_temperature(particle_data: []) -> []:
    temperature = []
    temperature_times = []
    for timeframe in particle_data:
        total_speed = 0
        temperature_times.append(timeframe[TIME])

        for particle in timeframe[PARTICLES]:       # NO TOMA EN CUENTA LA VELOCIDAD DEL OBSTACLE
            total_speed += math.sqrt(particle[VX] ** 2 + particle[VY] ** 2)  # TODO: check calculo de temperatura

        temperature.append(total_speed / len(timeframe[PARTICLES]))

    return temperature_times, temperature

import numpy as np
from numpy import ndarray

from src.util import *


def temperature(particle: []):
    return particle[VX] ** 2 + particle[VY] ** 2


def calculate_temperature(particle_data: []) -> ([], []):
    temperatures = []
    temperature_times = []
    for timeframe in particle_data:
        total_temp = 0
        temperature_times.append(timeframe[TIME])

        for particle in timeframe[PARTICLES]:  # NO TOMA EN CUENTA LA VELOCIDAD DEL OBSTACLE
            total_temp += temperature(particle)

        temperatures.append(total_temp)

    return temperature_times, temperatures


def average_temperature(particle_data: []) -> ndarray:
    return np.mean(calculate_temperature(particle_data)[1])



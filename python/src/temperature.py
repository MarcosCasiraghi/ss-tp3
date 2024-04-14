import math

from src.util import *


def temperature(particle: []):
    return math.sqrt(particle[VX] ** 2 + particle[VY] ** 2)  # TODO: check calculo de temperatura


def calculate_temperature(particle_data: []) -> ([], []):
    temperatures = []
    temperature_times = []
    for timeframe in particle_data:
        total_speed = 0
        temperature_times.append(timeframe[TIME])

        for particle in timeframe[PARTICLES]:  # NO TOMA EN CUENTA LA VELOCIDAD DEL OBSTACLE
            total_speed += temperature(particle)

        temperatures.append(total_speed / len(timeframe[PARTICLES]))

    return temperature_times, temperatures


def generate_temperature_bins(temperature_times: [], temperature: [], dt: float) -> []:
    binned_temperature = []

    temperature_accumulator = 0
    dt_accumulator = dt
    count = 0
    for t, ts in zip(temperature, temperature_times):
        temperature_accumulator += t
        count += 1
        if ts > dt_accumulator:
            binned_temperature.append(temperature_accumulator / count)      # TODO: check
            temperature_accumulator = 0
            dt_accumulator += dt
            count = 0

    return binned_temperature






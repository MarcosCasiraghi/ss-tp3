import math

from src.util import *


def dcm(obstacle: [], length: float):
    return math.sqrt((obstacle[X] - length / 2) ** 2 + (obstacle[Y] - length / 2) ** 2)  # TODO: check calculo de dcm


def calculate_dcm(particle_data: [], length: float) -> ([], []):
    dcms = []
    dcm_times = []
    for timeframe in particle_data:
        dcm_times.append(timeframe[TIME])
        dcms.append(dcm(timeframe[OBSTACLES][0], length))

    return dcm_times, dcms

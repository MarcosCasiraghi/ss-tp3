import math

from src.util import *


def dcm(obstacle: [], length: float):
    return (obstacle[X] - length / 2) ** 2 + (obstacle[Y] - length / 2) ** 2


def calculate_dcm(particle_data: [], length: float, delta_t: float) -> []:
    dcms = []
    total_delta_t = delta_t
    for event in particle_data:
        current_time = event[TIME]

        if current_time > total_delta_t:
            dcms.append(dcm(event[OBSTACLES][0], length))
            total_delta_t += delta_t

    return dcms

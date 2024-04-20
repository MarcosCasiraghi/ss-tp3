from multiprocessing.pool import Pool

import numpy as np

from src.util import *
from sklearn.linear_model import LinearRegression


def dc(obstacle: [], length: float):
    return (obstacle[X] - length / 2) ** 2 + (obstacle[Y] - length / 2) ** 2


def calculate_dc(particle_data: [], length: float, delta_t: float) -> []:
    dcs = []
    total_delta_t = delta_t
    for event in particle_data:
        current_time = event[TIME]

        if current_time > total_delta_t:
            dcs.append(dc(event[OBSTACLES][0], length))
            total_delta_t += delta_t

    return dcs


def process_files(args):
    d_filename, s_filename, delta_t = args
    static_data = get_static_data(s_filename)
    particle_data = get_particle_data(d_filename)
    dcms = calculate_dc(particle_data, static_data['l'], delta_t)
    return dcms


def calculate_dcm(particle_filename: [], static_filename: [], delta_t: float):
    all_dmcs = []

    args = []
    for p,s in zip(particle_filename, static_filename):
        args.append((p, s, delta_t))


    with Pool() as pool:
        results = pool.imap_unordered(process_files, args)
        pool.close()
        pool.join()

        results = [r for r in results]

    min_length = min(len(dcms) for dcms in results)
    for dcms in results:
        for _ in range(len(dcms) - min_length):
            dcms.pop()
        all_dmcs.append(np.array(dcms))

    dcms_times = [delta_t * i for i in range(0, min_length)]
    avg_dcms = np.mean(np.array(all_dmcs), axis=0)
    std_dcms = np.std(np.array(all_dmcs), axis=0)

    return dcms_times, avg_dcms, std_dcms


def up_to_idx(dcms_times: np.array, up_to: float):
    for i, val in enumerate(dcms_times):
        if val > up_to:
            return i


def calculate_regression(dcms_times: np.array, dcms:np.array, up_to: int):
    return np.polyfit(dcms_times[:up_to], dcms[:up_to], 1)


def ecm(dcms_times, dcms, a, b):

    error = 0
    for dt, d in zip(dcms_times, dcms):
        error += (d - (a * dt)) ** 2

    return error


def calculate_regression_error(dcms_times, dcms, coef, offset: float, step: float):
    a = coef[0]
    b = coef[1]

    print(coef)

    a_prime = a - offset
    errors = []
    a_values = []
    while a_prime < a + offset:
        a_values.append(a_prime)
        errors.append(ecm(dcms_times, dcms, a_prime, b))
        a_prime += step

    return a_values, errors


def calculate_incline(dcms: np.array, dcms_times: np.array, up_to: int) -> float:
    model = LinearRegression()
    model.fit(np.array(dcms_times[:up_to]).reshape(-1,1), dcms[:up_to])

    print(model.coef_)
    slope = model.coef_[0]

    return slope


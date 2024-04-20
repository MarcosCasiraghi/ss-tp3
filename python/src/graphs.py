import numpy as np
from matplotlib import pyplot as plt

from src.dcm import up_to_idx

PRESSURE_UNIT = '$(Pa \\cdot m)$'
TIME_UNIT = '$(s)$'
TEMP_UNITS = '$(U.A.)$'
DCM_UNITS = '$(m^2)$'

def pressure_plot(wall_pressure, obstacle_pressure, delta_t):
    time_values = [delta_t * i for i in range(1, len(wall_pressure) + 1)]

    # plt.scatter(time_values, [abs(p) for p in wall_pressure], marker='o', color='blue')
    plt.plot(time_values, [abs(p) for p in wall_pressure], linestyle='-', color='blue', label='Presion sobre pared')

    # plt.scatter(time_values, [abs(p) for p in obstacle_pressure], marker='o', color='orange')
    plt.plot(time_values, [abs(p) for p in obstacle_pressure], linestyle='-', color='orange', label='Presion sobre obstaculo')

    plt.legend()
    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel(f'Presión {PRESSURE_UNIT}')
    plt.grid(True)

    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)

    plt.show()


def temperature_plot(temperature_times: [], temperatures: []):
    plt.scatter(temperature_times, temperatures, marker='o', color='blue', s=5)
    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel(f'Temperatura {TEMP_UNITS}')
    plt.grid(True)
    plt.show()


def all_dcm_plot(dcm_times: [], dcms: [[]]):
    for d in dcms:
        plt.plot(dcm_times, d)
    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel(f'DC {DCM_UNITS}')
    plt.grid(True)
    plt.show()


def dcm_average_plot(dcm_times: [], dcms: [], std_dcms: [], up_to: int, poly1d_fn):
    plt.errorbar(dcm_times, dcms, std_dcms, linestyle='None', marker='o', color='blue', label='DCM')

    plt.plot(dcm_times[:up_to], poly1d_fn(dcm_times[:up_to]), label='Ajuste lineal', color='red')

    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel(f'DCM {DCM_UNITS}')
    plt.grid(True)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
    plt.legend()
    plt.show()


def graph_linear_regression_error(a: [], ecm: []):
    plt.plot(a, ecm, label='Error Cuadratico Medio')

    plt.xlabel(f'a')
    plt.ylabel(f'ECM')
    plt.grid(True)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0), useMathText=True)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
    plt.legend()
    plt.show()


def temp_pressure_plot(temperature: [], pressure: [], stds: []):
    wall_pressure = [p[0] for p in pressure]
    obstacle_pressure = [p[1] for p in pressure]

    wall_std = [p[0] for p in stds]
    obstacle_std = [p[1] for p in stds]

    plt.errorbar(temperature, wall_pressure, yerr=wall_std, fmt='o', color='blue', label='Presión promedio de las paredes')
    plt.errorbar(temperature, obstacle_pressure, yerr=obstacle_std, fmt='x', color='red', label='Presión promedio del obstáculo')

    plt.xlabel(f'Temperatura {TEMP_UNITS}')
    plt.ylabel(f'Presión {PRESSURE_UNIT}')
    plt.grid(True)
    plt.legend()

    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0), useMathText=True)

    plt.show()


def collisions_plot(collision_times: []):
    plt.scatter(collision_times, [i for i in range(len(collision_times))], marker='o', color='blue')
    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel('Cantidad de choques')
    plt.grid(True)
    plt.show()
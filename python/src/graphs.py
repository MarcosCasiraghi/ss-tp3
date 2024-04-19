from matplotlib import pyplot as plt

PRESSURE_UNIT = '$(Pa \\cdot m)$'
TIME_UNIT = '$(s)$'
TEMP_UNITS = '$(Ua)$'
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


def dcm_average_plot(dcm_times: [], dcms: []):
    plt.plot(dcm_times, dcms, color='blue')
    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel(f'DCM {DCM_UNITS}')
    plt.grid(True)
    plt.show()


def temp_pressure_plot(temperature: [], wall_pressure: [], velocity_values: []):
    plt.scatter(temperature, wall_pressure, marker='o', color='blue', label=velocity_values)
    plt.xlabel(f'Temperatura {TEMP_UNITS}')
    plt.ylabel(f'Presión {PRESSURE_UNIT}')
    plt.grid(True)
    plt.show()


def collisions_plot(collision_times: []):
    plt.scatter(collision_times, [i for i in range(len(collision_times))], marker='o', color='blue')
    plt.xlabel(f'Tiempo {TIME_UNIT}')
    plt.ylabel('Cantidad de choques')
    plt.grid(True)
    plt.show()
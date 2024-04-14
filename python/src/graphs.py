from matplotlib import pyplot as plt


def pressure_plot(pressures, delta_t):
    time_values = [delta_t * i for i in range(1, len(pressures) + 1)]

    plt.scatter(time_values, [abs(p) for p in pressures], marker='o', color='blue')
    plt.plot(time_values, [abs(p) for p in pressures], linestyle='-', color='gray')
    plt.xlabel('Tiempo')
    plt.ylabel('Presión')
    plt.grid(True)
    plt.show()


def temperature_plot(temperature_times: [], temperatures: []):
    plt.scatter(temperature_times, temperatures, marker='o', color='blue', s=5)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.grid(True)
    plt.show()


def dcm_plot(dcm_times: [], dcms: []):
    plt.scatter(dcm_times, dcms, marker='o', color='blue', s=5)
    plt.xlabel('Tiempo')
    plt.ylabel('DCM')
    plt.grid(True)
    plt.show()


def temp_pressure_plot(binned_temperature: [], binned_wall_pressure: []):
    plt.scatter(binned_temperature, binned_wall_pressure, marker='o', color='blue')
    plt.xlabel('Temperatura')
    plt.ylabel('Presión')
    plt.grid(True)
    plt.show()


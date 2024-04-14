from matplotlib import pyplot as plt


def pressure_plot(pressures, delta_t):
    time_values = [delta_t * i for i in range(1, len(pressures) + 1)]

    plt.scatter(time_values, [abs(p) for p in pressures], marker='o', color='blue')
    plt.plot(time_values, [abs(p) for p in pressures], linestyle='-', color='gray')
    plt.xlabel('Tiempo')
    plt.ylabel('Presión')
    plt.grid(True)
    plt.show()


def temperature_plot(temperature_times: [], temperature: []):
    plt.scatter(temperature_times, temperature, marker='o', color='blue', s=5)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.grid(True)
    plt.show()

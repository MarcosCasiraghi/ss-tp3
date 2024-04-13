from util import *
import matplotlib.pyplot as plt


def get_collision_velocities(particle_filename: str, static_data_filename: str):
    particle_data = get_particle_data(particle_filename)
    static_data = get_static_data(static_data_filename)

    collision_wall_times = []
    collision_velocities_walls = []

    collision_object_times = []
    collision_velocities_object =[]

    i = 0
    while i + 1 < len(particle_data):
        time = particle_data[i][TIME]
        prev = particle_data[i][PARTICLES]
        post = particle_data[i+1][PARTICLES]
        # TODO: agregar el obstacle

        prev_particles, post_particles = find_collision(prev, post)

        # colsion de particula con pared o obstaculo
        if len(prev_particles) == 1:
            # TODO: revisar si esto es suficiente para determinar que tipo de choque es
            if prev_particles[0][VX] == - post_particles[0][VX]:
                collision_wall_times.append(time)
                # se agrega velocidad normal al choque
                collision_velocities_walls.append(prev_particles[0][VX])
            elif prev_particles[0][VY] == - post_particles[0][VY]:
                collision_wall_times.append(time)
                # se agrega velocidad normal al choque
                collision_velocities_walls.append(prev_particles[0][VY])
            else:
                collision_object_times.append(time)
                # TODO: calcular velocidad normal al choque con obstaculo

        i = i + 1
        
    return collision_wall_times, collision_velocities_walls, collision_object_times, collision_velocities_object


def calculate_pressure(delta_t, collision_times, collision_velocities):
    num_samples = len(collision_times)
    pressures = []
    current_pressure = 0

    delta_t_accumulated = delta_t

    for i in range(num_samples):
        # Se fija los valores dentro del rango delta t
        if collision_times[i] <= delta_t_accumulated:
            # Todo: revisar si es * 2 o no
            current_pressure += collision_velocities[i] * 2
        else:
            pressures.append(current_pressure / delta_t)
            current_pressure = collision_velocities[i]
            delta_t_accumulated += delta_t

        if i == num_samples - 1:
            pressures.append(current_pressure / delta_t)

    return pressures


def find_collision(prev_array, post_array):
    prev_particles = list()
    post_particles = list()
    for prev, post in zip(prev_array, post_array):
        # Si alguna de las velocidades es distinta, es porque colisiono
        if prev[VX] != post[VX] or prev[VY] != post[VY]:
            prev_particles.append(prev)
            post_particles.append(post)

    return prev_particles, post_particles


def pressure_plot(pressures, delta_t):
    time_values = [delta_t * i for i in range(1, len(pressures) + 1)]

    plt.scatter(time_values, [abs(p) for p in pressures], marker='o', color='blue')
    plt.plot(time_values, [abs(p) for p in pressures], linestyle='-', color='gray')
    plt.xlabel('Tiempo')
    plt.ylabel('Presión')
    plt.grid(True)
    plt.show()


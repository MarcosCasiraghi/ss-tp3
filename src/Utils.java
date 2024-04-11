import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Utils {
    private static final Random random = new Random(2);

    public static List<Particle> createParticles(final int amount, final double particle_radius, final double length, final double obstacle_radius) {
        List<Particle> particles = new ArrayList<>();
        for(int i = 0; i < amount; i++){
            Particle particle = createNewParticleUnsuperposed(particles, length, particle_radius, obstacle_radius);
            particles.add(particle);
        }
        Particle.setR(particle_radius);
        return particles;
    }

    private static Particle createNewParticleUnsuperposed(List<Particle> particles, double l, double particle_r, double obstacle_radius){
        while (true) {
            double x_candidate = generateRandom(0 + particle_r, l - particle_r);
            double y_candidate = generateRandom(0 + particle_r, l - particle_r);

            boolean valid = (!(x_candidate + particle_r >= l / 2 - obstacle_radius) || !(x_candidate - particle_r <= l / 2 + obstacle_radius)) &&
                    (!(y_candidate + particle_r >= l / 2 - obstacle_radius) || !(y_candidate - particle_r <= l / 2 + obstacle_radius));

            if(valid){
                for( Particle particle : particles){
                    if(particle.isSuperposed(x_candidate, y_candidate, particle_r)){
                        valid = false;
                        break;
                    }
                }
            }
            if(valid){
                double angle = generateRandom(0, 2 * Math.PI);
                double xVelocity = Math.cos(angle);
                double yVelocity = Math.sin(angle);
                return new Particle(
                        particles.size() + 1,
                        x_candidate,
                        y_candidate,
                        xVelocity,
                        yVelocity
                );
            }

        }
    }

    private static double generateRandom(double lower, double upper){
        return lower + (upper - lower) * random.nextDouble();
    }

    public static List<Wall> createWalls(double l) {
        List<Wall> walls = new ArrayList<>();
        walls.add(new Wall(l, Wall.WallType.TOP));
        walls.add(new Wall(l, Wall.WallType.BOTTOM));
        walls.add(new Wall(l, Wall.WallType.LEFT));
        walls.add(new Wall(l, Wall.WallType.RIGHT));
        return walls;
    }
}

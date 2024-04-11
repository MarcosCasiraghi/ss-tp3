import models.Particle;
import models.Wall;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Utils {
    private static final Random random = new Random(2);

    public static List<Particle> createParticles(final int amount, final double length, final double particleRadius, final double particleMass, final List<Particle> obstacles) {
        List<Particle> particles = new ArrayList<>(obstacles);
        for(int i = 0; i < amount; i++){
            Particle particle = createNewParticleUnsuperposed(particles, length, particleRadius, particleMass);
            particles.add(particle);
        }
        return particles;
    }

    private static Particle createNewParticleUnsuperposed(List<Particle> particles, double l, double particleRadius, final double particleMass){
        while (true) {
            double xCandidate = generateRandom(0 + particleRadius, l - particleRadius);
            double yCandidate = generateRandom(0 + particleRadius, l - particleRadius);

            boolean valid = true;
            for(Particle particle : particles){
                if(particle.isSuperposed(xCandidate, yCandidate, particleRadius)){
                    valid = false;
                    break;
                }
            }

            if(valid){
                double angle = generateRandom(0, 2 * Math.PI);
                double xVelocity = Math.cos(angle);
                double yVelocity = Math.sin(angle);
                return new Particle(
                        xCandidate,
                        yCandidate,
                        xVelocity,
                        yVelocity,
                        particleRadius,
                        particleMass
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

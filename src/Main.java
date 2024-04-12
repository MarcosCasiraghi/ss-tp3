import models.Particle;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int n = 200;
        double l = 0.1;
        double particleR = 0.001;
        double particleMass = 1;
        double particleV = 1;
        double obstacleR = 0.005;
        double obstacleMass = 3;
        boolean fixedObstacle = false;
        long timestamp = System.currentTimeMillis();

        Simulation simulation = new Simulation(n, l, particleR, particleMass, particleV, obstacleR, obstacleMass, fixedObstacle);
        writeStaticFile(n, l, particleR, particleMass, particleV, obstacleR, obstacleMass, fixedObstacle, timestamp);

        try (FileWriter writer = new FileWriter("./python/output-files/particle-movement-" + timestamp + ".csv")) {

            saveParticleData(simulation.getParticles(), simulation.getTimeElapsed(), writer);

            for(int i=0; i<500; i++) {
                simulation.simulate();

                saveParticleData(simulation.getParticles(), simulation.getTimeElapsed(), writer);
            }
        }
        catch (IOException e){
            System.out.println(e);
        }

    }
    private static void writeStaticFile(int n, double l, double particleR, double particleMass, double particleV, double obstacleRadius, double obstacleMass, boolean fixedObstacle, long timestamp){
        try(FileWriter writer = new FileWriter("./python/output-files/static-data-" + timestamp + ".csv")) {
            writer.write("n," + n + "\n");
            writer.write("l," + l + "\n");
            writer.write("pr," + particleR + "\n");
            writer.write("pm," + particleMass + "\n");
            writer.write("pv," + particleV + "\n");
            writer.write("or," + obstacleRadius + "\n");
            writer.write("om," + obstacleMass + "\n");
            writer.write("fixed," + fixedObstacle + "\n");
        }
        catch (IOException e){
            System.out.println(e);
        }
    }
    private static void saveParticleData(List<Particle> particles, double timeElapsed,  FileWriter writer) {
        try{
            writer.write("t:" + timeElapsed + "\n");
            for(Particle p : particles){
                writer.write(p.toString() + "\n");
            }
        }
        catch (IOException e){
            System.out.println(e);
        }
    }
}
import models.Particle;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int n = 10;
        double l = 10;
        double particleR = 0.1;
        double particleMass = 1;
        double particleV = 1;
        double obstacleR = 1;
        double obstacleMass = 2;
        boolean fixedObstacle = true;
        long timestamp = System.currentTimeMillis();

        Simulation simulation = new Simulation(n, l, particleR, particleMass, obstacleR,obstacleMass,fixedObstacle);
        writeStaticFile(n, l, particleR, particleMass, particleV, obstacleR, obstacleMass, fixedObstacle, timestamp);

        try (FileWriter writer = new FileWriter("./python/output-files/particle-movement-" + timestamp + ".txt")) {

            saveParticleData(simulation.getParticles(), simulation.getTimeElapsed(), writer);

            for(int i=0; i<10000; i++) {
                simulation.simulate();

                saveParticleData(simulation.getParticles(), simulation.getTimeElapsed(), writer);
            }
        }
        catch (IOException e){
            System.out.println(e);
        }

    }
    private static void writeStaticFile(int n, double l, double particleR, double particleMass, double particleV, double obstacleRadius, double obstacleMass, boolean fixedObstacle, long timestamp){
        try(FileWriter writer = new FileWriter("./python/output-files/static-data-" + timestamp + ".txt")) {
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
import models.*;

import java.util.*;
import java.util.function.BiFunction;

public class Simulation {
    private final List<Particle> particles;
    private final List<Wall> walls;
    private final List<Particle> obstacles;
    private final double l;
    private double timeElapsed;

    private final PriorityQueue<Event> events;

    public Simulation(int n, double l, double particleR, double particleMass, double particleV, double obstacleRadius, double obstacleMass, boolean fixedObstacle) {
        Particle obstacle;
        if(fixedObstacle) {
            obstacle = new FixedObstacle(l/2.0, l/2.0, obstacleRadius);
        }
        else {
            obstacle = new MovableObstacle(l/2.0, l/2.0, obstacleRadius,  obstacleMass);
        }
        this.obstacles = List.of(obstacle);

        this.particles = Utils.createParticles(n, l, particleR, particleMass, particleV, obstacles);
        this.walls = Utils.createWalls(l);

        this.l = l;
        this.timeElapsed = 0;

        // Eventos iniciales
        this.events = new PriorityQueue<>();
        calculateEvents();
    }

    private void addEventsForParticle(Particle p, BiFunction<Particle, Particle, Boolean> discriminator){
        // Paredes
        for(Wall w : walls) {
            double t = p.getTimeToCollision(w) + timeElapsed;
            if(t != Double.POSITIVE_INFINITY){
                events.add(new Event(t, p, w));
            }
        }
        // Otras particulas / obstaculos
        for(Particle p2 : particles) {
            if(discriminator.apply(p, p2)){
                double t = p.getTimeToCollision(p2) + timeElapsed;
                if(t != Double.POSITIVE_INFINITY){
                    events.add(new Event(t, p, p2));
                }
            }
        }
    }

    private void calculateEvents(){
        for(Particle p : particles) {
            if(p.getType() == Collidable.CollidableType.IMMOVABLE){
                continue;
            }
            addEventsForParticle(p, (p1, p2) -> p1.getId() != p2.getId());
        }
    }
    private void removeStaleEvents(Particle p){
        events.removeIf(event -> {
            if(event.getParticle().equals(p)){
                return true;
            }
            if(event.getCollidable().getType() == Collidable.CollidableType.PARTICLE) {
                return ((Particle) event.getCollidable()).equals(p);
            }
            // TODO: complete
            return false;
        });
    }


    public void simulate() {
        // Proximo evento a ocurrir
        Event nextEvent = events.poll();
        if (nextEvent == null) {
            return;
        }
        double time = nextEvent.getT() - timeElapsed;
        Particle p = nextEvent.getParticle();
        Collidable c = nextEvent.getCollidable();

        // Muevo las particulas
        for (Particle particle : particles) {
            particle.move(time);
        }
        timeElapsed += time;

        // Colision
        p.collision(c);

        // Eliminamos los eventos que ya no sirven
        removeStaleEvents(p);
        if(c.getType() == Collidable.CollidableType.PARTICLE){
            removeStaleEvents((Particle) c);
        }

        // Agregamos los nuevos eventos posibles
        addEventsForParticle(p, (p1, p2)-> p1.getId() != p2.getId());
        if(c.getType() == Collidable.CollidableType.PARTICLE){
            addEventsForParticle((Particle) c, (p1, p2)-> p1.getId() != p2.getId());
        }

    }

    public List<Particle> getParticles() {
        return particles;
    }

    public double getTimeElapsed() {
        return timeElapsed;
    }
}

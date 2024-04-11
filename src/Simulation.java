import models.*;

import java.util.*;

public class Simulation {
    private final List<Particle> particles;
    private final List<Wall> walls;
    private final List<Particle> obstacles;
    private final double l;
    private double timeElapsed;

    private final PriorityQueue<Event> events;

    public Simulation(int n, double l, double particleR, double particleMass, double obstacleRadius, double obstacleMass, boolean fixedObstacle) {
        Particle obstacle;
        if(fixedObstacle) {
            obstacle = new FixedObstacle(l/2.0, l/2.0, obstacleRadius);
        }
        else {
            obstacle = new Particle(l/2.0, l/2.0, 0, 0, obstacleRadius,  obstacleMass);
        }
        this.obstacles = List.of(obstacle);

        this.particles = Utils.createParticles(n, l, particleR, particleMass, obstacles);
        this.walls = Utils.createWalls(l);

        this.l = l;
        this.timeElapsed = 0;
        events = calculateEvents();
    }

    private PriorityQueue<Event> calculateEvents(){
        PriorityQueue<Event> queue = new PriorityQueue<>();

        for(Particle p : particles) {
            // Paredes
            for(Wall w : walls) {
                double t = p.getTimeToCollision(w);
                if(t != Double.POSITIVE_INFINITY){
                    queue.add(new Event(t, p, w));
                }
            }
            // Otras particulas / obstaculos
            for(Particle p2 : particles) {
                if(p.getId() < p2.getId()){                 // Optimizacion: en vez de n*n, es n+n-1+n-2...
                    double t = p.getTimeToCollision(p2);
                    if(t != Double.POSITIVE_INFINITY){
                        queue.add(new Event(t, p, p2));
                    }
                }
            }
        }
        return queue;
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
    private void addEventsForParticle(Particle p){
        // Paredes
        for(Wall w : walls) {
            double t = p.getTimeToCollision(w);
            if(t != Double.POSITIVE_INFINITY){
                events.add(new Event(t, p, w));
            }
        }
        // Otras particulas / obstaculos
        for(Particle p2 : particles) {
            if(p.getId() != p2.getId()){
                double t = p.getTimeToCollision(p2);
                if(t != Double.POSITIVE_INFINITY){
                    events.add(new Event(t, p, p2));
                }
            }
        }
    }

    public void simulate() {
        // Proximo evento a ocurrir
        Event nextEvent = events.poll();
        if (nextEvent == null) {
            return;
        }
        double time = nextEvent.getT();
        Particle p = nextEvent.getParticle();
        Collidable c = nextEvent.getCollidable();

        // Muevo las particulas
        for (Particle particle : particles) {
            particle.move(time);
        }

        // Colision
        p.collision(c);

        // Eliminamos los eventos que ya no sirven
        removeStaleEvents(p);
        if(c.getType() == Collidable.CollidableType.PARTICLE){
            removeStaleEvents((Particle) c);
        }

        // Agregamos los nuevos eventos posibles
        addEventsForParticle(p);
        if(c.getType() == Collidable.CollidableType.PARTICLE){
            addEventsForParticle((Particle) c);
        }

        timeElapsed += time;
    }

    public List<Particle> getParticles() {
        return particles;
    }

    public double getTimeElapsed() {
        return timeElapsed;
    }
}

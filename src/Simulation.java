import com.sun.source.tree.Tree;

import java.util.*;

public class Simulation {

    private final List<Particle> particles;
    private final List<Wall> walls;
    private final double l;
    private double timeElapsed;

    private final PriorityQueue<Event> events;

    public Simulation(int n, double l, double particleR, double obstacleR) {
        this.walls = Utils.createWalls(l);
        this.particles = Utils.createParticles(n, particleR, l, obstacleR);
        this.l = l;
        this.timeElapsed = 0;
        events = reCalculateEvents();
    }

    private PriorityQueue<Event> reCalculateEvents(){
        PriorityQueue<Event> queue = new PriorityQueue<>();

        for(Particle p : particles) {
            for(Wall w : walls) {
                double t = p.getTimeToCollisionWithWall(w);
                if(t != Double.POSITIVE_INFINITY){
                    queue.add(new Event(t, p, w));
                }
            }
            for(Particle p2 : particles) {
                if(p.getId() < p2.getId()){
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
        for(Wall w : walls) {
            double t = p.getTimeToCollisionWithWall(w);
            if(t != Double.POSITIVE_INFINITY){
                events.add(new Event(t, p, w));
            }
        }
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
}

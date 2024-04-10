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
                if(p.willCollideWithWall(w)){
                    queue.add(new Event(p.getTimeToCollisionWithWall(w), p, w));
                }
            }

            for(Particle p2 : particles) {
                // TODO check: si funciona correctamente lo de <
                if(p.getId() < p2.getId() && p.willCollide(p2)){
                    queue.add(new Event(p.getTimeToCollision(p2), p, p2));
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
                return ((Particle)event.getCollidable()).equals(p);
            }
            // TODO: complete
            return false;
        });
    }

    public void simulate() {
        // Proximo evento a ocurrir
        Event nextEvent = events.poll();
        if(nextEvent == null){
            return;
        }
        double time = nextEvent.getT();
        Particle p = nextEvent.getParticle();
        Collidable c = nextEvent.getCollidable();

        // Muevo las particulas
        for(Particle particle : particles) {
            particle.move(time);
        }

        // Colision
        p.collision(c);

        // TODO: bajar al archivo (?)

        // Eliminamos los eventos que ya no sirven
        removeStaleEvents(p);

        // Agregamos los nuevos eventos posibles
        // oka pushea c
    }
}

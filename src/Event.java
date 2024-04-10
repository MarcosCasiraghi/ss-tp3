public class Event implements Comparable<Event>{
    private final double t;
    private final Particle particle;
    private final Collidable c2;

    public Event(double t, Particle particle, Collidable c2){
        this.t = t;
        this.particle = particle;
        this.c2 = c2;
    }
    public Particle getParticle() {
        return particle;
    }

    public Collidable getCollidable() {
        return c2;
    }

    public double getT() {
        return t;
    }

    @Override
    public int compareTo(Event other) {
        return Double.compare(t, other.t);
    }
}

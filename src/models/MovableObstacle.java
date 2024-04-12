package models;

public class MovableObstacle extends Particle{
    public MovableObstacle(double x, double y, double r, double mass) {
        super(x, y, 0, 0, r, mass);
    }

    @Override
    public String toString() {
        return "obs:" + getId() + "," + getX() + "," + getY();
    }
}

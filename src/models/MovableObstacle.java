package models;

import java.util.Locale;

public class MovableObstacle extends Particle{
    public MovableObstacle(double x, double y, double r, double mass) {
        super(x, y, 0, 0, r, mass);
    }

    @Override
    public String toString() {
        return "obs:"  + getId() + "," +
                String.format(Locale.US, "%.4f", getX()) + "," +
                String.format(Locale.US, "%.4f", getY()) + "," +
                String.format(Locale.US, "%.4f", getxVelocity()) + "," +
                String.format(Locale.US, "%.4f", getyVelocity());
    }
}

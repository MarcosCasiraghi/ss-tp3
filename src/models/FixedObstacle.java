package models;

import java.util.Locale;

public class FixedObstacle extends Particle {
    public FixedObstacle(double x, double y, double r) {
        super(x, y, 0, 0, r, 0);
        setType(CollidableType.IMMOVABLE);
    }

    @Override
    public void move(double t) {
        // Do nothing
    }

    @Override
    public void setxVelocity(double xVelocity) {
        throw new RuntimeException("No deberia ocurrir");
    }

    @Override
    public void setyVelocity(double yVelocity) {
        throw new RuntimeException("No deberia ocurrir");
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

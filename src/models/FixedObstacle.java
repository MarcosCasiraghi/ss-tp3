package models;

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
}

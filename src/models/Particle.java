package models;

import java.util.Locale;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicInteger;

public class Particle extends Collidable {
    private static final AtomicInteger globalId = new AtomicInteger(0);
    private final int id;
    private double xVelocity;
    private double yVelocity;
    private final double r;
    private final double mass;
    private int collisionCount;

    public Particle(double x, double y, double xVelocity, double yVelocity, double r, double mass) {
        super(CollidableType.PARTICLE);
        this.id = globalId.getAndIncrement();
        super.setX(x);
        super.setY(y);
        this.xVelocity = xVelocity;
        this.yVelocity = yVelocity;
        this.r = r;
        this.mass = mass;
        this.collisionCount = 0;
    }


    // = = = = = Public methods = = = = =

    public double getTimeToCollision(Collidable c){
        return switch (c.getType()) {
            case PARTICLE, IMMOVABLE -> getTimeToCollisionWithParticle((Particle) c);   // AYAYAY
            case WALL -> getTimeToCollisionWithWall((Wall) c);                          // AYAYAY
        };
    }
    public void collision(Collidable c){
        switch (c.getType()) {
            case PARTICLE -> collisionWithParticle((Particle) c);               // AYAYAY
            case WALL -> collisionWithWall((Wall) c);                           // AYAYAY
            case IMMOVABLE -> collisionWithImmovable((FixedObstacle) c);        // AYAYAY
        }
        collisionCount++;
    }
    public void move(double t) {
        setX(getX() + xVelocity * t);
        setY(getY() + yVelocity * t);
    }
    public boolean isSuperposed(double x, double y, double radius){
        return Math.sqrt(Math.pow((this.getX() - x), 2) + (Math.pow((this.getY() - y), 2))) - r - radius < 0;
    }

    // = = = = = Private methods = = = = =


    private double getTimeToCollisionWithParticle(Particle other){
        double delta_x = other.getX() - this.getX();
        double delta_y = other.getY() - this.getY();

        double delta_vx = other.getxVelocity() - this.getxVelocity();
        double delta_vy = other.getyVelocity() - this.getyVelocity();

        double vr = delta_x * delta_vx + delta_y * delta_vy;

        if( vr >= 0 ) return Double.POSITIVE_INFINITY;

        double d = vr * vr - (delta_vx * delta_vx + delta_vy * delta_vy) * ( delta_x * delta_x + delta_y * delta_y - Math.pow(r + other.r, 2) );

        if( d < 0 ) return Double.POSITIVE_INFINITY;

        return - ((vr + Math.sqrt(d)) / (delta_vx * delta_vx + delta_vy * delta_vy));
    }
    private double getTimeToCollisionWithWall(Wall wall){
        switch (wall.getWallType()) {
            case TOP -> {if(yVelocity >= 0) return Double.POSITIVE_INFINITY;}           // importante el =
            case BOTTOM -> {if(yVelocity <= 0) return Double.POSITIVE_INFINITY;}
            case LEFT -> {if(xVelocity >= 0) return Double.POSITIVE_INFINITY;}
            case RIGHT -> {if(xVelocity <= 0) return Double.POSITIVE_INFINITY;}
        }
        return switch (wall.getWallType()) {
            case TOP -> (r-super.getY()) / yVelocity;
            case BOTTOM -> (wall.getY() - r-super.getY()) / yVelocity;
            case LEFT -> (r-super.getX()) / xVelocity;
            case RIGHT -> (wall.getX() - r-super.getX()) / xVelocity;
        };
    }

    private void collisionWithWall(Wall wall){
        if (wall.getWallType() == Wall.WallType.LEFT || wall.getWallType() == Wall.WallType.RIGHT){
            xVelocity =  -xVelocity;
        }else{
            yVelocity =  -yVelocity;
        }
    }
    private void collisionWithImmovable(FixedObstacle p2){
        double delta_x = getX() - p2.getX();
        double delta_y = getY() - p2.getY();

        double delta_vx = xVelocity;
        double delta_vy = yVelocity;

        double J = (2 * mass * (delta_vx * delta_x + delta_vy * delta_y)) / ((r + p2.getR()));

        double Jx = J * delta_x / (r + p2.getR());
        double Jy = J * delta_y / (r + p2.getR());

        setxVelocity(xVelocity - Jx / mass);
        setyVelocity(yVelocity - Jy / mass);
    }
    private void collisionWithParticle(Particle p2){

        double delta_x = getX() - p2.getX();
        double delta_y = getY() - p2.getY();

        double delta_vx = xVelocity - p2.xVelocity;
        double delta_vy = yVelocity - p2.yVelocity;

        double J = (2 * mass * p2.mass * (delta_vx * delta_x + delta_vy * delta_y)) / ((r + p2.r) * (mass + p2.mass));

        double Jx = J * delta_x / (r + p2.r);
        double Jy = J * delta_y / (r + p2.r);

        setxVelocity(xVelocity - Jx / mass);
        setyVelocity(yVelocity - Jy / mass);

        p2.setxVelocity(p2.getxVelocity() + Jx / p2.mass);
        p2.setyVelocity(p2.getyVelocity() + Jy / p2.mass);
    }

    // = = = = = Getters and Setter = = = = =

    public int getId() {
        return id;
    }

    public double getxVelocity() {
        return xVelocity;
    }

    public double getyVelocity() {
        return yVelocity;
    }

    public void setxVelocity(double xVelocity) {
        this.xVelocity = xVelocity;
    }

    public void setyVelocity(double yVelocity) {
        this.yVelocity = yVelocity;
    }
    public double getR() {
        return r;
    }
    public double getMass() {
        return mass;
    }
    public int getCollisionCount() {
        return collisionCount;
    }


    // = = = = = General methods = = = = =

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Particle particle)) return false;
        return id == particle.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return "par:" + id + "," +
                String.format(Locale.US, "%.4f", getX()) + "," +
                String.format(Locale.US, "%.4f", getY()) + "," +
                String.format(Locale.US, "%.4f", getxVelocity()) + "," +
                String.format(Locale.US, "%.4f", getyVelocity());
    }
}

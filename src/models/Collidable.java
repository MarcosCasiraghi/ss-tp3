package models;

public abstract class Collidable {
    private double x;
    private double y;
    private CollidableType type;

    public Collidable(CollidableType type){
        this.type = type;
    }

    public CollidableType getType() {
        return type;
    }

    public void setType(CollidableType type) {
        this.type = type;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public enum CollidableType {
        PARTICLE,
        WALL,
        IMMOVABLE
    }
}

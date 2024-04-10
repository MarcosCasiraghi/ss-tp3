public class Collidable {
    private double x;
    private double y;
    private final CollidableType type;
    public Collidable(CollidableType type){
        this.type = type;
    }

    public CollidableType getType() {
        return type;
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

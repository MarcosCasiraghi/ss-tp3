package models;

public class Wall extends Collidable{
    private final WallType type;
    public Wall(double l, WallType type){
        super(CollidableType.WALL);
        this.type = type;
        switch (type){
            case TOP -> setY(0);
            case BOTTOM -> setY(l);
            case LEFT -> setX(0);
            case RIGHT -> setX(l);
        }
    }

    public WallType getWallType() {
        return type;
    }
    public enum WallType {
        TOP,
        BOTTOM,
        LEFT,
        RIGHT
    }
}

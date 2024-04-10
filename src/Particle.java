import java.util.Objects;

public class Particle extends Collidable {
    private final int id;
    private double xVelocity;
    private double yVelocity;
    private static double r;
    private static double mass;

    public Particle(int id, double x, double y, double xVelocity, double yVelocity) {
        super(CollidableType.PARTICLE);
        this.id = id;
        super.setX(x);
        super.setY(y);
        this.xVelocity = xVelocity;
        this.yVelocity = yVelocity;
    }
    public boolean isSuperposed(double x, double y, double radius){
        return Math.sqrt(Math.pow((this.getX() - x), 2) + (Math.pow((this.getY() - y), 2))) - Particle.getR() - radius < 0;
    }

    public double getTimeToCollision(Particle other){

        double delta_x = this.getX() - other.getX();
        double delta_y = this.getY() - other.getY();

        double delta_vx = this.getxVelocity() - other.getxVelocity();
        double delta_vy = this.getyVelocity() - other.getyVelocity();

        double vr = delta_x * delta_vx + delta_y * delta_vy;

        if( vr >= 0 ) return Double.POSITIVE_INFINITY;

        double d = vr * vr - (delta_vx * delta_vx + delta_vy * delta_vy) * ( delta_x * delta_x + delta_y * delta_y - Math.pow(2 * Particle.getR(), 2) );

        if( d < 0 ) return Double.POSITIVE_INFINITY;

        return - ((vr + Math.sqrt(d)) / (delta_vx * delta_vx + delta_vy * delta_vy));
    }
    public double getTimeToCollisionWithWall(Wall wall){
        switch (wall.getWallType()) {
            case TOP -> {if(yVelocity < 0) return Double.POSITIVE_INFINITY;}
            case BOTTOM -> {if(yVelocity > 0) return Double.POSITIVE_INFINITY;}
            case LEFT -> {if(xVelocity < 0) return Double.POSITIVE_INFINITY;}
            case RIGHT -> {if(xVelocity > 0) return Double.POSITIVE_INFINITY;}
        }
        return switch (wall.getWallType()) {
            case TOP -> (r-super.getY()) / yVelocity;
            case BOTTOM -> (wall.getY() - r-super.getY()) / yVelocity;
            case LEFT -> (r-super.getX()) / xVelocity;
            case RIGHT -> (wall.getX() - r-super.getX()) / xVelocity;
        };
    }

    public void collision(Collidable c){
        switch (c.getType()) {
            case PARTICLE -> particleCollision((Particle) c);        // AYAYAY
            case WALL -> collisionWithWall((Wall) c);        // AYAYAY
            case IMMOVABLE -> {/* TODO */}
        }
    }

    private void collisionWithWall(Wall wall){
        if (wall.getWallType() == Wall.WallType.LEFT || wall.getWallType() == Wall.WallType.RIGHT){
            xVelocity =  -xVelocity;
        }else{
            yVelocity =  -yVelocity;
        }
    }
    private void particleCollision(Particle p2){
        double r = Particle.getR();
        double m = Particle.getMass();

        double delta_x = getX() - p2.getX();
        double delta_y = getY() - p2.getY();

        double delta_vx = xVelocity - p2.xVelocity;
        double delta_vy = yVelocity - p2.yVelocity;

        double J = (2 * m * m * (delta_vx * delta_x + delta_vy * delta_y)) / ((2 * r) * (2 * m));

        double Jx = J * delta_x / (2 * r);
        double Jy = J * delta_y / (2 * r);

        setxVelocity(xVelocity + Jx/ m);
        setyVelocity(yVelocity + Jy/ m);

        p2.setxVelocity(p2.getxVelocity() - Jx/ m);
        p2.setyVelocity(p2.getyVelocity() - Jy/ m);
    }

    public void move(double t) {
        setX(getX() + xVelocity * t);
        setY(getY() + yVelocity * t);
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

    public static double getR() {
        return r;
    }

    public static void setR(double r) {
        Particle.r = r;
    }

    public static double getMass() {
        return mass;
    }

    public static void setMass(double mass) {
        Particle.mass = mass;
    }

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
}

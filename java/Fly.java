// adding get method for mass

public class Fly {
  //instance variables
  private double mass;
  private double speed;

  //constants
  public static final double DEFAULT_MASS = 5;
  public static final double DEFAULT_SPEED = 10;


  //constructors
  public Fly() {
    this(DEFAULT_MASS);
  }

  public Fly(double mass) {
    this(mass, DEFAULT_SPEED);
  }

  public Fly(double mass, double speed) {
    this.mass = mass;
    this.speed = speed;
  }

  //methods
  public double getMass() {
    return this.mass;
  }

  public static void main() {

  }
}
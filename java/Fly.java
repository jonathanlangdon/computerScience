// adding constructor chaining

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

  public Fly(double initMass) {
    this(initMass, DEFAULT_SPEED);
  }

  public Fly(double initMass, double initSpeed) {
    mass = initMass;
    speed = initSpeed;
  }

  public static void main() {

  }
}
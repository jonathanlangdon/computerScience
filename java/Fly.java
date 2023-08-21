// finished full class code

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

  public double getSpeed() {
    return this.speed;
  }

  public void setMass(double mass) {
    this.mass = mass;
  }

  public void setSpeed(double speed) {
    this.speed = speed;
  }
  
  public String toString() {
    if (this.mass == 0) {
      return String.format("I'm dead, but I used to be a fly with a speed of %.2f.", this.speed);
    } else {
      return String.format("I'm a speedy fly with %.2f speed and %.2f mass.", this.speed, this.mass);
    }
  }

  public void grow(int addedMass) {
    for (int i = 0; i < addedMass; i++) {
      this.mass += 1;
      if (this.mass <= 20) {
        this.speed += 1;
      } else {
        this.speed -= .5;
      }
    }
  }

  public boolean isDead() {
    return this.mass == 0;
  }
  
}
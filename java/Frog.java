// finished full class file

public class Frog {
  // instance variables
  private String name;
  private int age; // in months
  private double tongueSpeed;
  private boolean isFroglet;  //1-6 months old
  private static String species = "Rare Pepe";

  // constants
  public static final int DEFAULT_AGE = 5;
  public static final double DEFAULT_TONGUE_SPEED = 5;
  public static final int DEFAULT_GROWTH = 1;

  // constructors
  public Frog(String name) {
    this(name, DEFAULT_AGE, DEFAULT_TONGUE_SPEED);
  }

  public Frog(String name, double ageInYears, double tongueSpeed) {
    this(name, (int) ageInYears * 12, tongueSpeed);
  }

  public Frog(String name, int age, double tongueSpeed) {
    this.name = name;
    this.age = age;
    this.tongueSpeed = tongueSpeed;
    if (age < 7) this.isFroglet = true;
  }


  // methods
  public void grow () {
    this.grow(1);
  }

  public void grow(int numMonths) {
    for (int i = 0; i < numMonths; i++) {
      this.age += 1;
      if (this.age > 30 && this.tongueSpeed > 5) {
        this.tongueSpeed -= 1;
      } else if (this.age <= 12) {
        this.tongueSpeed += 1;
      }
    }
    if (this.age > 6) this.isFroglet = false;
  }

  public void eat(Fly attemptedFly) {
    if (attemptedFly.isDead()) return;
    if (this.tongueSpeed > attemptedFly.getSpeed()) {
      if (attemptedFly.getMass() >= .5 * this.age) {
        this.grow();
        attemptedFly.setMass(0);
      }
    } else {
      attemptedFly.grow(1);
    }
  }

  public String toString() {
    if (this.isFroglet) {
      return String.format("My name is %s and I'm a rare froglet! I'm %d months old and my tongue has a speed of %.2f.", this.name, this.age, this.tongueSpeed);
    } else {
      return String.format("My name is %s and I'm a rare frog. I'm %d months old and my tongue has a speed of %.2f.", this.name, this.age, this.tongueSpeed);
    }
  }

  public static void setSpecies(String newSpecies) {
    species = newSpecies;
  }

  public static String getSpecies() {
    return species;
  }

}
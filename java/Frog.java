// variables and constructors added

public class Frog {
  // instance variables
  private String name;
  private int age; // in months
  private double tongueSpeed;
  private boolean isFroglet;
  private static String species = "Rare Pepe";

  // constants
  public static final int DEFAULT_AGE = 5;
  public static final double DEFAULT_TONGUE_SPEED = 5;

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
  }


  // methods
  private 


  public static void main() {

  }
}
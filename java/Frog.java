// methods starting to be added

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
  private void grow () {

  }
  private void grow(int numMonths) {
    if (this.age >= 30) {
      this.tongueSpeed = Math.max(5, this.tongueSpeed - numMonths);
      } else if (this.age < 12) {
      this.tongueSpeed = Math.min(12, this.tongueSpeed + numMonths);
    }
    this.age += numMonths;
    if (this.age > 6) this.isFroglet = false;
  }


  public static void main() {

  }
}
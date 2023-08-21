// new fly objects created

public class Pond {
  public static void main() {
    Frog frogPeepo = new Frog("Peepo");
    Frog frogPepe = new Frog("Pepe", 10, 15);
    Frog frogPeepaw = new Frog("Peepaw", 4.6, 5);
    Frog frogPudu = new Frog("Pudu");
    Fly smallFly = new Fly(1, 3);
    Fly defaultFly = new Fly();
    Fly bigFly = new Fly(6);
  }
}
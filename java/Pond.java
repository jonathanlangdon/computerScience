// finished full program

public class Pond {
  public static void main(String[] args) {
    // The frogs are created
    Frog frogPeepo = new Frog("Peepo");
    Frog frogPepe = new Frog("Pepe", 10, 15);
    Frog frogPeepaw = new Frog("Peepaw", 4.6, 5);
    Frog frogPudu = new Frog("Pudu");

    // The flys are created
    Fly smallFly = new Fly(1, 3);
    Fly defaultFly = new Fly();
    Fly bigFly = new Fly(6);

    // The pond drama begins
    Frog.setSpecies("1331 Frogs");
    System.out.println(frogPeepo);
    frogPeepo.eat(bigFly);
    System.out.println(bigFly);
    frogPeepo.grow(8);
    frogPeepo.eat(bigFly);
    System.out.println(bigFly);
    System.out.println(frogPeepo);
    System.out.println(frogPudu);
    frogPudu.grow(3);
    Frog frog5 = new Frog("je", 5, 5);
    System.out.println(frog5);
    frog5.grow(8);
    System.out.println(frog5);
    System.out.println(frogPudu);
    frogPeepaw.grow(4);
    System.out.println(frogPeepaw);
    System.out.println(frogPepe);
    
    
  }
}
// updating methods

import java.util.Arrays;


public class RedAstronaut extends Player implements Impostor {
  private String skill;
  public static final int DEFAULT_SUS = 15;
  public static final String DEFAULT_SKILL = "experienced";

  //constructors
  public RedAstronaut(String name) {
    this(name, DEFAULT_SUS, DEFAULT_SKILL);
  }

  public RedAstronaut(String name, int susLevel, String skill) {
    super(name, susLevel);
    this.skill = skill;
  }

  public void emergencyMeeting() {
    System.out.println(String.format("%s is attempting to have a meeting", this.getName()));
    
    if (this.isFrozen()) {
      System.out.println(String.format("%s is frozen and can't have a meeting", this.getName()));
      return;
    }
    
    Player[] unfrozenPlayers = super.getPlayers();

    
    Arrays.sort(allPlayers);

    if (allPlayers.length == 0) {
      System.out.println("No eligible players to vote off.");
      return;
    }

    if (allPlayers.length > 1 && allPlayers[0].equals(allPlayers[1])) {
      System.out.println("Two players have the same highest susLevel, no one will be voted off.");
      return;
    }

    allPlayers[0].setFrozen(true);
    System.out.println(String.format("%s has been voted off.", allPlayers[0].getName()));

    if (gameOver()) {
      System.out.println("The game is over");
    } else {
      System.out.println("The game is not over");
    }

  }
}
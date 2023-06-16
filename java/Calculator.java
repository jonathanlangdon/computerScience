// assignment in my intro to Java class
// Basic calculator in terminal

import java.util.Scanner;

public class Calculator {
  static String[] array;
  public static void main(String[] args) {
    System.out.println("List of operations: add subtract multiply divide alphabetize");
    System.out.println("Enter an operation:");
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    input = input.toLowerCase();
      if (input.equals("add") || input.equals("subtract")) {
        int num1 = 0;
        int num2 = 0;
        System.out.println("Enter two integers:");
        GetInput(sc);
        try {
          num1 = Integer.parseInt(array[0]);
          num2 = Integer.parseInt(array[1]);
          System.out.printf("Answer: %d%n", (input.equals("add") ? (num1 + num2) : (num1 - num2)));
        } catch (Exception e) {InvalidStatement();}
      } else if (input.equals("multiply") || input.equals("divide")) {
        double num1 = 0;
        double num2 = 0;
        System.out.println("Enter two doubles:");
        GetInput(sc);
        try {
          num1 = Double.parseDouble(array[0]);
          num2 = Double.parseDouble(array[1]);
          switch (input) {
            case "multiply":
              System.out.printf("Answer: %.2f%n", num1 * num2);
              break;
            case "divide":
              if (num2 == 0) InvalidStatement();
              else System.out.printf("Answer: %.2f%n", num1 / num2);
              break;              
          }
        } catch (Exception e) {InvalidStatement();}
      } else if (input.equals("alphabetize")) {
        String str1 = "";
        String str2 = "";
        System.out.println("Enter two words:");
        GetInput(sc);
        try {
          str1 = array[0];
          str2 = array[1];
          int result = str1.compareToIgnoreCase(str2);
          if (result > 0) {
            System.out.printf("Answer: %s comes before %s alphabetically.%n", str2, str1);
          } else if (result < 0) {
            System.out.printf("Answer: %s comes before %s alphabetically.%n", str1, str2);
          } else System.out.println("Answer: Chicken or Egg.");
        } catch (Exception e) {InvalidStatement();}
      } else InvalidStatement();
  }

  public static void InvalidStatement() {
    System.out.println("Invalid input entered. Terminating...");
  }

  public static void GetInput(Scanner sc) {
    String items = sc.nextLine();
    array = items.split(" ");
  }
    
}
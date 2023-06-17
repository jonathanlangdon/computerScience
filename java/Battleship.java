import java.util.Scanner;
// import java.util.Arrays;

public class Battleship {
	public static void main(String[] args) {
		System.out.printf("Welcome to Battleship!%n%n");
		char[][] homeSea1 = new char[5][5];
		char[][] homeSea2 = new char[5][5];
		int [][] shipsArr1 = getHomeShips(1, homeSea1);
		int [][] shipsArr2 = getHomeShips(2, homeSea2);
		playGame();
	}

	// Use this method to print game boards to the console.
	private static void printBattleShip(char[][] player) {
		System.out.print("  ");
		for (int row = -1; row < 5; row++) {
			if (row > -1) {
				System.out.print(row + " ");
			}
			for (int column = 0; column < 5; column++) {
				if (row == -1) {
					System.out.print(column + " ");
				} else {
					System.out.print(player[row][column] + " ");
				}
			}
			System.out.println("");
		}
	}

	private static void playGame() {
		Scanner sc = new Scanner(System.in)
		char[][] enemySea1 = new char[5][5];
		char[][] enemySea2 = new char[5][5];
		int hits1 = 0;
		int hits2 = 0;
		while(hits1 < 5 && hits2 < 5) {
			int activePlayer = 1;
			System.out.printf("Player %d, enter hit row/column:", activePlayer);
		}
		sc.close();
		int winner = 0;
		if (hits1 == 5) winner = 1;
		else winner = 2;
		System.out.printf("PLAYER %d WINS! YOU SUNK ALL OF YOUR OPPONENT’S SHIPS!%n", winner);
	}

	private static int[][] getHomeShips(int playerNum, char[][] homeSea) {
		int[][] homeShips = new int[5][2];
		Scanner sc = new Scanner(System.in);
		System.out.printf("PLAYER %d, ENTER YOUR SHIPS’ COORDINATES.%n", playerNum);
		for (int i = 0; i < 5; i++) {
			Boolean validInput = false;
			do {
				try {
					System.out.printf("Enter ship %d location:%n", i+1);
					String input = sc.nextLine();
					String[] inputArr = input.split(" ");
					int num1 = Integer.parseInt(inputArr[0]);
					int num2 = Integer.parseInt(inputArr[1]);
					if (num1 > 4 || num2 > 4) throw new Exception();
					if(checkRepeats(num1, num2, homeShips)) {
						System.out.println("You already have a ship there. Choose different coordinates.");
						continue;
					}
					// checkRepeats(num1, num2, homeShips);
					homeShips[i][0] = num1;
					homeShips[i][1] = num2;
					validInput = true;
				} catch (Exception e) {
					System.out.println("Invalid coordinates. Choose different coordinates.");
				}
			} while (!validInput);
		}
		sc.close();
		fillSea(homeSea);
		for (int[] ship: homeShips) {
			homeSea[ship[0]][ship[1]] = '@';
		}
		printBattleShip(homeSea);
		for (int i = 0; i<100; i++) {
			System.out.printf("%n");
		}
		return homeShips;
	}
	
	private static void fillSea(char[][] sea) {
		for (char[] row: sea) {
			for (int col = 0; col < row.length; col++) {
				row[col] = '-';
			}
		}
	}

	private static boolean checkRepeats(int num1, int num2, int[][] shipsArr) {
		boolean match = false;
		for (int[] innerArray : shipsArr) {
			if (innerArray[0] == num1 && innerArray[1] == num2) {
				match = true;
				break;
			}
		}
		return match;
	}
}
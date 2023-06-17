import java.util.Scanner;
// import java.util.Arrays;

public class Battleship {
	public static void main(String[] args) {
		System.out.printf("Welcome to Battleship!%n%n");
		char[][] homeSea1 = new char[5][5];
		char[][] homeSea2 = new char[5][5];
		// int [][] shipsArr1 = getHomeShips(1, homeSea1);
		// int [][] shipsArr2 = getHomeShips(2, homeSea2);
		int[][] shipsArr1 = {{1,1},{1,2},{1,3},{1,4},{1,0}};
		int[][] shipsArr2 = {{2,1},{2,2},{2,3},{2,4},{2,0}};
		playGame(shipsArr1, shipsArr2);
	}
	
	private static void playGame(int[][] shipsArr1, int[][] shipsArr2) {
		char[][] enemySea1 = new char[5][5];
		char[][] enemySea2 = new char[5][5];
		int hitsOn1 = 0;
		int hitsOn2 = 0;
		while(hitsOn1 < 5 && hitsOn2 < 5) {
			// fireOnTarget(hitsOn2, 1, enemySea2, shipsArr2);
			hitsOn1 = fireOnTarget(hitsOn1, 2, enemySea1, shipsArr1);
			System.out.printf("Player 1 has %d hits and Player 2 has %d hits%n%n", hitsOn2, hitsOn1);
		}
		int winner = 0;
		if (hitsOn1 == 5) winner = 2;
		else winner = 1;
		System.out.printf("PLAYER %d WINS! YOU SUNK ALL OF YOUR OPPONENT’S SHIPS!%n", winner);
	}

	private static int fireOnTarget(int hits, int activePlayer, char[][] enemySea, int[][] shipsArr) {
		Scanner sc = new Scanner(System.in);
		System.out.printf("Player %d, enter hit row/column:", activePlayer);
		Boolean validInput = false;
		int num1 = 0;
		int num2 = 0;
		do {
			try {
				String input = sc.nextLine();
				String[] inputArr = input.split(" ");
				num1 = Integer.parseInt(inputArr[0]);
				num2 = Integer.parseInt(inputArr[1]);
				if (num1 > 4 || num2 > 4) throw new Exception();
				if(enemySea[num1][num2] == 'X' || enemySea[num1][num2] == 'O') {
					System.out.println("You already fired on this spot. Choose different coordinates.");
					continue;
				}
				validInput = true;
			} catch (Exception e) {
				System.out.println("Invalid coordinates. Choose different coordinates.");
			}
		} while (!validInput);
		int targetPlayer = activePlayer == 1 ? 2 : 1;
		boolean targetIsHit = false;
		for (int[] ship : shipsArr) {
			if (ship[0] == num1 && ship[1] == num2) {
				targetIsHit = true;
			}
		}
		if (targetIsHit) {
				System.out.printf("PLAYER %d HIT PLAYER %d’s SHIP!%n", activePlayer, targetPlayer);
				enemySea[num1][num2] = 'X';
				hits += 1;
			} else {
				System.out.printf("PLAYER %d MISSED!%n", activePlayer);
				enemySea[num1][num2] = 'O';
			}
		return hits;
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
					homeShips[i][0] = num1;
					homeShips[i][1] = num2;
					validInput = true;
				} catch (Exception e) {
					System.out.println("Invalid coordinates. Choose different coordinates.");
				}
			} while (!validInput);
		}
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

}
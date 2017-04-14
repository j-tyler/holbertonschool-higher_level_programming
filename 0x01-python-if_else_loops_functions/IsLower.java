import java.util.Scanner;

public class IsLower
{
	public static void main(String[] args)
	{
		System.out.print("Enter a character: ");
		Scanner sc = new Scanner(System.in);
		char c = sc.next().charAt(0);
		if (islower(c)) {
			System.out.println("Your character was lower case.");
		} else {
			System.out.println("Your character was not lower case.");
		}
	}

	private static boolean islower(char c)
	{
		if (c >= 'a' && c <= 'z') {
			return true;
		} else {
			return false;
		}
	}
}


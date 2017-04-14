import java.util.*;

public class ReplaceAt
{
	public static void main(String[] args)
	{
		List<String> messages = Arrays.asList("Hello", "World!", "How", "Are", "You");
		replaceAt(messages, 1, "LinkedIn");
		System.out.println(messages);
	}

	private static void replaceAt(List<String> msg, int idx, String s)
	{
		msg.set(idx, s);
	}
}

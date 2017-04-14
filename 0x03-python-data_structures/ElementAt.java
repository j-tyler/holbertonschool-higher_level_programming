import java.util.*;

public class ElementAt
{
	public static void main(String[] args)
	{
		List<String> messages = Arrays.asList("Hello", "World!", "How", "Are", "You");
		System.out.println(elementAt(messages, 1));
	}

	private static String elementAt(List<String> msg, int idx)
	{
		return (msg.get(idx));
	}
}

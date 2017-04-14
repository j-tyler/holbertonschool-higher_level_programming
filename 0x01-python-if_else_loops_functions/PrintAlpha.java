import java.util.stream.*;

public class PrintAlpha
{
	public static void main(String[] args)
	{
	    IntStream.range('a', 'z' + 1)
			.forEach(
        	n -> { System.out.println((char)n); }
		);
	}
}

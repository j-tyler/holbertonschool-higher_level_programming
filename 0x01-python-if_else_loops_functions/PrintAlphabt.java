import java.util.stream.*;

public class PrintAlphabt
{
	public static void main(String[] args)
	{
	    IntStream.range('a', 'z' + 1)
			.filter( n -> n != 'q' && n != 'e')
			.forEach( n -> System.out.println((char) n) );
	}
}

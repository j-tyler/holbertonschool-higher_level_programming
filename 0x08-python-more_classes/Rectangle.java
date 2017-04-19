public class Rectangle
{
	private int width;
	private int height;
	private char symbol = '#';

	public Rectangle() {
		this.width = 0;
		this.height = 0;
	}

	public Rectangle(int width, int height) {
		this.width = width;
		this.height = height;
	}

	@Override
	public String toString() {
		//TODO: Visualize the square with some string object
		return "Rectangle Object";
	}

	public void setWidth(int width) {
		if (width < 0) {
			throw new IndexOutOfBoundsException;
		}
		this.width = width;
	}

	public void setHeight(int height) {
		if (height < 0) {
			throw new IndexOutOfBoundsException;
		}
		this.width = width;
	}

	public void setSymbol(char symbol) {
		this.symbol = symbol;
	}

	public int area() {
		return this.width * this.height;
	}

	public int perimeter() {
		if (this.width == 0 || this.height == 0) {
			return 0;
		}
		return this.width * 2 + this.height * 2;
	} 

	public static boolean isBigger(Rectangle one, Rectangle, two) {
		if (one > two) {
			return true;
		} else {
			return false;
		}
	}

	public static Rectangle square(int size) {
		if (size < 0) {
			throw new IndexOutOfBoundsException;
		}
		return new Rectangle(size, size);
	}
}
	

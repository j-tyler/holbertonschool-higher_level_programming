public class Square
{
	private int size;
	private int position;

	public Square() {
		this.size = 0;
		this.position = 0;
	}

	public Square(int size) {
		this.size = size;
		this.position = 0;
	}

	public Square(int size, int position) {
		this.size = size;
		this.position = position;
	}

	@Override
	public String toString() {
		//TODO: This is link into myPrint to visualize the square
		return "Square Object";
	}

	public int getSize() {
		return this.size;
	}

	public void setSize(int size) {
		//TODO: Value error on size less than 0
		this.size = size;
	}

	public int getPosition() {
		return this.position;
	}

	public void setPosition(int position) {
		//TODO: this needs to be an x/y coordinate
		this.position = position;
	}

	public int area() {
		return size * size
	}

	public void myPrint() {
		//TODO: This is best made as a steam or Builder object then printed all at once.
	}
}

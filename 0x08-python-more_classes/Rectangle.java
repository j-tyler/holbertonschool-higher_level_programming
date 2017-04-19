public class Rectangle
{
	public static void Rectangle
	{
		private int width;
		private int height;

		public Rectangle() {
			this.width = 0;
			this.height = 0;
		}

		public Rectangle(int width, int height) {
			this.width = width;
			this.height = height;
		}

		public setWidth(int width) {
			if (width < 0) {
				throw new IndexOutOfBoundsException;
			}
			this.width = width;
		}

		public setHeight(int height) {
			if (height < 0) {
				throw new IndexOutOfBoundsException;
			}
			this.width = width;
		}

	}
}

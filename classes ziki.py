import matplotlib.pyplot as plt


class CoordinatePlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.x_coordinates = []
        self.y_coordinates = []

    def read_coordinates(self):
        """Reads coordinates from the specified file."""
        with open(self.file_path, "r") as my_file:
            my_file.readline()  # Skip the header
            for line in my_file:
                x, y = map(float, line.split(', '))
                self.x_coordinates.append(x)
                self.y_coordinates.append(y)

    def translate_coordinates(self, translation_x, translation_y):
        """Translates the coordinates by the specified amounts."""
        self.translated_x = [x + translation_x for x in self.x_coordinates]
        self.translated_y = [y + translation_y for y in self.y_coordinates]

    def plot(self):
        """Creates a scatter plot of the original and translated coordinates."""
        plt.scatter(self.x_coordinates, self.y_coordinates, color='red', label='Original Points')
        plt.scatter(self.translated_x, self.translated_y, color='black', label='Translated Points')

        # Add labels and title
        plt.ylabel('Y Coordinates')
        plt.xlabel('X Coordinates')
        plt.title('Scatter Plot of X and Y coordinates')
        plt.grid(True)
        plt.legend()  # Show legend
        plt.show()


def main():
    # Specify the path to the coordinates file
    file_path = "C:/Users/MY PC/Downloads/x_y_coordinates.txt"

    # Create an instance of CoordinatePlotter
    plotter = CoordinatePlotter(file_path)

    # Read coordinates from the file
    plotter.read_coordinates()


    plotter.translate_coordinates(1, 1)

    # Plot the coordinates
    plotter.plot()


# Run the main function
if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
from typing import List


def plot_movie_oscars(
    movies: List[str],
    num_oscars: List[int],
    title: str = "My Favorite Movies",
    output_file: str = "favorite_movies.png",
):
    """
    Plots a bar chart of movies and their respective number of Oscars.

    Parameters:
    movies (list of str): List of movie titles.
    num_oscars (list of int): List of number of Oscars each movie has won.
    title (str): Title of the bar chart.
    output_file (str): File name to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(movies)), num_oscars, color="skyblue")
    plt.title(title, fontsize=14)
    plt.ylabel("# of Academy Awards", fontsize=12)
    plt.xlabel("Movies", fontsize=12)
    plt.xticks(range(len(movies)), movies, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()


if __name__ == "__main__":
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    plot_movie_oscars(movies, num_oscars)

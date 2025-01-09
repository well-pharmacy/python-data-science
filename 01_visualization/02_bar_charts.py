import matplotlib.pyplot as plt
from typing import List
from collections import Counter


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


def plot_grade_distribution(grades: List[int]):
    """
    Plots a histogram of grades.

    Parameters:
    grades (list of int): List of grades.
    """
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
    plt.bar(
        [x + 5 for x in histogram.keys()],  # Shift bars right by 5
        histogram.values(),  # Give each bar its correct height
        10,  # Give each bar a width of 10
        edgecolor=(0, 0, 0),
    )  # Black edges for each bar
    plt.axis([-5, 105, 0, 5])  # x-axis from -5 to 105, y-axis from 0 to 5
    plt.xticks([10 * i for i in range(11)])  # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.savefig("grade_distribution.png", dpi=300)
    plt.close()


def plot_data_science_mentions(years: List[int], mentions: List[int]):
    """
    Plots a bar chart of mentions of 'data science' over the years.

    Parameters:
    years (list of int): List of years.
    mentions (list of int): List of mentions of 'data science'.
    """
    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")
    plt.ticklabel_format(useOffset=False)
    plt.axis([2016.5, 2018.5, 499, 506])
    plt.title("Look at the 'Huge' Increase!")
    plt.savefig("data_science_mentions.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    plot_movie_oscars(movies, num_oscars, "Favorite Movies", "favorite_movies.png")

    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    plot_grade_distribution(grades)

    years = [2017, 2018]
    mentions = [500, 505]
    plot_data_science_mentions(years, mentions)

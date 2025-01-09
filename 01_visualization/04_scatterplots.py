import matplotlib.pyplot as plt


def plot_friends_vs_minutes(
    friends, minutes, labels, title="Daily Minutes vs. Number of Friends"
):
    """
    Plots a scatter plot of daily minutes vs. number of friends.

    Parameters:
    friends (list of int): List of number of friends.
    minutes (list of int): List of daily minutes spent on the site.
    labels (list of str): List of labels for each point.
    title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(friends, minutes, color="blue", edgecolor="black", alpha=0.7)

    # Label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(
            label,
            xy=(friend_count, minute_count),  # Put the label with its point
            xytext=(5, -5),  # but slightly offset
            textcoords="offset points",
            fontsize=9,
            weight="bold",
        )

    # Adding labels and title
    plt.title(title, fontsize=16, weight="bold")
    plt.xlabel("# of friends", fontsize=14)
    plt.ylabel("Daily minutes spent on the site", fontsize=14)

    # Adding grid
    plt.grid(True, linestyle="--", alpha=0.7)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig("friends_vs_minutes.png", dpi=300)

    # Close the plot
    plt.close()


def plot_test_grades(test_1_grades, test_2_grades, title="Axes Are Comparable"):
    """
    Plots a scatter plot of test 1 grades vs. test 2 grades.

    Parameters:
    test_1_grades (list of int): List of test 1 grades.
    test_2_grades (list of int): List of test 2 grades.
    title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(test_1_grades, test_2_grades, color="red", edgecolor="black", alpha=0.7)

    # Adding labels and title
    plt.title(title, fontsize=16, weight="bold")
    plt.xlabel("Test 1 Grade", fontsize=14)
    plt.ylabel("Test 2 Grade", fontsize=14)

    # Ensure the axes are equal
    plt.axis("equal")

    # Adding grid
    plt.grid(True, linestyle="--", alpha=0.7)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig("test_grades_comparison.png", dpi=300)

    # Close the plot
    plt.close()


if __name__ == "__main__":
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    plot_friends_vs_minutes(friends, minutes, labels)

    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    plot_test_grades(test_1_grades, test_2_grades)

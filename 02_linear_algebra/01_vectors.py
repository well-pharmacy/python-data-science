import matplotlib.pyplot as plt
import numpy as np
from typing import List
import math

Vector = List[float]


def add(v1: Vector, v2: Vector) -> Vector:
    return [x + y for x, y in zip(v1, v2)]


def subtract(v1: Vector, v2: Vector) -> Vector:
    return [x - y for x, y in zip(v1, v2)]


def vector_sum(vectors: List[Vector]) -> Vector:
    return [sum(components) for components in zip(*vectors)]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * x for x in v]


def sum_of_squares(v: Vector) -> float:
    return sum(x * x for x in v)

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))


def plot_vectors(vectors: List[Vector], colors=None, labels=None, title="Vector Plot"):
    """
    Plots vectors in 2D space.

    Parameters:
    vectors (list of vectors): List of vectors to plot. Each vector is a tuple (x, y).
    colors (list of str): List of colors for each vector. Default is None.
    labels (list of str): List of labels for each vector. Default is None.
    title (str): Title of the plot. Default is "Vector Plot".
    """
    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    # Set colors and labels if not provided
    if colors is None:
        colors = ["b"] * len(vectors)
    if labels is None:
        labels = [f"v{i}" for i in range(len(vectors))]

    # Plot each vector
    for vector, color, label in zip(vectors, colors, labels):
        ax.quiver(
            0,
            0,
            vector[0],
            vector[1],
            angles="xy",
            scale_units="xy",
            scale=1,
            color=color,
            label=label,
        )
        ax.text(vector[0], vector[1], f" {label}", fontsize=12, ha="right")

    # Set limits
    all_vectors = np.array(vectors)
    max_val = np.max(np.abs(all_vectors)) * 1.1
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)

    # Adding labels and title
    plt.xlabel("X-axis", fontsize=14)
    plt.ylabel("Y-axis", fontsize=14)
    plt.title(title, fontsize=16, weight="bold")

    # Adding grid
    plt.grid(True, linestyle="--", alpha=0.7)

    # Adding legend
    plt.legend(loc="upper left", fontsize=12)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig("vector_plot.png", dpi=300)

    # Close the plot
    plt.close()


if __name__ == "__main__":
    v1 = [1, 2]
    v2 = [2, 1]
    v3 = [3, 3]
    sum_v = vector_sum([v1, v2, v3])
    mean_v = vector_mean([v1, v2, v3])
    scalar_v = scalar_multiply(2, v1)
    vectors: List[Vector] = [v1, v2, v3, sum_v, mean_v, scalar_v]
    colors = ["r", "g", "b", "m", "c", "y"]
    labels = ["v1", "v2", "v3", "v1 + v2 + v3", "mean(v1, v2, v3)", "2 * v1"]
    plot_vectors(
        vectors, colors, labels, title="Vector Sum, Mean, and Scalar Multiplication"
    )
    print("Vector plot saved as vector_plot.png")

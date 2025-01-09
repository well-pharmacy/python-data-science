import matplotlib.pyplot as plt
import numpy as np

from typing import List

Vector = List[float]


def add_vectors(v1: Vector, v2: Vector) -> Vector:
    """
    Adds two vectors component-wise.

    Parameters:
    v1 (Vector): First vector.
    v2 (Vector): Second vector.

    Returns:
    Vector: Sum of the two vectors.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length.")
    return [v1_i + v2_i for v1_i, v2_i in zip(v1, v2)]


def plot_vectors(vectors, colors=None, labels=None, title="Vector Plot"):
    """
    Plots vectors in 2D space.

    Parameters:
    vectors (list of tuples): List of vectors to plot. Each vector is a tuple (x, y).
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
    sum_v = add_vectors(v1, v2)
    vectors: List[Vector] = [v1, v2, sum_v]
    colors = ["r", "g", "b"]
    labels = ["v1", "v2", "v3"]
    plot_vectors(vectors, colors, labels)
    print("Vector plot saved as vector_plot.png")

import matplotlib.pyplot as plt


def plot_bias_variance_tradeoff(
    variance, bias_squared, title="The Bias-Variance Tradeoff"
):
    """
    Plots the Bias-Variance Tradeoff.

    Parameters:
    variance (list of int): List of variance values.
    bias_squared (list of int): List of bias squared values.
    title (str): Title of the plot.
    """
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(xs, variance, "g-", label="Variance", linewidth=2)  # green solid line
    plt.plot(
        xs, bias_squared, "r-.", label="Bias^2", linewidth=2
    )  # red dot-dashed line
    plt.plot(
        xs, total_error, "b:", label="Total Error", linewidth=2
    )  # blue dotted line

    # Adding labels and title
    plt.xlabel("Model Complexity", fontsize=14)
    plt.ylabel("Error", fontsize=14)
    plt.title(title, fontsize=16, weight="bold")

    # Adding grid
    plt.grid(True, linestyle="--", alpha=0.7)

    # Adding legend
    plt.legend(loc="upper center", fontsize=12)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig("bias_variance_tradeoff.png", dpi=300)

    # Close the plot
    plt.close()

if __name__ == "__main__":
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    plot_bias_variance_tradeoff(variance, bias_squared)

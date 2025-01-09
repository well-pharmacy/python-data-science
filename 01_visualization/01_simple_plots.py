import matplotlib.pyplot as plt

# Check available styles
print(plt.style.available)

# Use an available style
plt.style.use("ggplot")  # Replace 'ggplot' with any available style you prefer

# Data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Set figure size and style
plt.figure(figsize=(12, 8))

# Create the plot
plt.plot(
    years,
    gdp,
    color="#2ecc71",  # Green color
    marker="o",
    markersize=10,
    linewidth=2.5,
    linestyle="-",
)

# Customize the plot
plt.title(
    f"U.S. Nominal GDP ({min(years)}-{max(years)})", fontsize=18, pad=20, weight="bold"
)
plt.ylabel("Billions of USD", fontsize=14)
plt.xlabel("Year", fontsize=14)

# Add grid for better readability
plt.grid(True, linestyle="--", alpha=0.7)

# Format y-axis to show billions with comma separator
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot as an image
plt.savefig("us_nominal_gdp.png", dpi=300)

# Show the plot
plt.show()

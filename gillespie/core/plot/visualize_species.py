import matplotlib.pyplot as plt
from pathlib import Path


def plot(time, species, name, save=False, save_path: Path = None):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    for i in range(3):
        ax.set_title(f"Number of {name} molecules")
        ax.set_xlabel("Time (hours)")
        ax.set_ylabel("Counts")

    # Plot each simulated trajectory
    for i in range(time.shape[0]):
        ax.plot(
            time[i, :],
            species[name][i, :],
            marker="",
            color="grey",
            linewidth=0.6,
            alpha=0.3,
        )

    # Plot the mean
    ax.plot(
        time[0, :],
        species[name].mean(axis=0),
        marker="",
        color="blue",
        linewidth=2,
        alpha=0.8,
    )

    if save:
        fig.savefig(save_path / f"{name}.png")

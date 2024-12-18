import matplotlib.pyplot as plt
from pathlib import Path
from ..result import Result


def plot_species(res: Result, name: str, save: bool = False, save_path: Path = None):
    """
    Plot the number of molecules of a given species over time.

    Args:
    - res: Result object with the simulation results.
    - name: Name of the species to plot.
    - save: If True, save the figure.
    - save_path: Path to save the figure

    Returns:
    - None
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    for i in range(3):
        ax.set_title(f"Number of {name} molecules")
        ax.set_xlabel("Time (hours)")
        ax.set_ylabel("Counts")

    # Plot each simulated trajectory
    for i in range(res.time.shape[0]):
        ax.plot(
            res.time[i, :],
            res.species[name][i, :],
            marker="",
            color="grey",
            linewidth=0.6,
            alpha=0.3,
        )

    # Plot the mean
    ax.plot(
        res.time[0, :],
        res.species[name].mean(axis=0),
        marker="",
        color="blue",
        linewidth=2,
        alpha=0.8,
    )

    if save:
        fig.savefig(save_path / f"{name}.png")


def plot_simulation_by_id(
    res: Result, sim_id: int, save: bool = False, save_path: Path = None
):
    """
    Plot the number of molecules of each species over time for a given simulation.

    Args:
    - res: Result object with the simulation results.
    - sim_id: Simulation ID to plot.
    - save: If True, save the figure.
    - save_path: Path to save the figure

    Returns:
    - None
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    for i in range(3):
        ax.set_title(f"Simulation {sim_id}")
        ax.set_xlabel("Time (hours)")
        ax.set_ylabel("Counts")

    # Plot each species
    for name in res.species.keys():
        ax.plot(
            res.time[sim_id, :],
            res.species[name][sim_id, :],
            marker="",
            label=name,
            linewidth=2,
        )

    ax.legend()
    if save:
        fig.savefig(save_path / f"simulation_{sim_id}.png")


def plot_all_species(
    res: Result, save: bool = False, save_path: Path = None, one_plot: bool = False
):
    """
    Plot the number of molecules of each species in a simulation result.

    Args:
    - res: Result object with the simulation results.
    - save: If True, save the figure.
    - save_path: Path to save the figure

    Returns:
    - None
    """
    species = list(res.species.keys())
    if one_plot:
        fig, ax = plt.subplots(2, 3, figsize=(15, 10))
        for i in range(3):
            ax[1, i].set_title(f"Number of {species[i]} molecules")
            ax[1, i].set_xlabel("Time (hours)")
            ax[1, i].set_ylabel("Counts")

        for i in range(3):
            ax[0, i].set_title(f"Number of {species[i+3]} molecules")
            ax[0, i].set_xlabel("Time (hours)")
            ax[0, i].set_ylabel("Counts")

        for i in range(3):
            for j in range(res.time.shape[0]):
                ax[1, i].plot(
                    res.time[j, :],
                    res.species[species[i]][j, :],
                    marker="",
                    color="grey",
                    linewidth=0.6,
                    alpha=0.3,
                )
                ax[0, i].plot(
                    res.time[j, :],
                    res.species[species[i + 3]][j, :],
                    marker="",
                    color="grey",
                    linewidth=0.6,
                    alpha=0.3,
                )
            ax[1, i].plot(
                res.time[0, :],
                res.species[species[i]].mean(axis=0),
                marker="",
                color="blue",
                linewidth=2,
                alpha=0.8,
            )
            ax[0, i].plot(
                res.time[0, :],
                res.species[species[i + 3]].mean(axis=0),
                marker="",
                color="blue",
                linewidth=2,
                alpha=0.8,
            )
        if save:
            fig.savefig(save_path / "all_species.png")
    else:
        for s in species:
            plot_species(res, s, save, save_path)


def plot_all_simulations(res: Result, save: bool = False, save_path: Path = None):
    """
    Plot the number of molecules of each species in all simulations.

    Args:
    - res: Result object with the simulation results.
    - save: If True, save the figure.
    - save_path: Path to save the figure

    Returns:
    - None
    """
    for i in range(res.time.shape[0]):
        plot_simulation_by_id(res, i, save, save_path)

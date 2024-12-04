import matplotlib.pyplot as plt
from . import DataStruct
import numpy as np


class PlotStruct:

    # ------------------------------------------
    # Setup

    def __init__(self, dataStruct: DataStruct):

        self.setupAttributes(dataStruct)
        return

    def setupAttributes(self, dataStruct):

        self.data = dataStruct

        self.figure = None
        outputPath = None

    # ------------------------------------------
    # Special Functions

    def __del__(self):

        plt.saveFig()

    # ------------------------------------------
    # Utilities

    def createPlotRandTraject(self, n2plot, path):

        is2plot = np.random.choice(
            list(range(self.data.trajectories)), size=n2plot, replace=False
        )

        fig, axs = plt.subplots(n2plot, 1, figsize=(10, 20))
        molecule_type = [
            "TF Protein",
            "TF mRNA",
            "T RNA",
            "T Protein",
            "miRNA",
            "Complex",
        ]
        d = self.data
        axis = 0

        for i in is2plot:

            axs[axis].set_title(f"Number of molecules")
            axs[axis].set_xlabel("Time (hours)")
            axs[axis].set_ylabel("Counts")

            axs[axis].plot(
                self.data.timestamps[i, :],
                d.concentration_tf[i, :],
                marker="",
                color="red",
                linewidth=2.0,
                alpha=0.3,
            )
            axs[axis].plot(
                self.data.timestamps[i, :],
                d.concentration_tf_mrna[i, :],
                marker="",
                color="blue",
                linewidth=2.0,
                alpha=0.3,
            )
            axs[axis].plot(
                self.data.timestamps[i, :],
                d.concentration_t_rna[i, :],
                marker="",
                color="black",
                linewidth=2.0,
                alpha=0.3,
            )
            axs[axis].plot(
                self.data.timestamps[i, :],
                d.concentration_t[i, :],
                marker="",
                color="green",
                linewidth=2.0,
                alpha=0.3,
            )
            axs[axis].plot(
                self.data.timestamps[i, :],
                d.concentration_mi_rna[i, :],
                marker="",
                color="orange",
                linewidth=2.0,
                alpha=0.3,
            )
            axs[axis].plot(
                self.data.timestamps[i, :],
                d.concentration_complex[i, :],
                marker="",
                color="violet",
                linewidth=2.0,
                alpha=0.3,
            )

            axs[axis].legend(molecule_type)
            axis += 1

            continue
        plt.savefig(path)
        return

    def clearAll(self):
        plt.close("all")

    def saveFig(self, path):

        if self.figure == None:
            return

        plt.savefig(path)

import argparse
import logging
import pandas as pd
from pathlib import Path
from enum import Enum
from .core import Simulation
from .core.io import parse
from .core.plot import plot_all_simulations, plot_all_species

LOGGER = logging.getLogger(__name__)


class LogLevels(Enum):
    """Log level enumerator."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def setup_logging(verbosity: str = "INFO") -> None:
    """Configure logging.

    Args:
        verbosity: Level of logging verbosity.
    """
    level = LogLevels[verbosity].value
    logging.basicConfig(
        level=level,
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def create_parser():
    """
    Create a parser for the command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Gillespie simulation of TF chemical reaction system."
    )
    parser.add_argument(
        "--config",
        type=str,
        help=(
            "Path to the configuration file. [required]."
            "Allowed file formats: .csv, .json, .yaml."
            "AlloWed keys: rates, initial_states."
        ),
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to the output file. Default to /<current-dir>/output",
        default=None,
    )

    parser.add_argument(
        "--num-simulations",
        type=int,
        help="Number of simulations to run. Default is 10.",
        default=10,
    )
    parser.add_argument(
        "--num-timepoints",
        type=int,
        help="Number of timepoints to simulate. Default is 1000.",
        default=1000,
    )
    parser.add_argument(
        "--verbosity",
        choices=[e.name for e in LogLevels],
        default=LogLevels.INFO.name,
        type=str,
        help="Logging verbosity level.",
    )
    parser.add_argument(
        "--plot-all-simulations",
        action="store_true",
        help="Plot the results of all simulations.",
        default=False,
    )
    parser.add_argument(
        "--plot-all-species",
        action="store_true",
        help="Plot the results of all species.",
        default=False,
    )

    parser.add_argument("--seed", type=int, help="Random seed.", default=None)
    return parser


def main():
    """
    Main function for the command line interface. Parses the arguments and runs the simulation.
    """
    setup_logging()
    parser = create_parser()
    args = parser.parse_args()

    if not args.config:
        parser.error("Configuration file is required.")
        parser.print_help()
        sys.exit(1)

    config = parse(args.config)
    sim = Simulation(num_trajectories=args.num_simulations, steps=args.num_timepoints)
    LOGGER.info("Starting simulation.")
    res = sim.simulate(
        rates=config["rates"], initial_states=config["initial_states"], seed=args.seed
    )
    LOGGER.info("Simulation finished.")
    LOGGER.info("Writing results to output directory.")

    output_dir = Path(args.output) if args.output else Path("output")
    output_dir.mkdir(exist_ok=True)

    time_df = pd.DataFrame(
        data=res.time, columns=[f"time_{i}" for i in range(res.time.shape[1])]
    )
    time_df.to_csv(output_dir / "time.csv", index=False)
    for s in res.species:
        df = pd.DataFrame(
            data=res.species[s].T,
            columns=[f"{s}_{i}" for i in range(res.species[s].shape[0])],
        )
        df.to_csv(output_dir / f"{s}.csv", index=False)
    LOGGER.info("Results written to output directory.")
    plot_dir = output_dir / "plots"
    # remove the directory if it exists
    if plot_dir.exists():
        # remove all files in the directory
        for file in plot_dir.iterdir():
            file.unlink()
        plot_dir.rmdir()
    if args.plot_all_species:
        LOGGER.info("Plotting all species.")
        plot_dir.mkdir(exist_ok=True)
        plot_all_species(res, save=True, save_path=plot_dir)
        LOGGER.info("Plots saved to output directory.")

    if args.plot_all_simulations:
        LOGGER.info("Plotting all simulations.")
        plot_dir.mkdir(exist_ok=True)
        plot_all_simulations(res, save=True, save_path=plot_dir)
        LOGGER.info("Plots saved to output directory.")


if __name__ == "__main__":
    main()

import tempfile
from pathlib import Path

import numpy as np

from gillespie.core.plot import (
    plot_all_simulations,
    plot_all_species,
    plot_simulation_by_id,
    plot_species,
)
from gillespie.core.result import Result


def generate_dummy_result():
    time = np.linspace(0, 10, 100)
    species = {
        "mRNA_TF": np.random.rand(10, 100),
        "protein_TF": np.random.rand(10, 100),
        "mRNA_T": np.random.rand(10, 100),
        "protein_T": np.random.rand(10, 100),
        "miRNA": np.random.rand(10, 100),
        "complex": np.random.rand(10, 100),
    }
    return Result(time=np.tile(time, (10, 1)), species=species)


def test_plot_species():
    res = generate_dummy_result()
    with tempfile.TemporaryDirectory() as tmpdirname:
        save_path = Path(tmpdirname)
        plot_species(res, "mRNA_TF", save=True, save_path=save_path)
        assert (save_path / "mRNA_TF.png").exists(), "mRNA_TF.png not found"


def test_plot_simulation_by_id():
    res = generate_dummy_result()
    with tempfile.TemporaryDirectory() as tmpdirname:
        save_path = Path(tmpdirname)
        plot_simulation_by_id(res, 0, save=True, save_path=save_path)
        assert (save_path / "simulation_0.png").exists(), "simulation_0.png not found"


def test_plot_all_species():
    res = generate_dummy_result()
    with tempfile.TemporaryDirectory() as tmpdirname:
        save_path = Path(tmpdirname)
        plot_all_species(res, save=True, save_path=save_path)
        for species in res.species.keys():
            assert (save_path / f"{species}.png").exists(), f"{species}.png not found"


def test_plot_all_simulations():
    res = generate_dummy_result()
    with tempfile.TemporaryDirectory() as tmpdirname:
        save_path = Path(tmpdirname)
        plot_all_simulations(res, save=True, save_path=save_path)
        for i in range(res.time.shape[0]):
            assert (
                save_path / f"simulation_{i}.png"
            ).exists(), f"simulation_{i}.png not found"

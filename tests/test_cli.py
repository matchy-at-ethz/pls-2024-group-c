import subprocess
import os
import tempfile
import pandas as pd
from pathlib import Path


def test_cli():
    # Create a temporary directory for output
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Define the path to the configuration file
        config_path = "examples/config.json"

        # Run the CLI script
        result = subprocess.run(
            [
                "gillespie",
                "--config",
                config_path,
                "--output",
                tmpdirname,
                "--verbosity",
                "INFO",
                "--plot",
            ],
            capture_output=True,
            text=True,
        )

        # Check if the script ran successfully
        assert result.returncode == 0, f"CLI script failed with error: {result.stderr}"

        # Check if the output files are created
        output_dir = Path(tmpdirname)
        assert (
            output_dir / "time.csv"
        ).exists(), "time.csv not found in output directory"
        for species in [
            "mRNA_TF",
            "protein_TF",
            "mRNA_T",
            "protein_T",
            "miRNA",
            "complex",
        ]:
            assert (
                output_dir / f"{species}.csv"
            ).exists(), f"{species}.csv not found in output directory"

        # Optionally, check the contents of the output files
        time_df = pd.read_csv(output_dir / "time.csv")
        assert not time_df.empty, "time.csv is empty"
        for species in [
            "mRNA_TF",
            "protein_TF",
            "mRNA_T",
            "protein_T",
            "miRNA",
            "complex",
        ]:
            df = pd.read_csv(output_dir / f"{species}.csv")
            assert not df.empty, f"{species}.csv is empty"

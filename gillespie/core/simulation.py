import numpy as np
from typing import Dict
import random
from .result import Result


class Simulation:

    species: Dict[str, np.ndarray] = {
        "mRNA_TF": None,
        "protein_TF": None,
        "mRNA_T": None,
        "protein_T": None,
        "miRNA": None,
        "complex": None,
    }

    rates = {
        "a_T": 0.1,
        "mu_T": 0.1,
        "pi_T": 0.1,
        "mu_Q": 0.1,
        "alpha_s": 0.1,
        "k_s": 0.1,
        "mu_s": 0.1,
        "alpha_R": 0.1,
        "k_R": 0.1,
        "mu_R": 0.1,
        "beta": 0.1,
        "mu_c": 0.1,
        "pi_R": 0.1,
    }

    def __init__(
        self,
        rates=None,
        num_trajectories=100,
        steps=1000,
        initial_states: Dict[str, float] = None,
    ):
        # update rates if provided
        if rates:
            for key in rates:
                self.rates[key] = rates[key]

        self.reactions = [
            # constant transcription of TF mRNA
            lambda _: self.rates["a_T"],
            # constant degradation of TF mRNA
            lambda states: self.rates["mu_T"] * states["mRNA_TF"],
            # constant translation of TF protein
            lambda states: self.rates["pi_T"] * states["mRNA_TF"],
            # constant degradation of TF protein
            lambda states: self.rates["mu_Q"] * states["protein_TF"],
            # michaelis-menten transcription of miRNA
            lambda states: self.rates["alpha_s"]
            * states["protein_TF"]
            / (self.rates["k_s"] + states["protein_TF"]),
            # constant degradation of miRNA
            lambda states: self.rates["mu_s"] * states["miRNA"],
            # michaelis-menten transcription of T mRNA
            lambda states: self.rates["alpha_R"]
            * states["miRNA"]
            / (self.rates["k_R"] + states["miRNA"]),
            # constant degradation of T mRNA
            lambda states: self.rates["mu_R"] * states["mRNA_T"],
            # constant translation of T protein
            lambda states: self.rates["pi_R"] * states["mRNA_T"],
            # constant degradation of T protein
            lambda states: self.rates["mu_R"] * states["protein_T"],
            # miRNA-mRNA complex formation
            lambda states: self.rates["beta"] * states["miRNA"] * states["mRNA_T"],
            # complex degradation (miRNA mediated mRNA degradation)
            lambda states: self.rates["mu_c"] * states["complex"],
        ]

        self.stoichiometry = [
            # constant transcription of TF mRNA
            {"mRNA_TF": 1},
            # constant degradation of TF mRNA
            {"mRNA_TF": -1},
            # constant translation of TF protein
            {"protein_TF": 1},
            # constant degradation of TF protein
            {"protein_TF": -1},
            # michaelis-menten transcription of miRNA
            {"miRNA": 1},
            # constant degradation of miRNA
            {"miRNA": -1},
            # michaelis-menten transcription of T mRNA
            {"mRNA_T": 1},
            # constant degradation of T mRNA
            {"mRNA_T": -1},
            # constant translation of T protein
            {"protein_T": 1},
            # constant degradation of T protein
            {"protein_T": -1},
            # miRNA-mRNA complex formation
            {"miRNA": -1, "mRNA_T": -1, "complex": 1},
            # complex degradation (miRNA mediated mRNA degradation)
            {"complex": -1},
        ]

        # sanity check
        assert len(self.reactions) == len(self.stoichiometry)

        self.num_trajectories = num_trajectories
        self.steps = steps

        for key in self.species:
            self.species[key] = np.zeros((num_trajectories, steps + 1))

        if initial_states:
            for key in initial_states:
                self.species[key][:, 0] = initial_states[key]

    def simulate(self, rates=None, initial_sates: Dict[str, float] = None) -> Result:
        """
        Simulate the chemical reaction system using the Gillespie algorithm.
        """
        T = np.zeros((self.num_trajectories, self.steps + 1))
        if initial_sates is not None:
            for key in self.species:
                self.species[key][:, 0] = initial_sates[key]

        for i in range(self.num_trajectories):
            for j in range(self.steps):
                # get the current state
                states = {key: self.species[key][i, j] for key in self.species}

                # calculate rates with respective propensities
                rates = [reaction(states) for reaction in self.reactions]

                if np.all(np.array(rates) == 0):
                    break

                # randomly draw one transition
                reaction = random.choices(self.stoichiometry, weights=rates)[0]

                # update the state
                for key in self.species:
                    self.species[key][i, j + 1] = states[key] + reaction.get(key, 0)

                dt = random.expovariate(sum(rates))
                T[i, j + 1] = T[i, j] + dt

        return Result(time=T, species=self.species)

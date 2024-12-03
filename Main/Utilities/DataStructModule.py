import numpy as np


class DataStruct:

    # ------------------------------------------
    # Setup

    def __init__(self, data:dict):
        """
        I generally split up the init function for visibillity
        """

        self.setupAttributes(data)

        return

    def setupAttributes(self, data):
        """
        Initializes the Parameters
        """
        self.timestamps = np.zeros((data["trajectories"], 1))
        self.timestamps[:, 0] = data["protein"]["1"]["init"]
        self.concentration_tf_mrna = np.zeros((data["trajectories"], 1))
        self.concentration_tf_mrna[:, 0] = 0
        self.concentration_tf = np.zeros((data["trajectories"], 1))
        self.concentration_tf[:, 0] = data["TF"]["init" ]
        self.concentration_mi_rna = np.zeros((data["trajectories"], 1))
        self.concentration_mi_rna[:, 0] = data["mRNA"]["mirna"]["init"]
        self.concentration_t_rna = np.zeros((data["trajectories"], 1))
        self.concentration_t_rna[:, 0] = data["mRNA"]["tmRNA" ]["init"]
        self.concentration_t = np.zeros((data["trajectories"], 1))
        self.concentration_t[:, 0] = data["protein"]["2"]["init"] 
        self.concentration_complex = np.zeros((data["trajectories"], 1))
        self.concentration_complex[:, 0] = 0

        self.events = np.zeros((data["trajectories"], 1))

        self.current_step = 0
        self.trajectories = data["trajectories"]

        self.alpha_t = 20
        self.mu_t = 0.2
        self.mu_q = data["protein"]["1"]["decay"]
        self.alpha_s = data["mRNA"]["mirna"]["alpha_s"]
        self.mu_s = data["mRNA"]["mirna"]["decay"]
        self.k_r = data["mRNA"]["tmRNA" ]["ks"]
        self.k_s = data["mRNA"]["mirna"]["ks"]  # dont set em to integrs
        self.alpha_r = data["mRNA"]["tmRNA" ]["alpha_s"]
        self.mu_r = data["mRNA"]["tmRNA" ]["decay"]
        self.pi_h = 4  # pi_r
        self.mu_h = data["mRNA"]["tmRNA" ]["decay"]  # mu_r duplikat
        self.mu_c = data["muc"]
        self.beta = data["beta"]

    # ------------------------------------------
    # Update

    def update(self):
        """
        Adds another datapoint every time it is called
        """
        self.duplicateAllValues()  # duplicate the last values into the new column, then add the column

        for trajectory in range(self.trajectories):

            self.calculateTimesteps(trajectory)
            continue

        self.current_step += 1
        return

    def updateTFmRNA(self, increase, trajectory: int):

        if increase:
            self.concentration_tf_mrna[trajectory, (self.current_step + 1)] += 1
            return

        self.concentration_tf_mrna[trajectory, (self.current_step + 1)] -= 1
        return

    def updateTF(self, increase, trajectory: int):

        if increase:
            self.concentration_tf[trajectory, (self.current_step + 1)] += 1
            return

        self.concentration_tf[trajectory, (self.current_step + 1)] -= 1
        return

    def updateMiRNA(self, increase, trajectory):

        if increase:
            self.concentration_mi_rna[trajectory, (self.current_step + 1)] += 1
            return

        self.concentration_mi_rna[trajectory, (self.current_step + 1)] -= 1
        return

    def updateTRNA(self, increase, trajectory):

        if increase:
            self.concentration_t_rna[trajectory, (self.current_step + 1)] += 1
            return

        self.concentration_t_rna[trajectory, (self.current_step + 1)] -= 1
        return

    def updateT(self, increase, trajectory):

        if increase:
            self.concentration_t[trajectory, (self.current_step + 1)] += 1
            return

        self.concentration_t[trajectory, (self.current_step + 1)] -= 1
        return

    def updateComplex(self, increase, trajectory):

        if increase:
            self.concentration_complex[trajectory, (self.current_step + 1)] += 1
            self.concentration_mi_rna[trajectory, (self.current_step + 1)] -= 1
            self.concentration_t_rna[trajectory, (self.current_step + 1)] -= 1
            return

        self.concentration_complex[trajectory, (self.current_step + 1)] -= 1
        self.concentration_mi_rna[trajectory, (self.current_step + 1)] += 1
        return

    # ------------------------------------------
    # Utilities

    def verifyParameters(self):
        return

    def duplicateAllValues(self):
        """
        Does add the values to the arrays in general,
        when something happens the values will be overwrittten. simpler than if statements
        """
        self.timestamps = np.hstack(
            (self.timestamps, self.timestamps[:, -1].reshape(-1, 1).copy())
        )
        self.concentration_tf_mrna = np.hstack(
            (
                self.concentration_tf_mrna,
                self.concentration_tf_mrna[:, -1].reshape(-1, 1).copy(),
            )
        )
        self.concentration_tf = np.hstack(
            (self.concentration_tf, self.concentration_tf[:, -1].reshape(-1, 1).copy())
        )
        self.concentration_t_rna = np.hstack(
            (
                self.concentration_t_rna,
                self.concentration_t_rna[:, -1].reshape(-1, 1).copy(),
            )
        )
        self.concentration_t = np.hstack(
            (self.concentration_t, self.concentration_t[:, -1].reshape(-1, 1).copy())
        )
        self.concentration_mi_rna = np.hstack(
            (
                self.concentration_mi_rna,
                self.concentration_mi_rna[:, -1].reshape(-1, 1).copy(),
            )
        )
        self.concentration_complex = np.hstack(
            (
                self.concentration_complex,
                self.concentration_complex[:, -1].reshape(-1, 1).copy(),
            )
        )

        self.events = np.hstack((self.events, self.events[:, -1].reshape(-1, 1).copy()))

    def calculateTimesteps(self, trajectory):
        """
        Evaluates Partition Function then decides which concentration to update
        """
        r = self.evaluatePartitionFunction(trajectory)

        time = 1 * r * np.log(1 / np.random.random())
        self.timestamps[trajectory, self.current_step + 1] += time

        name, increase, err = self.determineEvent(r)
        self.events[trajectory, self.current_step] = name
        if err:
            return

        if name == 0:
            self.updateTFmRNA(increase, trajectory)

        if name == 1:
            self.updateTF(increase, trajectory)

        if name == 2:
            self.updateTRNA(increase, trajectory)

        if name == 3:
            self.updateT(increase, trajectory)

        if name == 4:
            self.updateMiRNA(increase, trajectory)

        if name == 5:
            self.updateComplex(increase, trajectory)

    def determineEvent(self, r):
        """
        I do it with one random number to limit proccessing
        """
        count = 0
        upper_bound = 0
        increase = False
        rand_float = np.random.random()

        boundaries = [
            (self.tf_rna_increase, 0),
            (self.tf_rna_part, 0),
            (self.tf_increase, 1),
            (self.tf_part, 1),
            (self.t_rna_increase, 2),
            (self.t_rna_part, 2),
            (self.t_increase, 3),
            (self.t_part, 3),
            (self.mi_rna_increase, 4),
            (self.mi_rna_part, 4),
            (self.complex_increase, 5),
            (self.complex_part, 5),
        ]

        for boundary, name in boundaries:

            increase = not increase  # alternate
            upper_bound += boundary * r  # increase boundary

            if not increase:
                upper_bound -= (
                    boundaries[count - 1][0] * r
                )  # subtract the probabillity for increase as its contained in the partition

            if (
                rand_float < upper_bound
            ):  # no need to explicitly check for the lower bound, as it has already been tested

                return (
                    name,
                    increase,
                    False,
                )  # I discarded the errorhandling later, now i just try again. it may be that
                # the total < 1 thus it doesnt produce an result, presumably due to float precision

            count += 1
            continue

        return self.determineEvent(r)

    def evaluatePartitionFunction(self, trajectory):
        """
        Get the Rates for increase and increase+decrease for each concentration and evaluate the total Partition function.

        GENERALLY STRUCTURE IT!!!
        """
        step = self.current_step
        q = self.concentration_tf[trajectory, step]

        self.tf_increase = (
            self.mu_t * self.concentration_tf_mrna[trajectory, step]
        )  # increase reaction
        self.tf_part = self.mu_q * q  # partition function for this

        self.tf_rna_increase = self.alpha_t
        self.tf_rna_part = (
            self.alpha_t + self.concentration_tf_mrna[trajectory, step] * self.mu_t
        )

        self.mi_rna_increase = (
            self.alpha_s * q / (q + self.k_s)
            + self.mu_c * self.concentration_complex[trajectory, step]
        )
        self.mi_rna_part = (
            self.mi_rna_increase
            + self.mu_s * self.concentration_mi_rna[trajectory, step]
        )

        self.t_rna_increase = self.alpha_r * q / (q + self.k_r)
        self.t_rna_part = (
            self.t_rna_increase + self.mu_r * self.concentration_t_rna[trajectory, step]
        )

        self.t_increase = self.pi_h * self.concentration_t_rna[trajectory, step]
        self.t_part = (
            self.t_increase + self.mu_h * self.concentration_t[trajectory, step]
        )

        self.complex_increase = (
            self.beta
            * self.concentration_t_rna[trajectory, step]
            * self.concentration_mi_rna[trajectory, step]
        )
        self.complex_part = (
            self.complex_increase
            + self.mu_c * self.concentration_complex[trajectory, step]
        )

        inv_r = (
            self.tf_part
            + self.tf_rna_part
            + self.mi_rna_part
            + self.t_rna_part
            + self.t_part
            + self.complex_part
        )

        return 1 / inv_r

    def seedRandGen(self, seed_val: int):
        np.random.seed(seed_val)

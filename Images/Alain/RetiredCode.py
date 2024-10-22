# Set the random number seed for reproducibility
np.random.seed(1)

# Set reaction rates 
rf = 0.1        # Forward reaction rate
rb = 1.0        # Backwards reaction rate

# Set meta-parameters
steps = 100          # Number of reactions per trajectory
trajectories = 100  # Number of trajectories to simulate

# Set up data arrays
T = np.zeros((trajectories, steps+1))
N_A = np.zeros((trajectories, steps+1))
N_B = np.zeros((trajectories, steps+1))
N_AB = np.zeros((trajectories, steps+1))

# Set initial conditions
T[:,0] = 0 # for completeness
N_A[:,0] = 10
N_B[:,0] = 30
N_AB[:,0] = 0

# Run simulation
for i in range(trajectories):
    for j in range(steps):
        # Calculate current total reaction rate
        R = rf * N_A[i,j] * N_B[i,j] + rb * N_AB[i,j]
        
        # Calculate and store time to next reaction
        u = np.random.random()
        t = 1/R * np.log(1/u)
        T[i, j+1] = T[i,j] + t
        
        # Select next reaction
        pf = rf * N_A[i,j] * N_B[i,j] / R # probability of forward reaction
        u = np.random.random()
        
        # Apply the reaction
        if u < pf:
            # selected forward reaction
            N_A[i,j+1] = N_A[i,j] - 1
            N_B[i,j+1] = N_B[i,j] - 1
            N_AB[i,j+1] = N_AB[i,j] + 1
        else:
            # selected backward reaction
            N_A[i,j+1] = N_A[i,j] + 1
            N_B[i,j+1] = N_B[i,j] + 1
            N_AB[i,j+1] = N_AB[i,j] - 1


# Plot the simulated trajectories for each molecule type
fig, axs = plt.subplots(3, 1, figsize=(10,20))

molecule_type = ['A', 'B', "AB"]
for i in range(3):
    axs[i].set_title(f'Number of {molecule_type[i]} molecules')
    axs[i].set_xlabel("Time (hours)")
    axs[i].set_ylabel("Counts")
    
# Plot each simulated trajectory
for i in range(trajectories):
    axs[0].plot(T[i,:], N_A[i,:], marker='', color='grey', linewidth=0.6, alpha=0.3)
    axs[1].plot(T[i,:], N_B[i,:], marker='', color='grey', linewidth=0.6, alpha=0.3)
    axs[2].plot(T[i,:], N_AB[i,:], marker='', color='grey', linewidth=0.6, alpha=0.3)

plt.show()

# Let's also plot a few simulations
n2plot = 3
is2plot = np.random.choice(list(range(trajectories)), size=n2plot, replace=False)
fig, axs = plt.subplots(n2plot, 1, figsize=(10,20))

for i in range(n2plot):
    axs[i].set_title(f'Number of {molecule_type[i]} molecules')
    axs[i].set_xlabel("Time (hours)")
    axs[i].set_ylabel("Counts")
    axs[i].plot(T[i,:], N_A[i,:], marker='', color='red', linewidth=2.0, alpha=0.3)
    axs[i].plot(T[i,:], N_B[i,:], marker='', color='blue', linewidth=2.0, alpha=0.3)
    axs[i].plot(T[i,:], N_AB[i,:], marker='', color='black', linewidth=2.0, alpha=0.3)
    axs[i].legend(molecule_type)
plt.show()




        chance = self.tf_part * r
        #print((self.t_part+self.complex_part+self.mi_rna_part+self.t_rna_part+self.tf_rna_part+self.tf_part)*r)
        if rand_float >= chance:
            #print(u > (self.tf_increase/self.tf_part), u , self.tf_increase/self.tf_part)
            self.updateTF(u < (self.tf_increase/self.tf_part), trajectory)
            return
        
        chance += self.tf_rna_part*r

        if rand_float >= chance:
            
            self.updateTFmRNA(u < (self.tf_rna_increase/self.tf_rna_part), trajectory)
            return

        chance += self.mi_rna_part*r
        
        if rand_float >= chance:

            self.updateMiRNA(u < (self.mi_rna_increase/self.mi_rna_part), trajectory)
            return
        
        chance += self.t_rna_part*r
        
        if rand_float >= chance:

            self.updateTRNA(u < (self.t_rna_increase/self.t_rna_part), trajectory)
            return
        
        chance += self.t_part*r
        
        if rand_float >= chance:

            self.updateT(u < (self.t_increase/self.t_part), trajectory)
        
        self.updateComplex(u < (self.complex_increase/self.complex_part), trajectory)
        return
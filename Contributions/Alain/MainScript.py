# Reactions:
# A + B -> AB
# AB -> A + B

# Molecular counts
# N_A
# N_B
# N_AB

# Reaction rates
# rf : reaction rate for A + B -> AB
# rb : reaction rate for AB -> A + B

# Import supporting packages
import numpy as np
import matplotlib.pyplot as plt
from DataStructModule import DataStruct
from PlotStructModule import PlotStruct
#%matplotlib inline

def MainProcess(                
    tf_transcription_rate,
    tf_translation_rate,
    decay_rate_tf_mrna,
    decay_rate_tf_protein,
    decay_rate_mirna,
    beta,
    complex_dissociation_rate):

    #Do Shit

    return 



if __name__ == "__main__":

    #----------------------------------------------------
    #process_parameters(*sys.argv[1:]) #for feeding in the parameters from the forms app, idkbut idk

    struct = DataStruct(2)
    struct.seedRandGen(2)

    for i in range(30000):
        struct.update()
    
    plot = PlotStruct(struct)
    plot.createPlotRandTraject(2)


    #-------------------------------------------------
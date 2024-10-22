For The Gillespie Simulation. Seperate in classes so parts can be changed independantly, DO NOT CHANGE THE DATA-STRUCTURE ONCE DECIDED UPON. It should be expandable without restructuring.

TODO
* Put the data in a pandas array (the Rows can be named and it is not static compared to the numpy array)
* Implement the Matrix Multiplication to calculate the partition function (R) -> Nora
* Implement the random select function from a module
* Think about ways to test and Implement tests
* Implement the second plot shown in the script
* Think about how to input the parameters ()
    * Write save/ read functions for config files (yaml, json whatever)
* Reduce repetition in how the concentrations are updated

Less Important
* Think about the interface - tkinter works but is tedious
    * Write Reusable elements for the interface 
    * Think of a way to properly connect the elements that allows signals to be propelled
      throughout the "tree"
    * Work out the threading
* Limit the Input Values to be sensible
    * Determine what sensible parameters are

Features (maybe idk, just ideas)
* Save data as .csv,.h5 or smth
* allow the simmulation to run cuntinously until User-Input interrupt and continuusly plot.
    * Allow to modify Parameters while Running


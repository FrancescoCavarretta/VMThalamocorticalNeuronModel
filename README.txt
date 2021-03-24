 This model entry contains the NEURON code for:

Bichler EK, Cavarretta F, Jaeger D (2021) Changes in Excitability Properties of Ventromedial Motor Thalamic Neurons in 6-OHDA Lesioned Mice. eNeuro 8(1): ENEURO.0436-20.2021. doi: 10.1523/ENEURO.0436-20.2021.

Requirements:
NEURON v. 7.7+
Python v. 3.7+ with SciPy, NumPy, PyNWB, and MatPlotLib


To run:

1. Compile the mod files by typing:

nrnivmodl

2. Generate the simulated data (ie, run the simulations):

nrniv -python sag_sim.py 
nrniv -python rebound_sim.py 
nrniv -python fi_curve_sim.py

Alternatively, you may execute the command replacing "nrniv -python" with "python" or "python3".

3. Visualize the data (ie, reproduce Figure 6 in Bichler et al, 2021):
python fig_vis.py

Do not hesitate to contact me via email for additional information:
francesco.cavarretta@emory.edu or francescocavarretta@hotmail.it



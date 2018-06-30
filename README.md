# regression_band_structure

Code performs linear regression on simulated band structure data for MoS2. For effective mass calculations,
we use a quadratic (parabolic) fit (degree = 2) for our data. This is example where knowledge of the behavior 
of the dispersion relation in the vicinity of the conduction band minimum  guides us to choose a quadratic fit. 
Even though a higher degree polynomial fit, e.g. degree = 4 produces a better accuracy (higher R-squared value), 
it leads to overfitting of the data.

c_band.csv: conduction band data for MoS2 crysal calculated using quantum espresso software package.
analysis.py: code to perform parabolic fit of the simulated band structure data

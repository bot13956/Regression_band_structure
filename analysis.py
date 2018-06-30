
"""
Created on Fri Jun 29 20:52:35 2018

Code performs linear regression on simulated band structure data for MoS2. For effective mass calculations,
we use a quadratic (parabolic) fit (degree = 2) for our data. This is example where knowledge of the behavior 
of the dispersion relation in the vicinity of the conduction band minimum  guides us to choose a quadratic fit. 
Even though a higher degree polynomial fit, e.g. degree = 4 produces a better accuracy (higher R-squared value), 
it leads to overfitting of the model.

@author: Benjamin O. Tayo
"""
#import necessary libraries
import pylab
import pandas as pd

#import conduction band data: x = crystal momentum; y = energy
data=pd.read_csv('c_band.csv')

#select x values in the vicinity of the conduction band minimum
data=data[(data.x >0.82) & (data.x<1.0)]


#perform polynomial fit using pylab
Xvals=data.x
Yvals=data.y
degree = 2
model=pylab.polyfit(Xvals,Yvals,degree)
estY=pylab.polyval(model,Xvals)

#calculating R-squared value
R2 = 1 - ((Yvals-estY)**2).sum()/((Yvals-Yvals.mean())**2).sum()

#plot of observed and modeled data
pylab.scatter(Xvals,Yvals, c='b', label='observed')
pylab.plot(Xvals,estY, c='r', label='predicted:' + ' R2' '='+ ' ' + str(round(R2,4)))
pylab.xlabel('k (A/Bohr)')
pylab.ylabel('E (eV)')
pylab.xticks(pylab.arange(0.8, 1.05, 0.05))
pylab.legend()
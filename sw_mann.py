import math
import numpy
import scipy.optimize as op
import matplotlib.pyplot as plt
import os
import pdb

def solwind(x):
	return (x**2.0) - (2.0*numpy.log(x)) - rhs	

def solwind_deriv(x):
	return (2.0*x) - 2.0*(1.0/x)	

def sw_mann(r):
	global rhs
	T = 1.4e6
	G = 6.671e-11
	kB = 1.3807e-23
	mp = 1.6726e-27
	ms = 1.99e30	
	rs = 6.958e8
	mu = 0.6
	C = 6.3*(10.0**34.0)

	delta = 0.0
	delta = delta*(math.pi/180.0)

	vc = numpy.sqrt(  (kB*T)/(mu*mp) )
	rc = (G*ms)/(2.0*(vc**2.0))

	for i in numpy.arange(len(r)):
		r[i]= r[i]*rs
	
	v = numpy.zeros(len(r))
	n = numpy.zeros(len(r))
	va = numpy.zeros(len(r))
	vms = numpy.zeros(len(r))
	
	
	for i in numpy.arange(len(r)):
		br = 2.20*((rs/r[i])**3.0)* numpy.sqrt(1.0 + 3.0*numpy.sin(delta)**2.0)
		rhs = 4.0*numpy.log(r[i]/rc)+4.0*(rc/r[i]) - 3.0
		v[i] = op.fsolve(solwind, r[i]/rc, fprime=solwind_deriv) * vc
		n[i] = C/ (v[i] * r[i]**2 * 100.0**3.0)
		va[i] = br / numpy.sqrt(4.0*math.pi*n[i]*(mp*1000.0))/100.0
		vms[i] = numpy.sqrt(vc**2+va[i]**2)
	

	for i in numpy.arange(len(r)):
		r[i]= r[i]/rs
		v[i] = v[i]/1000.0
		va[i] = va[i]/1000.0
		vms[i] = vms[i]/1000.0
	
	#pdb.set_trace()
	plt.plot(r,v)
	plt.xlabel('Heliocentric Distance (R/R$_{\odot}$)', fontsize=14)
	plt.ylabel('Solar Wind Velocity (km s$^{-1}$)', fontsize=14)
	plt.grid(True)
	plt.show()


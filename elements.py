import numpy as np
import random
from particle import Particle

class Argon:
	__kB = 1.3806 * 10 ** (-23) #Boltzman constant
	__m = 39.95


	def __init__(self, N):
		self.particles = []
		self.N = N
		a = 1
		b0 = [a , 0 , 0]
		b1 = [a/2, (a*np.sqrt(3))/2, 0]
		b2 = [a/2, (a*np.sqrt(3))/6, (a*np.sqrt(2./3))]
		
		h = (N -1)/2 #help variable
		
		for i0 in range(N):
			for i1 in range(N):
				for i2 in range(N):
					r = np.dot(i0 - h, b0) + np.dot(i1 - h, b1) + np.dot(i2 - h, b2)
					self.particles.append(Particle("Ar",r[0],r[1],r[2]))

	def MakeMomentum(self, T0):
		E_sum = 0 # sum of energy
		for par in self.particles:
			par.addMomentum(maxwell=True)
			E_sum += par.px + par.py + par.pz
		#Renormalize to get E = 0.5*kb*T 
		norm_factor = (0.5 * self.__kB * T0) / E_sum #normalization factor
		#Calculate momentum from enegy and apply norm_factor

		for par in self.particles:
			par.addMomentum(
				random.choice([-1,1])*np.sqrt(2*self.__m*par.px * norm_factor), 
				random.choice([-1,1])*np.sqrt(2*self.__m*par.py * norm_factor), 
				random.choice([-1,1])*np.sqrt(2*self.__m*par.pz * norm_factor)
				)
		#Remowe momvement in all axis
		sum_px = 0 
		sum_py = 0
		sum_pz = 0
		for par in self.particles: #calculate movement
			sum_px += par.px
			sum_py += par.py
			sum_pz += par.pz
		for par in self.particles: #apply correction
			par.addMomentum(
				par.px - sum_px/self.N,
				par.py - sum_py/self.N,
				par.pz - sum_pz/self.N
			)
			
import numpy as np
import random
from particle import Particle
import input as inp

class Argon:
	__kB = 8.31 * 10 ** (-3) #Boltzman constant
	__m = 39.95 #argon atomic mass


	def __init__(self, N, a):
		self.particles = []
		self.N = N
		b0 = [a , 0 , 0]
		b1 = [a/2, (a*np.sqrt(3))/2, 0]
		b2 = [a/2, (a*np.sqrt(3))/6, (a*np.sqrt(2./3))]
		
		h = (N -1)/2 #help variable
		
		for i0 in range(N):
			for i1 in range(N):
				for i2 in range(N):
					r = np.dot(i0 - h, b0) + np.dot(i1 - h, b1) + np.dot(i2 - h, b2)
					self.particles.append(Particle("Ar",r))

	def MakeMomentum(self, T0):
		E_sum = 0 # sum of energy
		for par in self.particles:
			par.setMomentum(maxwell=True)
			E_sum += par.px + par.py + par.pz
		#Renormalize to get E = 0.5*kb*T 
		norm_factor = (0.5 * self.__kB * T0) / E_sum #normalization factor
		#Calculate momentum from enegy and apply norm_factor

		for par in self.particles:
			par.setMomentum([
				random.choice([-1,1])*np.sqrt(2*self.__m*par.px * norm_factor), 
				random.choice([-1,1])*np.sqrt(2*self.__m*par.py * norm_factor), 
				random.choice([-1,1])*np.sqrt(2*self.__m*par.pz * norm_factor)
			])
		#Remowe momvement in all axis
		sum_px = 0 
		sum_py = 0
		sum_pz = 0
		for par in self.particles: #calculate movement
			sum_px += par.px
			sum_py += par.py
			sum_pz += par.pz
		for par in self.particles: #apply correction
			par.setMomentum([
				par.px - sum_px/self.N**3,
				par.py - sum_py/self.N**3,
				par.pz - sum_pz/self.N**3
			])

	def CalculatePressure(self, L , f):
		p = 0
		for par in self.particles:
			r = np.linalg.norm(par.r())
			if r >= L:
				p += np.linalg.norm(np.dot((f*(L -r))/(r),par.r()))
		return p

	def CalculateTemperature(self):
		T = 0
		for par in self.particles:
			T += np.linalg.norm(par.p())**2
		T = T * 2/(3*self.N*self.__kB*2*self.__m)
		return T

	def MakeForces(self, L, f, R):	 #this should be changed variable to __init__
		#remove olf forces
		for par in self.particles:
			par.setForce([0,0,0])
		#add van der Waales force  
		ep = 1	#!!!! to input !!!!
		rest = self.particles.copy()
		for i_par in self.particles:
			rest.remove(i_par)
			for j_par in rest:
				r_ij = np.subtract(i_par.r(),j_par.r())
				r_norm = np.linalg.norm(r_ij)
				i_par.setForce(np.add(i_par.F(),  np.dot(12*ep*((R/r_norm)**12-(R/r_norm)**6)/r_norm**2,r_ij)))
				j_par.setForce(np.add(j_par.F(), np.dot(-12*ep*((R/r_norm)**12-(R/r_norm)**6)/r_norm**2,r_ij)))

		#add virtual vessel
		for par in self.particles:
			r = np.linalg.norm(par.r())
			if r >= L:
				par.setForce(np.add(par.F(),np.dot(f*(L-r)/(r),par.r())))

	def Simulate(self, tau):
		for par in self.particles:
			par.setMomentum(np.add(par.p(),np.dot(0.5*tau,par.F())))
			par.setPosition(np.add(par.r(),np.dot(tau/self.__m,par.p())))
		self.MakeForces(inp.L, inp.f, inp.R) #this should be changed 	variable from self
		for par in self.particles:
			par.setMomentum(np.add(par.p(),np.dot(0.5*tau,par.F())))
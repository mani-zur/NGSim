#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log
import random

class Particle:
	def __init__(self, element , x = 0, y = 0, z = 0):
		self.elem = element
		self.x = x
		self.y = y
		self.z = z
		self.setForce([0,0,0])
	
	def r(self):
		return [self.x, self.y, self.z]

		
	def setMomentum(self, PX = 0, PY = 0, PZ = 0, maxwell = False):
		if maxwell:
			self.px= log(random.uniform(0,1))
			self.py= log(random.uniform(0,1))
			self.pz= log(random.uniform(0,1))
		else :
			self.px= PX
			self.py= PY
			self.pz= PZ
	
	def setForce(self, force):
		self.Fx = force[0]
		self.Fy = force[1]
		self.Fz = force[2]

	def F(self):
		return [self.Fx, self.Fy, self.Fz]
		
	def __str__ (self):
		return self.elem + " " + str(self.x) + " " + str(self.y) + " " + str(self.z) + "\n"
		
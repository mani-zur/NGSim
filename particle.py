#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log
import random

class Particle:
	def __init__(self, element , r):
		self.elem = element
		self.x = r[0]
		self.y = r[1]
		self.z = r[2]
		self.setForce([0,0,0])
	
	def r(self):
		return [self.x, self.y, self.z]
	
	def p(self):
		return [self.px, self.py, self.pz]

	def F(self):
		return [self.Fx, self.Fy, self.Fz]

	def setPosition(self, r):
		self.x = r[0]
		self.y = r[1]
		self.z = r[2]

		
	def setMomentum(self, momentum = [0,0,0], maxwell = False):
		if maxwell:
			self.px= log(random.uniform(0,1))
			self.py= log(random.uniform(0,1))
			self.pz= log(random.uniform(0,1))
		else :
			self.px= momentum[0]
			self.py= momentum[1]
			self.pz= momentum[2]
	
	def setForce(self, force):
		self.Fx = force[0]
		self.Fy = force[1]
		self.Fz = force[2]
		
	def __str__ (self):
		return self.elem + " " + str(self.x) + " " + str(self.y) + " " + str(self.z) + "\n"
		
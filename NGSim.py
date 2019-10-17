#!/usr/bin/env python
# -*- coding: utf-8 -*-

import input as inp
from elements import Argon
import time

def main():
	start = time.time()
	cristal = Argon(inp.x, inp.a)	
	#File making
	file = open("out.xyz", "w")
	file.write(str(inp.x**3)+ "\n")
	file.write("\n")
	file.write(str(cristal))

	cristal.MakeMomentum(inp.T_0)
	cristal.MakeForces(inp.L, inp.f, inp.R)
	for i in range(1000):
		#print(cristal.CalculateTemperature(), cristal.CalculatePressure(inp.L, inp.f))
		cristal.Simulate(inp.tau)
		file.write(str(inp.x**3)+ "\n")
		file.write("\n")
		file.write(str(cristal))
	file.close()
	end = time.time()
	print(end - start)
		


if __name__ == "__main__":
	main()

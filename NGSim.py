#!/usr/bin/env python
# -*- coding: utf-8 -*-

import input as inp
from elements import Argon

def main():
	cristal = Argon(inp.x)	
	#File making
	file = open("out.xyz", "w")
	file.write(str(inp.x**3)+ "\n")
	file.write("\n")

	cristal.MakeMomentum(273)
		


if __name__ == "__main__":
	main()

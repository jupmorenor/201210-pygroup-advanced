# -*- coding: UTF-8 -*-
#
#		intro.py
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
'''
Created on 10/07/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''
import pygame
from funcionesBasicas import Funciones as funciones

class Intro():
	"""Introduccion al juego, muestra los logotipos de la universidad y de Pygroup.
	Importa y ejecuta el menu principal.
	Esta es la clase que inicia la ejecucion del programa.
	"""
	
	def __init__(self):
		pygame.init()
		self.ventana = pygame.display.set_mode(funciones.VENTANA)
		self.imagen_fondoA = funciones.cargarImagen("imagenes/escudo_UD.png")
		self.imagen_fondoB = funciones.cargarImagen("imagenes/Pygroup_Logo.jpg")
		self.tiempo = 400
		self.juego = None
		
	def introduccion(self):
		pygame.init()
		pygame.display.set_caption("UDTanks 2.0")
		reloj = pygame.time.Clock()
		
		while True:
			self.tiempo-=1
			
			if self.tiempo > 200:
				self.ventana.blit(self.imagen_fondoA, (0,0))
			elif self.tiempo > 0 and self.tiempo <= 200:
				self.ventana.blit(self.imagen_fondoB, (0,0))
			else:
				try:
					import menu
					self.juego = menu.Menu_UDTanks(self.ventana)
					self.juego.mainMenu()
				except(ImportError):
					print("No se encuentra el juego")
					return 0

			pygame.display.update()
			reloj.tick(60)
		return 0
			
if __name__ == '__main__':
	jugar = Intro()
	jugar.introduccion()
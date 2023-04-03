# -*- coding: UTF-8 -*-
#
#		puntajes.py
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
Created on 8/07/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''
import pygame
from funcionesBasicas import Funciones as funciones

class Puntajes():
	
	def __init__(self, pantalla):
		self.ventana = pantalla
		self.imagen_fondo = funciones.cargarImagen("imagenes/puntajes.jpg")
		self.musica_fondo = "sonido/EXTEND SKY.ogg"
		self.color_texto=[255,255,255]
		self.puntajes = []
		
	def cargarPuntajes(self):
		try:
			puntajes = open("puntajes.pyfile", 'r')
			lista = puntajes.readlines()
			puntajes.close()
		except(IOError):	
			lista = "NO SE ENCONTRARON PUNTAJES REGISTRADOS".split()
		return lista
		
	def mainPuntajes(self):
		funciones.cargarMusica(self.musica_fondo)
		pygame.mixer.music.play(-1)
		
		self.puntajes = self.cargarPuntajes()
		
		while True:
			
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN:
					pygame.mixer.music.stop()
					return 0
				
			self.ventana.blit(self.imagen_fondo, (0,0))
			
			for i in range(1, len(self.puntajes)+1):
				imagen, rect = funciones.dibujarTexto(self.puntajes[i-1].expandtabs(),
													 funciones.VENTANA[0]/2, 
													 (funciones.VENTANA[1]/20) * i, 
													 self.color_texto)
				self.ventana.blit(imagen, rect)
			
			pygame.display.update()
		return 0
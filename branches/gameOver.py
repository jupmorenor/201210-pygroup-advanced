# -*- coding: UTF-8 -*-
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
Created on 27/06/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''
import pygame
from generales import Generales
from random import randint

class GameOver():
	
	def __init__(self, ventana):
		self.funciones = Generales()
		self.ventana = ventana  #pygame.display.set_mode(self.funciones.VENTANA) 
		self.imagen = randint(1,3)
		self.imagen_fondo = self.funciones.cargar_imagen("imagenes/game over "+str(self.imagen)+".jpg")#final con imagen aleatoria
		self.musica_fondo = "sonido/PUPPET OF THE MAGUS.ogg"
		self.alpha = 0
		self.imagen_fondo.set_alpha(self.alpha)
		
	def blit_alpha(self, ventana, imagen, ubicacion, opacidad):
    """Metodo que controla la transparencia del fade-in"""
		x = ubicacion[0]
		y = ubicacion[1]
		temp = pygame.Surface((imagen.get_width(), imagen.get_height())).convert()
		temp.blit(ventana, (-x, -y))
		temp.blit(imagen, (0,0))
		temp.set_alpha(opacidad)
		ventana.blit(temp, ubicacion)
		
	def mainGameOver(self):
		self.funciones.cargar_musica(self.musica_fondo)
		pygame.mixer.music.play(-1)
		
		while True:
			
			if self.alpha<=255:
				self.alpha+=0.05
				self.blit_alpha(self.ventana, self.imagen_fondo, (0,0), int(self.alpha))
			
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN:
					pygame.mixer.music.stop()
					return 0
			
			pygame.display.update()
			
		return 0 
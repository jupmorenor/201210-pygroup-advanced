# -*- coding: UTF-8 -*-
#
#		creditos.py
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
Created on 26/06/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''
import pygame
from funcionesBasicas import Funciones as funciones

class Creditos():
	
	def __init__(self, ventana):
		self.ventana = ventana
		self.imagen_fondo = funciones.cargarImagen("imagenes/creditos.jpg")
		self.musica_fondo = "sonido/SELAGINELLA.ogg"
		self.color_texto = [255,255,255]
		self.linea1_img, self.linea1_rect = funciones.dibujarTexto("JUEGO DESARROLLADO COMO PROYECTO DE", 400, 216, self.color_texto)
		self.linea2_img, self.linea2_rect = funciones.dibujarTexto("EL GRUPO DE TRABAJO PYGROUP", 400, 232, self.color_texto)
		self.linea3_img, self.linea3_rect = funciones.dibujarTexto("POR:", 400, 248, self.color_texto)
		self.linea4_img, self.linea4_rect = funciones.dibujarTexto("JUAN PABLO MORENO RICO     2011102059", 400, 264, self.color_texto)
		self.linea5_img, self.linea5_rect = funciones.dibujarTexto("ALEJANDRO DUARTE     20092020120", 400, 280, self.color_texto)
		self.linea6_img, self.linea6_rect = funciones.dibujarTexto("Musica por THE CROW'S CLAW", 400, 312, self.color_texto)
		self.linea7_img, self.linea7_rect = funciones.dibujarTexto("Imagenes tomadas de Internet de varios sitios", 400, 328, self.color_texto)
		self.linea8_img, self.linea8_rect = funciones.dibujarTexto("AGRADECEMOS EL INCENTIVAR ESTAS ACTIVIDADES", 400, 360, self.color_texto)
		
	def mainCreditos(self):
		funciones.cargarMusica(self.musica_fondo)
		pygame.mixer.music.play(-1)

		while True:
			
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN:
					pygame.mixer.music.stop()
					return 0
					
			self.ventana.blit(self.imagen_fondo, (0,0))
			self.ventana.blit(self.linea1_img, self.linea1_rect)
			self.ventana.blit(self.linea2_img, self.linea2_rect)
			self.ventana.blit(self.linea3_img, self.linea3_rect)
			self.ventana.blit(self.linea4_img, self.linea4_rect)
			self.ventana.blit(self.linea5_img, self.linea5_rect)
			self.ventana.blit(self.linea6_img, self.linea6_rect)
			self.ventana.blit(self.linea7_img, self.linea7_rect)
			self.ventana.blit(self.linea8_img, self.linea8_rect)
			pygame.display.update()
		return 0
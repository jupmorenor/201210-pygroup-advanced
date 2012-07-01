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
Created on 30/06/2012
@author: Juanpa y Yami
'''
import pygame
import sys
from generales import Generales
from nivel_1 import Nivel1
from objetos import Cursor, Boton

class UDTanks():
	
	def __init__(self):
		pygame.init()
		self.funciones = Generales()
		self.ventana = pygame.display.set_mode(self.funciones.VENTANA)
		self.imagen_fondo = self.funciones.cargar_imagen("imagenes/menu.jpg")
		self.musica_fondo = "sonido/TWIN CRESCENT.ogg"
		self.empezar = Boton(self.funciones.cargar_imagen("imagenes/boton1.png"),200,100)#boton para nivel 1
		self.continuar = Boton(self.funciones.cargar_imagen("imagenes/boton2.png"),200,150)#boton Cargar jugador Guardado
		self.puntajes = Boton(self.funciones.cargar_imagen("imagenes/boton3.png"),200,200)#boton ver puntajes
		self.creditos = Boton(self.funciones.cargar_imagen("imagenes/boton4.png"),200,250)#boton ver creditos
		self.salir = Boton(self.funciones.cargar_imagen("imagenes/boton5.png"),200,300)#boton salir 
		self.cursor = Cursor()
		
	def ejecutar(self):
		pygame.init()
		pygame.display.set_caption("UDTanks") 
		self.funciones.cargar_musica(self.musica_fondo)
		pygame.mixer.music.play(-1)
		
		
		while True:
			
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT or evento.type == pygame.K_ESCAPE:
					pygame.mixer.music.stop()
					pygame.quit()
					sys.exit()
				elif evento.type == pygame.MOUSEBUTTONDOWN:
					if self.cursor.colliderect(self.empezar):
						pygame.mixer.music.stop()
						nivelEnEjecucion = Nivel1(self.ventana)
						nivelEnEjecucion.mainNivel1() # ejecuta el nivel 1
						self.funciones.cargar_musica(self.musica_fondo)
						pygame.mixer.music.play(-1)
					elif self.cursor.colliderect(self.continuar):
						pygame.mixer.music.stop()
						nivelEnEjecucion = Nivel1(self.ventana)
						nivelEnEjecucion.cargarDatos("Tanque 1")# carga los datos guardados
						nivelEnEjecucion.mainNivel1()
						self.funciones.cargar_musica(self.musica_fondo)
						pygame.mixer.music.play(-1)
					elif self.cursor.colliderect(self.puntajes):
						#pygame.mixer.music.stop()
						pass#por implementar
						#self.funciones.cargar_musica(self.musica_fondo)
						#pygame.mixer.music.play(-1)
					elif self.cursor.colliderect(self.creditos):
						pygame.mixer.music.stop()
						from creditos import Creditos
						nivelEnEjecucion2 = Creditos(self.ventana)
						nivelEnEjecucion2.mainCreditos() # abre la ventana de creditos
						self.funciones.cargar_musica(self.musica_fondo)
						pygame.mixer.music.play(-1)
					elif self.cursor.colliderect(self.salir):
						pygame.mixer.music.stop()
						pygame.quit()
						sys.exit()
			
			self.cursor.actualizar()
			self.ventana.blit(self.imagen_fondo, (0,0))
			self.ventana.blit(self.empezar.imagen, self.empezar.rect)
			self.ventana.blit(self.continuar.imagen, self.continuar.rect)
			self.ventana.blit(self.puntajes.imagen, self.puntajes.rect)
			self.ventana.blit(self.creditos.imagen, self.creditos.rect)
			self.ventana.blit(self.salir.imagen, self.salir.rect)
			pygame.display.update()
		return 0
	
if __name__ == '__main__':
	juego = UDTanks()
	juego.ejecutar()
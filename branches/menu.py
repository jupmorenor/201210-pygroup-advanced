# -*- coding: UTF-8 -*-
#
#		menu.py
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
Created on 30/06/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''
import sys
import pygame
from funcionesBasicas import Funciones as funciones
from objetos import Cursor, Boton

class Menu_UDTanks():
	"""Menu principal del juego, tiene 5 botones y un sonido en reproduccion
	"""
	
	def __init__(self, pantalla):
		self.ventana = pantalla
		self.imagen_fondo = funciones.cargarImagen("imagenes/menu.jpg")
		self.musica_fondo = "sonido/TWIN CRESCENT.ogg"
		self.empezar = Boton(funciones.cargarImagen("imagenes/boton1.png"),125,450)#boton para nivel 1
		self.continuar = Boton(funciones.cargarImagen("imagenes/boton2.png"),325,450)#boton Cargar jugador Guardado
		self.puntajes = Boton(funciones.cargarImagen("imagenes/boton3.png"),525,450)#boton ver puntajes
		self.creditos = Boton(funciones.cargarImagen("imagenes/boton4.png"),225,500)#boton ver creditos
		self.salir = Boton(funciones.cargarImagen("imagenes/boton5.png"),425,500)#boton salir 
		self.cursor = Cursor()
		self.nivelEnEjecucion = None
		
	def mainMenu(self): 
		funciones.cargarMusica(self.musica_fondo)
		pygame.mixer.music.play(-1)
		reloj = pygame.time.Clock()
		
		while True:
			
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT or evento.type == pygame.K_ESCAPE:
					pygame.mixer.music.stop()
					pygame.quit()
					sys.exit()
				elif evento.type == pygame.MOUSEBUTTONDOWN:
					if self.cursor.colliderect(self.empezar):
						try: 
							import nivel_1
							nombre = funciones.ingresarUsuario()
							self.nivelEnEjecucion = nivel_1.Nivel1(self.ventana, nombre)
							pygame.mixer.music.stop()
							self.nivelEnEjecucion.mainNivel1() # ejecuta el nivel 1
							self.nivelEnEjecucion = None
							del(nivel_1)
							funciones.cargarMusica(self.musica_fondo)
							pygame.mixer.music.play(-1)
						except(ImportError):
							print("No se encuentra el módulo correspondeinte")
							
					elif self.cursor.colliderect(self.continuar):
						try:
							import nivel_1
							nombre = funciones.ingresarUsuario() 
							self.nivelEnEjecucion = nivel_1.Nivel1(self.ventana, nombre)
							self.nivelEnEjecucion.cargarDatos(nombre)# carga los datos guardados
							pygame.mixer.music.stop()
							self.nivelEnEjecucion.mainNivel1()
							self.nivelEnEjecucion = None
							del(nivel_1)
							funciones.cargarMusica(self.musica_fondo)
							pygame.mixer.music.play(-1)	
						except(ImportError):
							print("No se encuentra el módulo correspondeinte")
									
					elif self.cursor.colliderect(self.puntajes):
						try:
							import puntajes
							self.nivelEnEjecucion = puntajes.Puntajes(self.ventana)
							pygame.mixer.music.stop()
							self.nivelEnEjecucion.mainPuntajes() # muestra la ventana de puntajes
							self.nivelEnEjecucion = None
							del(puntajes)
							funciones.cargarMusica(self.musica_fondo)
							pygame.mixer.music.play(-1)
						except(ImportError):
							print("No se encuentra el módulo correspondeinte")
					
					elif self.cursor.colliderect(self.creditos):
						try:
							import creditos
							self.nivelEnEjecucion = creditos.Creditos(self.ventana)
							pygame.mixer.music.stop()
							self.nivelEnEjecucion.mainCreditos() # abre la ventana de creditos
							self.nivelEnEjecucion = None
							del(creditos)
							funciones.cargarMusica(self.musica_fondo)
							pygame.mixer.music.play(-1)
						except(ImportError):
							print("No se encuentra el módulo correspondeinte")
						
					elif self.cursor.colliderect(self.salir):
						pygame.mixer.music.stop()
						pygame.quit() # cierra el juego
						sys.exit()
			
			self.cursor.actualizar()
			self.ventana.blit(self.imagen_fondo, (0,0))
			self.ventana.blit(self.empezar.imagen, self.empezar.rect)
			self.ventana.blit(self.continuar.imagen, self.continuar.rect)
			self.ventana.blit(self.puntajes.imagen, self.puntajes.rect)
			self.ventana.blit(self.creditos.imagen, self.creditos.rect)
			self.ventana.blit(self.salir.imagen, self.salir.rect)
			pygame.display.update()
			reloj.tick(60)
		return 0
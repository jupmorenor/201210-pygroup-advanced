# -*- coding: UTF-8 -*-
#
#		funciones.py
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
Created on 10/05/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''

import pygame 
from tkinter import Tk, Entry, Button, StringVar
from math import degrees, radians, sin, cos, atan2

class Funciones():
	'''
	Constantes y metodos estaticos para el uso general del programa.
	Tales como:
		cargarImagen
		cargarSonido
		cargarMusica
		dibujarTexto
		agregarImagen
		direccionPunto
		vectorEnX
		vectorEnY
	'''
	
	#Constantes para el ancho y alto de la ventana
	VENTANA = (ANCHO, ALTO) = (800, 600)
		
	@classmethod
	def ingresarUsuario(cls):
		
		cls.nombre=""
		
		def salir():
			root.quit()
	
		def cargarArchivo():
			cls.nombre=a.get()
			root.destroy()
	
		def obtenerN():
			n=a.get()
			return (n)
		
		root = Tk()
		root.title('CargarDatos')
		a = StringVar()
		atxt = Entry(root, textvariable=a,width=20)
		cargar = Button(root, text="Cargar Archivo", command=cargarArchivo,width=15)
		salirB= Button(root, text ="Salir", command=root.destroy, width=10)
		atxt.grid(row=0, column=0)
		cargar.grid(row=1, column=0)
		salirB.grid(row=1,column=1)
		root.mainloop()
		return (obtenerN())
	
	#Funciones para uso general de cualquier objeto
	@classmethod
	def cargarImagen(cls, archivo):
		"""
		Crea un objeto que contiene la imagen dada, si la imagen no se encuentra, 
		el programa no puede iniciar.
		"""
		try: 
			imagen = pygame.image.load(archivo).convert_alpha()
		except(pygame.error): #en caso de error
			print("No se pudo cargar la imagen: ", archivo)
			pygame.quit()
			raise(SystemExit)
		return imagen
		
	@classmethod
	def cargarSonido(cls, archivo):
		"""Crea un objeto a partir del archivo de efecto de sonido dado"""
		try:
			sonido = pygame.mixer.Sound(archivo)
		except(pygame.error):
			print("No se pudo cargar el sonido: ", archivo)
			sonido = None
		return sonido
	
	@classmethod
	def cargarMusica(cls, archivo):
		"""Carga en el mixer el archivo de musica dado para su reproduccion"""
		try: 
			pygame.mixer.music.load(archivo)
		except(pygame.error):
			print("No se pudo cargar la cancion: ", archivo)
	
	@classmethod	
	def dibujarTexto(cls, texto, posx, posy, color):
		"""
		Genera dado un texto y una posicion, una imagen para dibujar en pantalla 
		y su respectivo rectangulo contenedor.
		"""
		fuente = pygame.font.Font("DroidSans.ttf", 20)
		salida = pygame.font.Font.render(fuente, texto, 1, color)
		salida_rect = salida.get_rect()
		salida_rect.centerx = posx
		salida_rect.centery = posy
		return salida, salida_rect
	
	@classmethod
	def agregarImagen(cls, ruta, ancho, alto):
		"""Corta las subimagenes de una plantilla de imagenes para animar"""
		subimagenes = []
		imagen_completa = cls.cargarImagen(ruta)
		ancho_total, alto_total = imagen_completa.get_size()
		for i in range(int(alto_total / alto)):
			for j in range(int(ancho_total / ancho)):
				subimagenes.append(imagen_completa.subsurface(pygame.Rect(j * ancho, i * alto, ancho, alto)))
		return subimagenes
	
	@classmethod
	def direccionPunto(cls, x, y, x2_y2,):
		"""Devuelve la direccion en grados que hay hacia un punto"""
		x2, y2 = x2_y2
		dist_x = x2 - x
		dist_y = y2 - y
		direccion = -1 * degrees(atan2(dist_y, dist_x))
		return direccion
	
	@classmethod	
	def vectorEnX(cls, dist, ang):
		"""Devuelve el componente x de un vector"""
		return cos(radians(ang)) * dist
	
	@classmethod
	def vectorEnY(cls, dist, ang):
		"""Devuelve el componente y de un vector"""
		return sin(radians(ang)) * -dist

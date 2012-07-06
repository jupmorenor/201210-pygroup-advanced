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
from tkinter import *
from pygame.locals import *
from math import degrees, radians, sin, cos, atan2

class Generales():

	"""Constantes para uso general de cualquier objeto"""
	def __init__(self):
		self.VENTANA=self.ANCHO,self.ALTO=800,600
		
	def leerDatos(self):
		self.nombre=""
		def salir():
			root.quit()
	
		def cargarArchivo():
			self.nombre=a.get()
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
	
	"""Funciones para uso general de cualquier objeto"""
	def cargar_imagen(self, ruta):
		"""funcion para cargar imagenes"""
		try: imagen=pygame.image.load(ruta).convert_alpha()
		except(pygame.error): #en caso de error
			print("No se pudo cargar la imagen: ", ruta)
			raise(SystemExit)
		return imagen
		
	def cargar_sonido(self, ruta):
		"""Funcion para cargar sonidos"""
		try:sonido=pygame.mixer.Sound(ruta)
		except(pygame.error):
			print("No se pudo cargar el sonido: ", ruta)
			sonido=None
		return sonido
	
	def cargar_musica(self, ruta):
		"""Funcion para cargar musica"""
		try: pygame.mixer.music.load(ruta)
		except(pygame.error):
			print("No se pudo cargar la cancion: ", ruta)
		
	def texto(self, texto, posx, posy, color):
		"""Funcion para escritura de texto"""
		fuente = pygame.font.Font("DroidSans.ttf", 20)
		salida = pygame.font.Font.render(fuente, texto, 1, color)
		salida_rect = salida.get_rect()
		salida_rect.centerx = posx
		salida_rect.centery = posy
		return salida, salida_rect
	
	def agregar_imagen(self, ruta, largo, alto):
		"""Funcion para cortar las subimagenes de una imagen animada"""
		subimagenes = []
		imagen_completa = self.cargar_imagen(ruta)
		ancho_total, altura_total = imagen_completa.get_size()
		for i in range(int(ancho_total/largo)):
			subimagenes.append(imagen_completa.subsurface((i*largo,0,largo,alto)))
		return subimagenes
	
	def direccion_punto(self, x,y,x2_y2,):
		"""Funcion que devuelve la direccion que hay hacia un punto"""
		x2, y2 = x2_y2
		dist_x = x2-x
		dist_y = y2-y
		direccion=-1*degrees(atan2(dist_y,dist_x))
		return direccion
		
	def vector_en_x(self, length, dirr):
		"""Devuelve el componente x de un vector"""
		x_dist=cos(radians(dirr)) * length
		return x_dist
	
	def vector_en_y(self, length, dirr):
		"""Devuelve el componente y de un vector"""
		y_dist=sin(radians(dirr)) * -length
		return y_dist

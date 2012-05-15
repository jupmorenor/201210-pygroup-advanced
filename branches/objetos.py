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
import pygame, sys, random
from pygame.locals import *
from generales import *
# ----------------------------------------------
# Clases
# ----------------------------------------------
class Base_de_Tanque(pygame.sprite.Sprite):
	"""Objeto tanque del primer nivel"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = Generales.cargar_imagen("ruta")#por definir
		self.postimagen = self.preimagen
		self.rectangulo = self.preimagen.get_rect()
		self.rectangulo.center = [400, 400]
		self.velocidad = 5
		
	def actualizar(self, evento):
		if evento.key==K_ESCAPE:
			pygame.quit()
			sys.exit(0)
		if evento.key==K_UP:
			self.rectangulo.centery-=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,90)
		if evento.key==K_DOWN:
			self.rectangulo.centery+=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,270)
		if evento.key==K_LEFT:
			self.rectangulo.centerx-=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,180)
		if evento.key==K_RIGHT:
			self.rectangulo.centerx+=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,0)
		self.rectangulo = [min(max(self.rectangulo.centerx,-8),Generales.VENTANA[0]-32), min(max(self.rectangulo.centery,-8),Generales.VENTANA[1]-32)]
		
class Rotor_de_Tanque(pygame.sprite.Sprite):
	"""Objeto tanque del primer nivel"""
	def __init__(self, ruta_img, ruta_snd):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = Generales.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rectangulo = self.preimagen.get_rect()
		self.disparo = Generales.cargar_sonido(ruta_snd)
		self.balas_disparadas=[]
		
	def actualizar(self, mouse, ventana, baseTanque):
		self.angulo = Generales.direccion_punto(self.rectangulo.centerx, self.rectangulo.centery, mouse)
		self.postimagen = pygame.transform.rotate(self.preimagen, self.angulo)
		self.rectangulo.center = baseTanque.rectangulo.center
		ventana.blit(self.postimagen, self.rectangulo)
		
	def disparar(self, boton_mouse):
		if boton_mouse:
			bala = Bala(self.rectangulo, self.angulo)
			self.disparo.play()
			self.balas_disparadas.append(bala)
		
class Enemigo_Tanque(Rotor_de_Tanque):
	"""Objeto enemigo del primer nivel"""
	def __init__(self, ruta_img, ruta_snd):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = Generales.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rectangulo = self.preimagen.get_rect()
		self.disparo = Generales.cargar_sonido(ruta_snd)
		self.balas_disparadas=[]
		self.velocidad = 2
	
	def actualizar(self, direccion):
		self.angulo = Generales.direccion_punto(self.rectangulo.centerx, self.rectangulo.centery, direccion)
		self.postimagen = pygame.transform.rotate(self.preimagen, self.angulo)
		self.rectangulo.centerx+=Generales.vector_en_x(self.velocidad, self.angulo)
		self.rectangulo.centery+=Generales.vector_en_y(self.velocidad, self.angulo)
      
  def disparar(self):
		bala = Bala(self.rectangulo, self.angulo)
		self.balas_disparadas.append(bala)
    #falta definir la forma en que el tanque enemigo dispara
		pass
	
class Bala(pygame.sprite.Sprite):
	"""Objeto bala general para todos los objetosq ue disparan"""
	def __init__(self, ruta_img, posicion_inicial, angulo):
		pygame.sprite.Sprite.__init__(self)
		self.angulo = angulo
		self.imagen = pygame.transform.rotate(Generales.cargar_imagen(ruta_img), self.angulo)
		self.rectangulo = self.imagen.get_rect()
		self.velocidad = 4
		self.rectangulo.center = posicion_inicial
		
	def actualizar(self):
		self.rectangulo.centerx+=Generales.vector_en_x(self.velocidad, self.angulo)
		self.rectangulo.centery+=Generales.vector_en_y(self.velocidad, self.angulo)
		if self.rectangulo.centerx > Generales.VENTANA[0] or self.rectangulo.centerx < 0 or self.rectangulo.centery > Generales.VENTANA[1] or self.rectangulo.centery < 0:
			self.kill()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
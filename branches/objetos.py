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
Created on 10/05/2012
@author: Juan Pablo Moreno y Alejandro Duarte
'''
import pygame, sys, random
from pygame.locals import *
from generales import *

funciones = Generales()

# ----------------------------------------------
# Clases
# ----------------------------------------------
class Jugador_Control():
	"""objeto controlador del momento del juego"""
	def __init__(self):
		"""definicion de algunas variables de tipo general"""
		self.puntajeTotal = 0
		self.color_texto=[0,0,0]
		self.puntajeNivel = 0
		self.nivel = 0
		self.vida = 100
		self.balasPorDisparar = 20
		self.tiempo = 6000
		
	def actualizar1(self, ventana):
		"""dibujado en pantalla del texto"""
		self.puntos_img, self.puntos_rect = funciones.texto("Puntos: " +str(self.puntajeNivel), 64, 16, self.color_texto)
		self.vidas_img, self.vidas_rect = funciones.texto("Vida: " +str(self.vida), 64, 32, self.color_texto)
		self.balas_img, self.balas_rect = funciones.texto("Balas: " + str(self.balasPorDisparar), 64, 48, self.color_texto)
		self.tiempo_img, self.tiempo_rect = funciones.texto("Tiempo: " + str(int(self.tiempo/100)), 64, 64, self.color_texto)
		ventana.blit(self.puntos_img, self.puntos_rect)
		ventana.blit(self.vidas_img, self.vidas_rect)
		ventana.blit(self.balas_img, self.balas_rect)
		ventana.blit(self.tiempo_img, self.tiempo_rect)
		
class Base_de_Tanque(pygame.sprite.Sprite):
	"""Objeto tanque del primer nivel"""
	def __init__(self, ruta_img):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = funciones.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rect = self.preimagen.get_rect()
		self.posicion=[100,100]
		self.rect.center = self.posicion
		self.velocidad = 5
			
	def actualizar(self, evento):
		if evento.key==K_ESCAPE:
			pygame.quit()
			sys.exit()
		if evento.key==K_UP:
			self.posicion[1]-=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,90)
		if evento.key==K_DOWN:
			self.posicion[1]+=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,270)
		if evento.key==K_LEFT:
			self.posicion[0]-=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,180)
		if evento.key==K_RIGHT:
			self.posicion[0]+=self.velocidad
			self.postimagen=pygame.transform.rotate(self.preimagen,0)
		self.posicion=[min(max(self.posicion[0],0),funciones.VENTANA[0]), min(max(self.posicion[1],0),funciones.VENTANA[1])]
		self.rect.center = self.posicion
		
class Rotor_de_Tanque(pygame.sprite.Sprite, Jugador_Control):
	"""Objeto tanque del primer nivel"""
	def __init__(self, ruta_img, ruta_snd):
		pygame.sprite.Sprite.__init__(self)
		Jugador_Control.__init__(self)
		self.preimagen = funciones.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rect = self.preimagen.get_rect()
		self.disparo = funciones.cargar_sonido(ruta_snd)
		self.balas_disparadas=[]
		
	def actualizar(self, mouse, ventana, baseTanque):
		self.angulo = funciones.direccion_punto(self.rect.centerx, self.rect.centery, mouse)
		self.postimagen = pygame.transform.rotate(self.preimagen, self.angulo)
		self.rect = self.postimagen.get_rect()
		self.rect.center = baseTanque
		ventana.blit(self.postimagen, self.rect)
		
	def disparar(self, boton_mouse):
		"""dispara una bala"""
		if boton_mouse:
			if self.balasPorDisparar>0:
				bala = Bala("imagenes/nivel 1/bala.png", self.rect.center, self.angulo)
				self.disparo.play()
				self.balas_disparadas.append(bala)
				self.balasPorDisparar-=1
				
	def dibujar_Balas(self, ventana):
		for i in range(len(self.balas_disparadas)):
			if self.balas_disparadas[i].actualizar(ventana):
				self.balas_disparadas.pop(i)
				break
		
class Enemigo_Tanque(pygame.sprite.Sprite):
	"""Objeto enemigo del primer nivel"""
	def __init__(self, x, y, ruta_img, ruta_snd):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = funciones.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rect = self.preimagen.get_rect()
		self.posicion = [x,y]
		self.rect.center = self.posicion
		self.disparo = funciones.cargar_sonido(ruta_snd)
		self.velocidad = 0.5
		self.frecuencia = random.randrange(250,500)
		self.alarma = self.frecuencia
		self.objeto = random.randrange(1,7)
		self.balas_disparadas=[]
	
	def actualizar(self, direccion):
		self.angulo = funciones.direccion_punto(self.rect.centerx, self.rect.centery, direccion)
		self.postimagen = pygame.transform.rotate(self.preimagen, self.angulo)
		self.rect = self.postimagen.get_rect()
		self.posicion[0]+=funciones.vector_en_x(self.velocidad, self.angulo)
		self.posicion[1]+=funciones.vector_en_y(self.velocidad, self.angulo)
		self.rect.center = self.posicion
		self.alarma-=1
		
	def disparar(self):
		if self.alarma<=0:
			bala = Bala("imagenes/nivel 1/bala.png", self.rect.center, self.angulo)
			self.balas_disparadas.append(bala)
			self.disparo.play()
			self.frecuencia -= 50
			if self.frecuencia<=50: self.frecuencia=500
			self.alarma = self.frecuencia

	def dibujar_Balas(self, ventana):
		for i in range(len(self.balas_disparadas)):
			if self.balas_disparadas[i].actualizar(ventana):
				self.balas_disparadas.pop(i)
				break
			
	def darBonus(self):
		bonus = random.randint(1,20)
		if bonus>=5: bonus=0
		if bonus!=0: objBonus=Objeto_Bonus(self.rect.center, bonus)
		else: objBonus=None
		return objBonus
	
	def destruir(self, ob):
		if self.rect.colliderect(ob):
			pass
		return Explosion(self.rect.center)
				
class Bala(pygame.sprite.Sprite):
	"""Objeto bala general para todos los objetos que disparan"""
	def __init__(self, ruta_img, posicion_inicial, angulo):
		pygame.sprite.Sprite.__init__(self)
		self.angulo = angulo
		self.imagen = pygame.transform.rotate(funciones.cargar_imagen(ruta_img), self.angulo)
		self.rect = self.imagen.get_rect()
		self.velocidad = 4
		self.rect.center = posicion_inicial
		
	def actualizar(self, ventana):
		self.rect.centerx+=funciones.vector_en_x(self.velocidad, self.angulo)
		self.rect.centery+=funciones.vector_en_y(self.velocidad, self.angulo)
		ventana.blit(self.imagen, self.rect)
		if self.rect.centerx > funciones.VENTANA[0] or self.rect.centerx < 0 or self.rect.centery > funciones.VENTANA[1] or self.rect.centery < 0:
			return True	

class Explosion(pygame.sprite.Sprite):
	"""Objeto que representa la explosion de otro objeto"""
	def __init__(self, posicion):
		pygame.sprite.Sprite.__init__(self)
		self.imagenes = funciones.agregar_imagen("imagenes/nivel 1/explosion.png", 192, 192)
		self.rect = self.imagenes[0].get_rect()
		self.rect.center = posicion
		self.subimagen = 0
		
	def actualizar(self, ventana):
		ventana.blit(self.imagenes[int(self.subimagen)], self.rect)
		self.subimagen += 0.2
		if self.subimagen >= len(self.imagenes)-1:
			return True

class Objeto_Bonus(pygame.sprite.Sprite):
	"""Objeto recogible por el jugador"""
	def __init__(self, pos, tp):
		pygame.sprite.Sprite.__init__(self)
		self.tipo=tp
		self.tipos={1:"vida", 2:"balas", 3:"tiempo", 4:"bomba"}
		if tp<= len(self.tipos):
			self.imagen = funciones.cargar_imagen("imagenes/nivel 1/"+self.tipos[tp]+".png")
			self.rect = self.imagen.get_rect()
			self.rect.center = pos

	def actualizar(self, ventana, otro):
		ventana.blit(self.imagen, self.rect)
		return self.rect.colliderect(otro)
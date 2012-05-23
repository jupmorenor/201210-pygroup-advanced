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
		self.puntajeTotal = 0
		self.color_texto=[0,0,0]
    self.puntajeNivel=0
    self.nivel=0
    self.vida=100
    self.balas=0
    self.tiempo=0
  def cambiarVida(self, cambioV):
    self.vida+=self.vida+cambioV
    return self.vida
  def cambiarBalas(self, cambioB):
    return self.balas=self.balas+cambioB
    
  def verificarCambiarNivel(self, puntaje, tiempoT, vidaT, balasT):
    cambiarNivel=False 
    if self.puntajeNivel==100:
      self.puntajeTotal=self.puntajeTotal+bonusTiempo(tiempoT)+bonusVida(vidaT)+bonusBalas(balasT)
      cambiarNivel=True
    return cambiarNivel
  def cambiarNivel(self, verificar):
    """Instrucciones para cambiar de nivel"""
    
  def bonusTiempo(self, tiempoT):
    """instrucciones para dar bonus de tiempo"""
    return bonusT
  def bonusVidas(self, vidaT):
    """Instrucciones para bonus vidas"""
    return bonusV
  def bonusbalas(self, balasT):
    """Instrucciones para bonus de cantidad de balas"""
    return bonusB
    
		
	def actualizar(self, vidas, balas, ventana):
		self.puntos_img, self.puntos_rect = funciones.texto("Puntos: " +str(self.puntaje), 64, 16, self.color_texto)
		self.vidas_img, self.vidas_rect = funciones.texto("Vidas: " +str(vidas), 64, 32, self.color_texto)
		self.balas_img, self.balas_rect = funciones.texto("Balas: " + str(balas), 64, 48, self.color_texto)
		ventana.blit(self.puntos_img, self.puntos_rect)
		ventana.blit(self.vidas_img, self.vidas_rect)
		ventana.blit(self.balas_img, self.balas_rect)

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
		self.vidas = 5
		
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
			self.postimagen=pygame.transform.rotatSe corrige la forma en que se actualizan las balase(self.preimagen,0)
		self.rect.center = [min(max(self.posicion[0],0),funciones.VENTANA[0]), min(max(self.posicion[1],0),funciones.VENTANA[1])]
		
class Rotor_de_Tanque(pygame.sprite.Sprite):
	"""Objeto tanque del primer nivel"""
	def __init__(self, ruta_img, ruta_snd):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = funciones.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rect = self.preimagen.get_rect()
		self.disparo = funciones.cargar_sonido(ruta_snd)
		self.balas_porDisparar = 20
		self.balas_disparadas=[]
		
	def actualizar(self, mouse, ventana, baseTanque):
		self.angulo = funciones.direccion_punto(self.rect.centerx, self.rect.centery, mouse)
		self.postimagen = pygame.transform.rotate(self.preimagen, self.angulo)
		self.rect = self.postimagen.get_rect()
		self.rect.center = baseTanque
		ventana.blit(self.postimagen, self.rect)
		
	def disparar(self, boton_mouse):
		if boton_mouse:
			if self.balas_porDisparar>0:
				bala = Bala("imagenes/nivel 1/bala.png", self.rect.center, self.angulo)
				#self.disparo.play()
				self.balas_disparadas.append(bala)
				self.balas_porDisparar-=1
		
class Enemigo_Tanque(pygame.sprite.Sprite):
	"""Objeto enemigo del primer nivel"""
	def __init__(self, ruta_img, ruta_snd):
		pygame.sprite.Sprite.__init__(self)
		self.preimagen = funciones.cargar_imagen(ruta_img)
		self.postimagen = self.preimagen
		self.rect = self.preimagen.get_rect()
		self.disparo = funciones.cargar_sonido(ruta_snd)
		self.velocidad = 2
		self.balas_disparadas=[]
	
	def actualizar(self, direccion):
		self.angulo = funciones.direccion_punto(self.rect.centerx, self.rect.centery, direccion)
		self.postimagen = pygame.transform.rotate(self.preimagen, self.angulo)
		self.rect.centerx+=funciones.vector_en_x(self.velocidad, self.angulo)
		self.rect.centery+=funciones.vector_en_y(self.velocidad, self.angulo)
		
	def disparar(self):
		bala = Bala(self.rect, self.angulo)
		self.balas_disparadas.append(bala)
		#falta definir la forma en que el tanque enemigo dispara
		pass
	
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
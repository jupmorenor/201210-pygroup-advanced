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
from pygame.locals import *
from generales import Generales
from objetos import *

class Nivel1():
	"""Escena numero 1 del juego"""
	def __init__(self, pantalla, nombre):
		self.funciones = Generales()
		self.ventana = pantalla #pygame.display.set_mode(self.funciones.VENTANA)
		self.imagen_fondo = self.funciones.cargar_imagen("imagenes/nivel 1/fondo_Nv_1.png")
		self.musica_fondo = "sonido/CROSSFIRE BARRAGE.ogg"
		self.base_tanque = Base_de_Tanque("imagenes/nivel 1/tanque_base_Nv_1.png")
		self.rotor_tanque = Rotor_de_Tanque("imagenes/nivel 1/tanque_rotor_Nv_1.png", "sonido/Explosion01.ogg", nombre)
		self.pos_mouse = []
		self.bot_mouse = 0
		self.enemigos = []
		self.bonuscreado=[]
		self.explosiones = []
		self.alarma = 1
		self.salir =False
		
	def controlEnemigos(self):
		self.alarma -= 0.1
		if self.alarma<=0:
			xrandom = random.randint(0,funciones.VENTANA[0])
			yrandom = random.randint(0,funciones.VENTANA[1])
			if not (xrandom>0 and xrandom<funciones.VENTANA[0])and(yrandom>0 and yrandom<funciones.VENTANA[1]):
				enemigo=Enemigo_Tanque(xrandom, yrandom, "imagenes/nivel 1/tanque_enemigo_Nv_1.png", "sonido/Explosion01.ogg")
				self.enemigos.append(enemigo)
				self.alarma=1
		
	def actualizarEnemigos(self):	
		for i in range(len(self.enemigos)):
			self.enemigos[i].actualizar(self.base_tanque.posicion)
			self.enemigos[i].disparar()
			self.ventana.blit(self.enemigos[i].postimagen, self.enemigos[i].rect)
			if self.enemigos[i].dibujar_Balas(self.ventana, self.base_tanque.rect):
				self.rotor_tanque.vida-=20
			
		
	def controlExplosiones(self):
		for i in range(len(self.explosiones)):
			if self.explosiones[i].actualizar(self.ventana):
				self.explosiones.pop(i)
				break
			
	def controlBonuses(self):
		bonus=None
		for i in range(len(self.bonuscreado)):
			if self.bonuscreado[i]==None:
				self.bonuscreado.pop(i)
				break
			elif self.bonuscreado[i].actualizar(self.ventana, self.base_tanque.rect):
				bonus=self.bonuscreado.pop(i)
				break
		if bonus!=None:
			if bonus.tipo==1:
				self.rotor_tanque.vida+=10
			elif bonus.tipo==2:
				self.rotor_tanque.balasPorDisparar+=5
			elif bonus.tipo==3:
				self.rotor_tanque.tiempo+=500
			elif bonus.tipo==4:
				j=0
				for j in range(len(self.enemigos)):
					if(j!=0):
						j=0
					self.rotor_tanque.puntajeNivel+=len(self.enemigos)
					self.bonuscreado.append(self.enemigos[j].darBonus())
					sale=self.enemigos.pop(j)
					explosion=Explosion(sale.rect.center)
					self.explosiones.append(explosion)

	def controlColisiones(self):
		for i in range(len(self.rotor_tanque.balas_disparadas)):
			for j in range(len(self.enemigos)):
				if self.enemigos[j].rect.colliderect(self.rotor_tanque.balas_disparadas[i].rect):
					self.bonuscreado.append(self.enemigos[j].darBonus())
					sale=self.enemigos.pop(j)
					self.rotor_tanque.balas_disparadas.pop(i)
					explosion=Explosion(sale.rect.center)
					self.explosiones.append(explosion)
					self.rotor_tanque.puntajeNivel+=1
					break
			break
		
	def guardarDatos(self, nombre):
		nombreJ = nombre + ".txt"
		try: archivo = open(nombreJ, "w")
		except(IOError):
			print("No hay datos registrados con ese nombre")
		vidaJ = self.rotor_tanque.vida
		tiempoJ = self.rotor_tanque.tiempo
		balasJ = self.rotor_tanque.balasPorDisparar
		puntajeJ = self.rotor_tanque.puntajeNivel
		archivo.write(str(vidaJ)+"\n")
		archivo.write(str(tiempoJ)+"\n")
		archivo.write(str(balasJ)+"\n")
		archivo.write(str(puntajeJ)+"\n")
		archivo.close
		
	def cargarDatos(self, nombre):
		nombreJ = nombre + ".txt"
		try:
			archivo = open(nombreJ)
			lis = archivo.readlines()
			self.rotor_tanque.vida = int(lis[0])
			self.rotor_tanque.tiempo = int(lis[1])
			self.rotor_tanque.balasPorDisparar = int(lis[2])
		except(IOError):
			print("No hay datos registrados con ese nombre")
				
	def terminarJuego(self):
		if self.rotor_tanque.vida <= 0 or self.rotor_tanque.tiempo<=0:
			pygame.mixer.music.stop()
			from gameOver import GameOver
			terminar = GameOver(self.ventana)
			terminar.mainGameOver()
			return True
		else:
			return False
				
	def mainNivel1(self):
		reloj=pygame.time.Clock()
		pygame.key.set_repeat(1,25)
		self.funciones.cargar_musica(self.musica_fondo)
		pygame.mixer.music.play(-1)
		
		while True:
			self.pos_mouse = pygame.mouse.get_pos()
			self.bot_mouse = pygame.mouse.get_pressed()
			self.rotor_tanque.tiempo-=1
			self.salir = self.terminarJuego()
			if self.salir == True:
				return 0
			
			#Seccion de actualizacion de eventos
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT or evento.type == pygame.K_ESCAPE:
					pygame.mixer.music.stop()
					self.guardarDatos(self.rotor_tanque.nombreJugador)
					return 0
				elif evento.type == pygame.KEYDOWN:
					self.base_tanque.actualizar(evento)
				if evento.type == pygame.MOUSEBUTTONDOWN:
					self.rotor_tanque.disparar(self.bot_mouse)
			#Seccion de dibujo
			self.ventana.blit(self.imagen_fondo, (0,0))
			self.ventana.blit(self.base_tanque.postimagen, self.base_tanque.rect)
			self.rotor_tanque.actualizar(self.pos_mouse, self.ventana, self.base_tanque.rect.center)
			
			self.controlBonuses()
			self.controlEnemigos()
			self.actualizarEnemigos()
			self.controlExplosiones()
			self.controlColisiones()
			
			self.rotor_tanque.dibujar_Balas(self.ventana)
			self.rotor_tanque.actualizar1(self.ventana)
			pygame.display.update()
			reloj.tick(30)
			
		return 0
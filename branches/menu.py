


import pygame
import interfazNivel_1


 # importo el modulo

class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)
	def update(self):
		self.left,self.top=pygame.mouse.get_pos()
class Boton(pygame.sprite.Sprite):
	def __init__(self,imagen, x, y):
		self.imagen1=imagen
		self.rect= self.imagen1.get_rect()
		self.rect.left,self.rect.top=(x,y)
 class menu():
  #funcion main
  def principal():
    pygame.init() 
       
    pantalla=pygame.display.set_mode((500,400))
    
    pygame.display.set_caption("Juego") 
    #creo un reloj para controlar los fps
    reloj1=pygame.time.Clock()
    cursor1=Cursor()
    
    boton1= Boton(pygame.image.load("boton1.png"),200,100)#boton Interfaz nivel 1
    boton2= Boton(pygame.image.load("boton2.png"),200,200)#boton Cargar jugador Guardado
    boton3= Boton(pygame.image.load("boton3.png"),200,200)#boton Salir
    boton4= Boton(pygame.image.load("boton4.png"),200,200)#boton Ver Creditos
    
    blanco=(255,255,255) 
    colorF=blanco
    
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type== pygame.MOUSEBUTTONDOWN:
            	if cursor1.colliderect(boton1.rect):
            		import interfazNivel_1
            		nivel1=interfazNivel_1.Nivel1()
            		nivel1.mainNivel1()
            		salir=True
              if cursor1.colliderect(boton2.rect):
                #aca toca hacer la sobre carga del metodo
                import interfazNivel_1
            		nivel1=interfazNivel_1.Nivel1()
            		nivel1.mainNivel1()
            		salir=True
            	if cursor1.colliderect(boton3.rect):
            		salir=True
              if cursor1.colliderect(boton4.rect):
                #ver creditos
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        cursor1.update()
        pantalla.fill(colorF)
        pantalla.blit(boton1.imagen1, boton1.rect)
        pantalla.blit(boton2.imagen1, boton2.rect)
        
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    


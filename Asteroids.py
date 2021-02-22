from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import random    
import sys 


xObstaculo = 0.0
yObstaculo = -0.9
obstaculoVivo = True

xObstaculo2 = 0.9
yObstaculo2 = 0.9
obstaculoVivo2 = True

xObstaculo3 = -0.6
yObstaculo3 = -0.6
obstaculoVivo3 = True

xObstaculo4 = 0.5
yObstaculo4 = -0.6
obstaculoVivo4 = True

xObstaculo5 = -0.6
yObstaculo5 = 0.6
obstaculoVivo5 = True

xObstaculo6 =  0.2
yObstaculo6 = -0.6
obstaculoVivo6 = True

xObstaculo7 = 0.5
yObstaculo7 = 0.7
obstaculoVivo7 = True

xObstaculo8 = -0.7
yObstaculo8 = -0.5
obstaculoVivo8 = True

xObstaculo9 = 0.0
yObstaculo9 = 0.9
obstaculoVivo9 = True

xObstaculo10 = 0.5
yObstaculo10 = 0.9
obstaculoVivo10 = True

xObstaculo11 = 0.5
yObstaculo11 = -0.9
obstaculoVivo11 = True

xObstaculo12 = -0.2
yObstaculo12 = -0.9
obstaculoVivo12 = True

xObstaculo13 = -0.3
yObstaculo13 = 0.9
obstaculoVivo13 = True

xObstaculo14 = 0.05
yObstaculo14 = -0.65
obstaculoVivo14 = True

xObstaculo15 = 0.55
yObstaculo15 = 0.8
obstaculoVivo15 = True

xObstaculo16 = -0.55
yObstaculo16 = -0.8
obstaculoVivo16 = True

xObstaculo17 = -0.55
yObstaculo17 = -0.8
obstaculoVivo17 = True

xObstaculo18 = 0.9
yObstaculo18 = -0.9
obstaculoVivo18 = True

xObstaculo19 = -0.9
yObstaculo19 = -0.9
obstaculoVivo19 = True

xObstaculo20 = -0.9
yObstaculo20 = 0.9
obstaculoVivo20 = True

rotacion = 0
direccion = 0

xCarrito = 0.0
yCarrito = -0.0

colisionando = False

angulo = 0
# el desfase es debido a que el triangulo en 0 grados voltea
# hacia arriba y no hacia la derecha
desfase = 90

velocidad = 3.5
velocidad_angular = 345

tiempo_anterior = 0

# Indicador si hay "bala" viva o no
disparando = False
xBala = 0
yBala = 0


def actualizar_bala(tiempo_delta):
    global disparando
    global xBala
    global yBala
    global anguloBala
    global velocidad
    global obstaculoVivo
    global obstaculoVivo2
    global obstaculoVivo3
    global obstaculoVivo4
    global obstaculoVivo5
    global obstaculoVivo6
    global obstaculoVivo7
    global obstaculoVivo8
    global obstaculoVivo9
    global obstaculoVivo10
    global obstaculoVivo11
    global obstaculoVivo12
    global obstaculoVivo13
    global obstaculoVivo14
    global obstaculoVivo15
    global obstaculoVivo16
    global obstaculoVivo17
    global obstaculoVivo18
    global obstaculoVivo19
    global obstaculoVivo20
    
    if disparando:
        if xBala >= 1:
            disparando = False
        elif xBala <= -1:
            disparando = False
        elif yBala >= 1:
            disparando = False
        elif yBala <= -1:
            disparando = False
        print("Disparando")
        yBala = yBala + \
            (sin((anguloBala + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
        xBala = xBala + \
            (cos((anguloBala + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
        # checar colision con obstaculo si sigue "vivo"
        if obstaculoVivo and xBala + 0.01 > xObstaculo - 0.05 and xBala - 0.01 < xObstaculo + 0.05 and yBala + 0.01 > yObstaculo - 0.05 and yBala - 0.01 < yObstaculo + 0.05:
            
            obstaculoVivo = False
            disparando = False

        if obstaculoVivo2 and xBala + 0.01 > xObstaculo2 - 0.05 and xBala - 0.01 < xObstaculo2 + 0.05 and yBala + 0.01 > yObstaculo2 - 0.05 and yBala - 0.01 < yObstaculo2 + 0.05:
            obstaculoVivo2 = False
            disparando = False
        
        if obstaculoVivo3 and xBala + 0.01 > xObstaculo3 - 0.05 and xBala - 0.01 < xObstaculo3 + 0.05 and yBala + 0.01 > yObstaculo3 - 0.05 and yBala - 0.01 < yObstaculo3 + 0.05:
            obstaculoVivo3 = False
            disparando = False
        
        if obstaculoVivo4 and xBala + 0.01 > xObstaculo4 - 0.05 and xBala - 0.01 < xObstaculo4 + 0.05 and yBala + 0.01 > yObstaculo4 - 0.05 and yBala - 0.01 < yObstaculo4 + 0.05:
            obstaculoVivo4 = False
            disparando = False
        
        if obstaculoVivo5 and xBala + 0.01 > xObstaculo5 - 0.05 and xBala - 0.01 < xObstaculo5 + 0.05 and yBala + 0.01 > yObstaculo5 - 0.05 and yBala - 0.01 < yObstaculo5 + 0.05:
            obstaculoVivo5 = False
            disparando = False
        
        if obstaculoVivo6 and xBala + 0.01 > xObstaculo6 - 0.05 and xBala - 0.01 < xObstaculo6 + 0.05 and yBala + 0.01 > yObstaculo6 - 0.05 and yBala - 0.01 < yObstaculo6 + 0.05:
            obstaculoVivo6 = False
            disparando = False
        
        if obstaculoVivo7 and xBala + 0.01 > xObstaculo7 - 0.05 and xBala - 0.01 < xObstaculo7 + 0.05 and yBala + 0.01 > yObstaculo7 - 0.05 and yBala - 0.01 < yObstaculo7 + 0.05:
            obstaculoVivo7 = False
            disparando = False
        
        if obstaculoVivo8 and xBala + 0.01 > xObstaculo8 - 0.05 and xBala - 0.01 < xObstaculo8 + 0.05 and yBala + 0.01 > yObstaculo8 - 0.05 and yBala - 0.01 < yObstaculo8 + 0.05:
            obstaculoVivo8= False
            disparando = False
        
        if obstaculoVivo9 and xBala + 0.01 > xObstaculo9 - 0.05 and xBala - 0.01 < xObstaculo9 + 0.05 and yBala + 0.01 > yObstaculo9 - 0.05 and yBala - 0.01 < yObstaculo9 + 0.05:
            obstaculoVivo9 = False
            disparando = False
        
        if obstaculoVivo10 and xBala + 0.01 > xObstaculo10 - 0.05 and xBala - 0.01 < xObstaculo10 + 0.05 and yBala + 0.01 > yObstaculo10 - 0.05 and yBala - 0.01 < yObstaculo10 + 0.05:
            obstaculoVivo10 = False
            disparando = False

        if obstaculoVivo11 and xBala + 0.01 > xObstaculo11 - 0.05 and xBala - 0.01 < xObstaculo11 + 0.05 and yBala + 0.01 > yObstaculo11 - 0.05 and yBala - 0.01 < yObstaculo11 + 0.05:
            obstaculoVivo11 = False
            disparando = False

        if obstaculoVivo12 and xBala + 0.01 > xObstaculo12 - 0.05 and xBala - 0.01 < xObstaculo12 + 0.05 and yBala + 0.01 > yObstaculo12 - 0.05 and yBala - 0.01 < yObstaculo12 + 0.05:
            obstaculoVivo12 = False
            disparando = False
        
        if obstaculoVivo13 and xBala + 0.01 > xObstaculo13 - 0.05 and xBala - 0.01 < xObstaculo13 + 0.05 and yBala + 0.01 > yObstaculo13 - 0.05 and yBala - 0.01 < yObstaculo13 + 0.05:
            obstaculoVivo13 = False
            disparando = False
        
        if obstaculoVivo14 and xBala + 0.01 > xObstaculo14 - 0.05 and xBala - 0.01 < xObstaculo14 + 0.05 and yBala + 0.01 > yObstaculo14 - 0.05 and yBala - 0.01 < yObstaculo14 + 0.05:
            obstaculoVivo14 = False
            disparando = False
        
        if obstaculoVivo15 and xBala + 0.01 > xObstaculo15 - 0.05 and xBala - 0.01 < xObstaculo15 + 0.05 and yBala + 0.01 > yObstaculo15 - 0.05 and yBala - 0.01 < yObstaculo15 + 0.05:
            obstaculoVivo15 = False
            disparando = False
        
        if obstaculoVivo16 and xBala + 0.01 > xObstaculo16 - 0.05 and xBala - 0.01 < xObstaculo16 + 0.05 and yBala + 0.01 > yObstaculo16 - 0.05 and yBala - 0.01 < yObstaculo16 + 0.05:
            obstaculoVivo16 = False
            disparando = False
        
        if obstaculoVivo17 and xBala + 0.01 > xObstaculo17 - 0.05 and xBala - 0.01 < xObstaculo17 + 0.05 and yBala + 0.01 > yObstaculo17 - 0.05 and yBala - 0.01 < yObstaculo17 + 0.05:
            obstaculoVivo17 = False
            disparando = False
        
        if obstaculoVivo18 and xBala + 0.01 > xObstaculo18 - 0.05 and xBala - 0.01 < xObstaculo18 + 0.05 and yBala + 0.01 > yObstaculo18 - 0.05 and yBala - 0.01 < yObstaculo18 + 0.05:
            obstaculoVivo18= False
            disparando = False
        
        if obstaculoVivo19 and xBala + 0.01 > xObstaculo19 - 0.05 and xBala - 0.01 < xObstaculo19 + 0.05 and yBala + 0.01 > yObstaculo19 - 0.05 and yBala - 0.01 < yObstaculo19 + 0.05:
            obstaculoVivo19 = False
            disparando = False
        
        if obstaculoVivo20 and xBala + 0.01 > xObstaculo20 - 0.05 and xBala - 0.01 < xObstaculo10 + 0.05 and yBala + 0.01 > yObstaculo20 - 0.05 and yBala - 0.01 < yObstaculo20 + 0.05:
            
            obstaculoVivo20 = False
            disparando = False
       
def checar_colisiones():
    global colisionando
    # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    # Y extremoSuperiorCarrito > extremoInferiorObstaculo
    # Y extremoInferiorCarrito < extremoSuperiorObstaculo
    if xCarrito + 0.05 > xObstaculo - 0.05 and xCarrito - 0.05 < xObstaculo + 0.05 and yCarrito + 0.05 > yObstaculo - 0.05 and yCarrito - 0.05 < yObstaculo + 0.05:
        colisionando = True
      
    elif xCarrito + 0.05 > xObstaculo2 - 0.05 and xCarrito - 0.05 < xObstaculo2 + 0.05 and yCarrito + 0.05 > yObstaculo2 - 0.05 and yCarrito - 0.05 < yObstaculo2 + 0.05:
        colisionando = True
     
    elif xCarrito + 0.05 > xObstaculo3 - 0.05 and xCarrito - 0.05 < xObstaculo3 + 0.05 and yCarrito + 0.05 > yObstaculo3 - 0.05 and yCarrito - 0.05 < yObstaculo3 + 0.05:
        colisionando = True
          
    elif xCarrito + 0.05 > xObstaculo4 - 0.05 and xCarrito - 0.05 < xObstaculo4 + 0.05 and yCarrito + 0.05 > yObstaculo4 - 0.05 and yCarrito - 0.05 < yObstaculo4 + 0.05:
        colisionando = True
         
    elif xCarrito + 0.05 > xObstaculo5 - 0.05 and xCarrito - 0.05 < xObstaculo5 + 0.05 and yCarrito + 0.05 > yObstaculo5 - 0.05 and yCarrito - 0.05 < yObstaculo5 + 0.05:
        colisionando = True
           
    elif xCarrito + 0.05 > xObstaculo5 - 0.05 and xCarrito - 0.05 < xObstaculo5 + 0.05 and yCarrito + 0.05 > yObstaculo5 - 0.05 and yCarrito - 0.05 < yObstaculo5 + 0.05:
        colisionando = True
          
    elif xCarrito + 0.05 > xObstaculo6 - 0.05 and xCarrito - 0.05 < xObstaculo6 + 0.05 and yCarrito + 0.05 > yObstaculo6 - 0.05 and yCarrito - 0.05 < yObstaculo6 + 0.05:
        colisionando = True
         
    elif xCarrito + 0.05 > xObstaculo7 - 0.05 and xCarrito - 0.05 < xObstaculo7 + 0.05 and yCarrito + 0.05 > yObstaculo7 - 0.05 and yCarrito - 0.05 < yObstaculo7 + 0.05:
        colisionando = True
          
    elif xCarrito + 0.05 > xObstaculo8 - 0.05 and xCarrito - 0.05 < xObstaculo8 + 0.05 and yCarrito + 0.05 > yObstaculo8 - 0.05 and yCarrito - 0.05 < yObstaculo8 + 0.05:
        colisionando = True
          
    elif xCarrito + 0.05 > xObstaculo9 - 0.05 and xCarrito - 0.05 < xObstaculo9 + 0.05 and yCarrito + 0.05 > yObstaculo9 - 0.05 and yCarrito - 0.05 < yObstaculo9 + 0.05:
        colisionando = True
            
    elif xCarrito + 0.05 > xObstaculo10 - 0.05 and xCarrito - 0.05 < xObstaculo10 + 0.05 and yCarrito + 0.05 > yObstaculo10 - 0.05 and yCarrito - 0.05 < yObstaculo10 + 0.05:
            colisionando = True

    elif xCarrito + 0.05 > xObstaculo11 - 0.05 and xCarrito - 0.05 < xObstaculo11 + 0.05 and yCarrito + 0.05 > yObstaculo11 - 0.05 and yCarrito - 0.05 < yObstaculo11 + 0.05:
        colisionando = True
       
    elif xCarrito + 0.05 > xObstaculo12 - 0.05 and xCarrito - 0.05 < xObstaculo12 + 0.05 and yCarrito + 0.05 > yObstaculo12 - 0.05 and yCarrito - 0.05 < yObstaculo12 + 0.05:
        colisionando = True
           
    elif xCarrito + 0.05 > xObstaculo13 - 0.05 and xCarrito - 0.05 < xObstaculo13 + 0.05 and yCarrito + 0.05 > yObstaculo13 - 0.05 and yCarrito - 0.05 < yObstaculo13 + 0.05:
        colisionando = True
          
    elif xCarrito + 0.05 > xObstaculo14 - 0.05 and xCarrito - 0.05 < xObstaculo14 + 0.05 and yCarrito + 0.05 > yObstaculo14 - 0.05 and yCarrito - 0.05 < yObstaculo14 + 0.05:
        colisionando = True
            
    elif xCarrito + 0.05 > xObstaculo15 - 0.05 and xCarrito - 0.05 < xObstaculo15 + 0.05 and yCarrito + 0.05 > yObstaculo15 - 0.05 and yCarrito - 0.05 < yObstaculo15 + 0.05:
        colisionando = True
           
    elif xCarrito + 0.05 > xObstaculo15 - 0.05 and xCarrito - 0.05 < xObstaculo15 + 0.05 and yCarrito + 0.05 > yObstaculo15 - 0.05 and yCarrito - 0.05 < yObstaculo15 + 0.05:
        colisionando = True
           
    elif xCarrito + 0.05 > xObstaculo16 - 0.05 and xCarrito - 0.05 < xObstaculo16 + 0.05 and yCarrito + 0.05 > yObstaculo16 - 0.05 and yCarrito - 0.05 < yObstaculo16 + 0.05:
        colisionando = True
           
    elif xCarrito + 0.05 > xObstaculo17 - 0.05 and xCarrito - 0.05 < xObstaculo17 + 0.05 and yCarrito + 0.05 > yObstaculo17 - 0.05 and yCarrito - 0.05 < yObstaculo17 + 0.05:
        colisionando = True
            
    elif xCarrito + 0.05 > xObstaculo18 - 0.05 and xCarrito - 0.05 < xObstaculo18 + 0.05 and yCarrito + 0.05 > yObstaculo18 - 0.05 and yCarrito - 0.05 < yObstaculo18 + 0.05:
        colisionando = True
          
    elif xCarrito + 0.05 > xObstaculo19 - 0.05 and xCarrito - 0.05 < xObstaculo19 + 0.05 and yCarrito + 0.05 > yObstaculo19 - 0.05 and yCarrito - 0.05 < yObstaculo19 + 0.05:
        colisionando = True
            
    elif xCarrito + 0.05 > xObstaculo20 - 0.05 and xCarrito - 0.05 < xObstaculo20 + 0.05 and yCarrito + 0.05 > yObstaculo20 - 0.05 and yCarrito - 0.05 < yObstaculo20 + 0.05:
        colisionando = True
    else:
        colisionando = False
    
    
        


def actualizar(window):
    global colisionando
    global tiempo_anterior
    global angulo
    global xCarrito
    global yCarrito
    global defase
    global rotacion
    global xObstaculo
    global yObstaculo
    global xObstaculo2
    global yObstaculo2
    global xObstaculo3
    global yObstaculo3
    global xObstaculo4
    global yObstaculo4
    global xObstaculo5
    global yObstaculo5
    global xObstaculo6
    global yObstaculo6
    global xObstaculo7
    global yObstaculo7
    global xObstaculo8
    global yObstaculo8
    global xObstaculo9
    global yObstaculo9
    global xObstaculo10
    global yObstaculo10
    global xObstaculo11
    global yObstaculo11
    global xObstaculo12
    global yObstaculo12
    global xObstaculo13
    global yObstaculo13
    global xObstaculo14
    global yObstaculo14
    global xObstaculo15
    global yObstaculo15
    global xObstaculo16
    global yObstaculo16
    global xObstaculo17
    global yObstaculo17
    global xObstaculo18
    global yObstaculo18
    global xObstaculo19
    global yObstaculo19
    global xObstaculo20
    global yObstaculo20


    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)


    if estadoIzquierda == glfw.PRESS:
        angulo = angulo + (velocidad_angular * tiempo_delta)
        if angulo > 360:
            angulo = 0
    if estadoDerecha == glfw.PRESS:
        angulo = angulo - (velocidad_angular * tiempo_delta)
        if angulo < 0:
            angulo = 360

    #if estadoArriba == glfw.PRESS:
     #   yCarrito = yCarrito + \
       #     (sin((angulo + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
      #  xCarrito = xCarrito + \
        #    (cos((angulo + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)

    #Cierre del juego
    if colisionando == True: 
        sys.exit()

    #Obstaculo
    

    if  yObstaculo < 0:
        yObstaculo = yObstaculo + 0.001

        if xObstaculo > 0:
            xObstaculo = xObstaculo - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo = 0.0
        yObstaculo = -0.9

    

   
    #Obstaculo2
    if xObstaculo2 > 0 or yObstaculo2 > 0:
        yObstaculo2 = yObstaculo2 - 0.001
        xObstaculo2 = xObstaculo2 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo2 = 0.9
        yObstaculo2 = 0.9

    

    #Obstaculo3
    if  yObstaculo3 < 0:
        yObstaculo3 = yObstaculo3 + 0.001

        if xObstaculo3 < 0:
            xObstaculo3 = xObstaculo3 + 0.001
    else:
        #xObstaculo2 = -1.0
        yObstaculo3 = -0.6
        xObstaculo3 = -0.6


    #Obstaculo4
    if  yObstaculo4 < 0:
        yObstaculo4 = yObstaculo4 + 0.001

        if xObstaculo4 > 0:
            xObstaculo4 = xObstaculo4 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo4 = 0.5
        yObstaculo4 = -0.6

    #Obstaculo5
    if  yObstaculo5 > 0:
        yObstaculo5 = yObstaculo5 - 0.001

        if xObstaculo5 < 0:
            xObstaculo5 = xObstaculo5 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo5 = -0.6
        yObstaculo5 = 0.6

    #Obstaculo6
    if  yObstaculo6 < 0:
        yObstaculo6 = yObstaculo6 + 0.001

        if xObstaculo6 > 0:
            xObstaculo6 = xObstaculo6 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo6 =  0.2
        yObstaculo6 = -0.6
        
    #Obstaculo7
    if  yObstaculo7 > 0:
        yObstaculo7 = yObstaculo7 - 0.001

        if xObstaculo7 > 0:
            xObstaculo7 = xObstaculo7 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo7 = 0.5
        yObstaculo7 = 0.7

    #Obstaculo8
    if  yObstaculo8 < 0:
        yObstaculo8 = yObstaculo8 + 0.001

        if xObstaculo8 < 0:
            xObstaculo8 = xObstaculo8 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo8 = -0.7
        yObstaculo8 = -0.5

    #Obstaculo9
    if  yObstaculo9 > 0:
        yObstaculo9 = yObstaculo9 - 0.001

        if xObstaculo9 > 0:
            xObstaculo9 = xObstaculo9 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo9 = 0.0
        yObstaculo9 = 0.9
    #Obstaculo10
    if  yObstaculo10 > 0:
        yObstaculo10 = yObstaculo10 - 0.001

        if xObstaculo10 > 0:
            xObstaculo10 = xObstaculo10 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo10 = 0.5
        yObstaculo10 = 0.9  
    #Obstaculo11
    
    if  yObstaculo11 < 0:
        yObstaculo11 = yObstaculo11 + 0.001

        if xObstaculo11 > 0:
            xObstaculo11 = xObstaculo11 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo11 = 0.5
        yObstaculo11 = -0.9   
   

    #Obstaculo12
    if  yObstaculo12 < 0:
        yObstaculo12 = yObstaculo12 + 0.001

        if xObstaculo12 < 0:
            xObstaculo12 = xObstaculo12 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo12 = -0.2
        yObstaculo12 = -0.9 

    #Obstaculo13
    if  yObstaculo13 > 0:
        yObstaculo13 = yObstaculo13 - 0.001

        if xObstaculo13 < 0:
            xObstaculo13 = xObstaculo13 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo13 = -0.3
        yObstaculo13 = 0.9
    #Obstaculo14
    if  yObstaculo14 > 0:
        yObstaculo14 = yObstaculo14 - 0.001

        if xObstaculo14 < 0:
            xObstaculo14 = xObstaculo14 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo14 = -0.65
        yObstaculo14 = 0.9
    #Obstaculo15
    if  yObstaculo15 > 0:
        yObstaculo15 = yObstaculo15 - 0.001

        if xObstaculo15 > 0:
            xObstaculo15 = xObstaculo15 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo15 = 0.55
        yObstaculo15 = 0.8
    #Obstaculo16
    if  yObstaculo16 < 0:
        yObstaculo16 = yObstaculo16 + 0.001

        if xObstaculo16 < 0:
            xObstaculo16 = xObstaculo16 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo16 = -0.55
        yObstaculo16 = -0.8
    #Obstaculo17
    if  yObstaculo17 < 0:
        yObstaculo17 = yObstaculo17 + 0.001

        if xObstaculo17 < 0:
            xObstaculo17 = xObstaculo17 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo17 = -0.55
        yObstaculo17 = -0.8
    #Obstaculo18
    if  yObstaculo18 < 0:
        yObstaculo18 = yObstaculo18 + 0.001

        if xObstaculo18 > 0:
            xObstaculo18 = xObstaculo18 - 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo18 = 0.9
        yObstaculo18 = -0.9
    #Obstaculo19
    if  yObstaculo19 < 0:
        yObstaculo19 = yObstaculo19 + 0.001

        if xObstaculo19 < 0:
            xObstaculo19 = xObstaculo19 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo19 = -0.9
        yObstaculo19 = -0.9
    #Obstaculo20
    if  yObstaculo20 > 0:
        yObstaculo20 = yObstaculo20 - 0.001

        if xObstaculo20 < 0:
            xObstaculo20 = xObstaculo20 + 0.001
    else:
        #xObstaculo2 = -1.0
        xObstaculo20 = -0.9 
        yObstaculo20 = 0.9
   
        

    checar_colisiones()
    actualizar_bala(tiempo_delta)
    tiempo_anterior = tiempo_actual
  
    

 
def dibujarObstaculo(): #PENTAGONO
    global xObstaculo
    global yObstaculo

    if obstaculoVivo:
        glPushMatrix()
        glTranslate(xObstaculo, yObstaculo, 0.0 )
        glBegin(GL_POLYGON)
        glColor3f(0.490, 0.117, 0.980) 
        glVertex(0.0, 0.05, 0.0)
        glVertex(-0.05, 0.0, 0.0)
        glVertex(-0.03, -0.05, 0.0)
        glVertex(0.03, -0.05, 0.0)
        glVertex(0.05,0.0, 0.0)
        glEnd()
        glPopMatrix()



def dibujarNave():
    global posX_nave
    global posY_nave
    glPushMatrix()
    glTranslate(posX_nave, posY_nave, 0)
    glScalef(0.035,0.035,0.035)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.0,1.0,0.0)
    glVertex3f(0.4,0.4,0.0)
    glVertex3f(0.4,-0.4,0)
    glVertex3f(-0.4,-0.4,0)
    glVertex3f(-0.4,0.4,0.0)
    glEnd()
    glColor3f(0.8,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.4,-0.2,0.0)
    glVertex3f(0.0,-0.4,0.0)
    glVertex3f(-0.6,-1.0,0.0)
    glVertex3f(0.4,-0.2,0.0)
    glVertex3f(0.0,-0.4,0.0)
    glVertex3f(0.6,-1.0,0.0)
    glEnd()
    glColor3f(0.7,0.9,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3+0.3,0.0)
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3+0.1,0.0)
    glEnd()
    glPopMatrix()

def dibujarNave():
    global posX_nave
    global posY_nave
    glPushMatrix()
    glTranslate(posX_nave, posY_nave, 0)
    glScalef(0.035,0.035,0.035)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.0,1.0,0.0)
    glVertex3f(0.4,0.4,0.0)
    glVertex3f(0.4,-0.4,0)
    glVertex3f(-0.4,-0.4,0)
    glVertex3f(-0.4,0.4,0.0)
    glEnd()
    glColor3f(0.8,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.4,-0.2,0.0)
    glVertex3f(0.0,-0.4,0.0)
    glVertex3f(-0.6,-1.0,0.0)
    glVertex3f(0.4,-0.2,0.0)
    glVertex3f(0.0,-0.4,0.0)
    glVertex3f(0.6,-1.0,0.0)
    glEnd()
    glColor3f(0.7,0.9,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3+0.3,0.0)
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.3,sin(angulo)*0.3+0.1,0.0)
    glEnd()
    glPopMatrix()
     

def dibujarObstaculo2(): #OCTAGONO
    global xObstaculo2
    global yObstaculo2

    if obstaculoVivo2:
        glPushMatrix()
        glTranslate(xObstaculo2, yObstaculo2, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.141, 0.078, 1.0)
        glVertex(0.01, 0.05, 0.0)
        glVertex(-0.02, 0.05, 0.0)
        glVertex(-0.05, 0.02, 0.0)
        glVertex(-0.05, -0.01, 0.0)
        glVertex(-0.02, -0.04, 0.0)
        glVertex(0.01, -0.04, 0.0)
        glVertex(0.04, -0.01, 0.0)
        glVertex(0.04, 0.02, 0.0)
        glEnd()
        glPopMatrix()

def dibujarObstaculo3():#HEXAGONO
    global xObstaculo3
    global yObstaculo3

    if obstaculoVivo3:
        glPushMatrix()
        glTranslate(xObstaculo3, yObstaculo3, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.277, 0.439, 0.760)
        glVertex(0.02, 0.05, 0.0)
        glVertex(-0.02, 0.05, 0.0)
        glVertex(-0.05, 0.01, 0.0)
        glVertex(-0.02, -0.03, 0.0)
        glVertex(0.02, -0.03, 0.0)
        glVertex(0.05, 0.01, 0.0)
        glEnd()
        glPopMatrix()

def dibujarObstaculo4():
    global xObstaculo4
    global yObstaculo4

    if obstaculoVivo4: #TRAPECIO
        glPushMatrix()
        glTranslate(xObstaculo4, yObstaculo4, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.639, 0.239, 0.211)
        glVertex(0.03, 0.04, 0.0)
        glVertex(-0.03, 0.04, 0.0)
        glVertex(-0.05, -0.03, 0.0)
        glVertex(0.05, -0.03, 0.0)
        glEnd()
        glPopMatrix()

def dibujarObstaculo5(): #COHETE
    global xObstaculo5
    global yObstaculo5

    if obstaculoVivo5:
        glPushMatrix()
        glTranslate(xObstaculo5, yObstaculo5, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 0, 0)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.03 - 0.05, sin(angulo)*0.03 + 0.00,0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex(-0.02, 0.02, 0.0)
        glVertex(-0.02, -0.02, 0.0)
        glVertex(-0.04, 0.015, 0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex(-0.02, 0.02, 0.0)
        glVertex(-0.02, -0.02, 0.0)
        glVertex(-0.04, -0.015, 0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex(-0.02, 0.01, 0.0)
        glVertex(-0.04, 0.0, 0.0)
        glVertex(-0.02, -0.015, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1, 0, 0)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.01 + 0.03,sin(angulo) * 0.01 + 0.0 ,0.0) #2/ X Y Y
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(0.03, 0.01, 0.0)
        glVertex(-0.02, 0.01, 0.0)
        glVertex(-0.02, -0.01, 0.0)
        glVertex(0.03, -0.01, 0.0)
        glEnd()
        

        glBegin(GL_POLYGON) #VENTANA
        glColor3f(0.380, 0.741, 0.909)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.005 + 0.02,sin(angulo) * 0.005 + 0.0 ,0.0) #2/ X Y Y
        glEnd()

        glPopMatrix()

def dibujarObstaculo6(): #PIRAMIDE
    global xObstaculo6
    global yObstaculo6

    if obstaculoVivo6:
        glPushMatrix()
        glTranslate(xObstaculo6, yObstaculo6, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.858, 0.713, 0.274)
        glVertex(0.0, 0.05, 0.0)
        glVertex(-0.05, -0.03, 0.0)
        glVertex(0.0, -0.05, 0.0)
        glVertex(0.05, -0.03, 0.0)
        glEnd()
        glPopMatrix()

def dibujarObstaculo7():
    global xObstaculo7
    global yObstaculo7

    if obstaculoVivo7: #BANDERA
        glPushMatrix()
        glTranslate(xObstaculo7, yObstaculo7, 0.0)
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(-0.02, 0.05, 0.0)
        glVertex(-0.03, 0.05, 0.0)
        glVertex(-0.03, -0.05, 0.0)
        glVertex(-0.02, -0.05, 0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.639, 0.239, 0.211)
        glVertex(-0.02, 0.05, 0.0)
        glVertex(-0.02, 0.0, 0.0)
        glVertex(0.03, 0.020, 0.0)
        glEnd()

        glPopMatrix()

def dibujarObstaculo8(): #ESTRELLA AZUL 6 PICOS
    global xObstaculo8
    global yObstaculo8

    if obstaculoVivo8:
        glPushMatrix()
        glTranslate(xObstaculo8, yObstaculo8, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.258, 0.878, 0.960)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.07 - 0.0, sin(angulo)*0.07 + 0.00,0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.258, 0.878, 0.960)
        glVertex(0.03, 0.03, 0.0)
        glVertex(-0.03, 0.03, 0.0)
        glVertex(0.0, -0.05, 0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.258, 0.878, 0.960)
        glVertex(0.03, -0.03, 0.0)
        glVertex(0.0, 0.05, 0.0)
        glVertex(-0.03, -0.03, 0.0)
        glEnd()

        glPopMatrix()

def dibujarObstaculo9(): #ESTRELLA 2 8 PICOS
    global xObstaculo9
    global yObstaculo9

    if obstaculoVivo9:
        glPushMatrix()
        glTranslate(xObstaculo9, yObstaculo9, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.619, 1.0, 0.941)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.07 - 0.0, sin(angulo)*0.07 + 0.00,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.619, 1.0, 0.941)
        glVertex(0.03, 0.03, 0.0)
        glVertex(-0.03, 0.03, 0.0)
        glVertex(-0.03, -0.03, 0.0)
        glVertex(0.03, -0.03, 0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.619, 1.0, 0.941)
        glVertex(0.0, 0.04, 0.0)
        glVertex(-0.04, 0.0, 0.0)
        glVertex(0.0, -0.04, 0.0)
        glVertex(0.04, 0.0, 0.0)
        glEnd()
        glPopMatrix()


def dibujarObstaculo10(): #MEDIO CIRCULO 
    global xObstaculo10
    global yObstaculo10

    if obstaculoVivo10:
        glPushMatrix()
        glTranslate(xObstaculo10, yObstaculo10, 0.0)
        glBegin(GL_POLYGON)

        for x in range(180):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.06 - 0.4,sin(angulo) * 0.075 + 0.5 ,0.0)
        glEnd()
        glPopMatrix()




def dibujarObstaculo11(): #SATURNO
    global xObstaculo11
    global yObstaculo11

    if obstaculoVivo11:
        glPushMatrix()
        glTranslate(xObstaculo11, yObstaculo11, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.721, 0.580, 0.2)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.07 - 0.05, sin(angulo)*0.07 + 0.05, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.874, 0.529)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.05 - 0.05,sin(angulo) * 0.025 + 0.05 ,0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.721, 0.580, 0.2)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.04 - 0.05,sin(angulo) * 0.04 + 0.05 ,0.0)
        glEnd()
        glPopMatrix()

    

def dibujarObstaculo12(): #ALIEN 
    global xObstaculo12
    global yObstaculo12

    if obstaculoVivo12:
        glPushMatrix()
        glTranslate(xObstaculo12, yObstaculo12, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.521, 0.949, 0.901)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.08 - 0.05, sin(angulo)*0.08 + 0.03,0.0)
        glEnd()

        glBegin(GL_POLYGON) #LUZ NAVE
        glColor3f(0.521, 0.949, 0.901)
        glVertex(-0.04, 0.03, 0.0)
        glVertex(-0.06, 0.03, 0.0)  
        glVertex(-0.07, -0.03, 0.0)
        glVertex(-0.03, -0.03, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.529, 1.0, 0.788)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.025 - 0.05,sin(angulo) * 0.025 + 0.05 ,0.0)
        glEnd()
        

        glBegin(GL_POLYGON)
        glColor3f(0.368, 0.380, 0.384)
        for x in range(360): 
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.05 - 0.05,sin(angulo) * 0.02 + 0.04 ,0.0)
        glEnd()



        glPopMatrix()


def dibujarObstaculo13(): #PLANETA
    global xObstaculo13
    global yObstaculo13

    if obstaculoVivo13:
        glPushMatrix()
        glTranslate(xObstaculo13, yObstaculo13, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.639, 0.239, 0.211)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.08 - 0.05, sin(angulo)*0.08 + 0.05,0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.639, 0.239, 0.211)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.05 - 0.05,sin(angulo) * 0.05 + 0.05 ,0.0)
        glEnd()
        glPopMatrix()


def dibujarObstaculo14(): #ASTONAUTA
    global xObstaculo14
    global yObstaculo14

    if obstaculoVivo14:
        glPushMatrix()
        glTranslate(xObstaculo14, yObstaculo14, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.02 - 0.0,sin(angulo) * 0.02 + 0.02 ,0.0) #2/ X Y Y
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(0.01, 0.02, 0.0)
        glVertex(-0.01, 0.02, 0.0)
        glVertex(-0.01, -0.02, 0.0)
        glVertex(0.01, -0.02, 0.0)
        glEnd()


        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.015 - 0.0,sin(angulo) * 0.015 + 0.02 ,0.0) #2/ X Y Y
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(0.01, -0.02, 0.0)
        glVertex(0.002, -0.02, 0.0)
        glVertex(0.002, -0.04, 0.0)
        glVertex(0.01, -0.04, 0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(-0.002, -0.02, 0.0)
        glVertex(-0.01, -0.02, 0.0)
        glVertex(-0.01, -0.04, 0.0)
        glVertex(-0.002, -0.04, 0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(0.02, 0.01, 0.0)
        glVertex(0.01, 0.01, 0.0)
        glVertex(0.01, -0.01, 0.0)
        glVertex(0.02, -0.01, 0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        glVertex(-0.01, 0.01, 0.0)
        glVertex(-0.02, 0.01, 0.0)
        glVertex(-0.02, -0.01, 0.0)
        glVertex(-0.01, -0.01, 0.0)
        glEnd()
        glPopMatrix()



def dibujarObstaculo15(): #PLANETA HUMO
    global xObstaculo15
    global yObstaculo15

    if obstaculoVivo15:
        glPushMatrix()
        glTranslate(xObstaculo15, yObstaculo15, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 1, 1)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.04 - 0.03, sin(angulo)*0.04 + 0.02,0.0)
        glEnd()


        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.301, 0.701, 0.788)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.06 - 0.0, sin(angulo)*0.06 + 0.05,0.0)
        glEnd()

    
        glBegin(GL_POLYGON)
        glColor3f(0.301, 0.701, 0.788)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.04 - 0.0,sin(angulo) * 0.04 + 0.05 ,0.0) #2/ X Y Y
        glEnd()


        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.03 - 0.03,sin(angulo) * 0.01 + 0.02 ,0.0) #2/ X Y Y
        glEnd()


        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.03 - 0.05,sin(angulo) * 0.01 + 0.03 ,0.0) #2/ X Y Y
        glEnd()
        glPopMatrix()


def dibujarObstaculo16(): #CUADRADO
    global xObstaculo16
    global yObstaculo16

    if obstaculoVivo16:
        glPushMatrix()
        glTranslate(xObstaculo16, yObstaculo16, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.337, 0.231, 0.470)
        glVertex(-0.05, 0.05, 0.0)
        glVertex(0.05, 0.05, 0.0)
        glVertex(0.05, -0.05, 0.0)
        glVertex(-0.05, -0.05, 0.0)
        glEnd()
        glPopMatrix()



def dibujarObstaculo17(): #RELOJ DE ARENA
    global xObstaculo17
    global yObstaculo17

    if obstaculoVivo17:
        glPushMatrix()
        glTranslate(xObstaculo17, yObstaculo17, 0.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.709, 0.537, 0.243)
        glVertex(0.05, 0.05, 0.0)
        glVertex(-0.05, 0.05, 0.0)
        glVertex(0.0, -0.01, 0.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.709, 0.537, 0.243)
        glVertex(0.00, 0.00, 0.0)
        glVertex(-0.05, -0.05, 0.0)
        glVertex(0.05, -0.05, 0.0)
        glEnd()
        glPopMatrix()



def dibujarObstaculo18(): #ESTRELLA
    global xObstaculo18
    global yObstaculo18

    if obstaculoVivo18:
        glPushMatrix()
        glTranslate(xObstaculo18, yObstaculo18, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.870, 0.756, 0.349)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.08,sin(angulo)*0.08,0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.701, 0.654, 0.313)
        glVertex(0.0, 0.05, 0.0)
        glVertex(-0.03, 0.0, 0.0)
        glVertex(0.0, -0.05, 0.0)
        glVertex(0.03, 0.0, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.980, 0.949, 0.705)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.01 + 0.00,sin(angulo) * 0.01 + 0.0 ,0.0) #2/ X Y Y
        glEnd()
        glPopMatrix()


def dibujarObstaculo19(): #SOL
    global xObstaculo19
    global yObstaculo19

    if obstaculoVivo19:
        glPushMatrix()
        glTranslate(xObstaculo19, yObstaculo19, 0.0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.870, 0.756, 0.349)
        glVertex3f(0.0,0.0,0.0)
        for x in range(361):
            angulo = x * 3.14159 / 180.0
            glColor3f(0.0,0.0,0.0)
            glVertex3f(cos(angulo)*0.08,sin(angulo)*0.08,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.988, 0.474, 0.050)
        glVertex(0.04, 0.04, 0.0)
        glVertex(-0.04, 0.04, 0.0)
        glVertex(-0.04, -0.04, 0.0)
        glVertex(0.04, -0.04, 0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.988, 0.474, 0.050)
        glVertex(0.05, 0.0, 0.0)
        glVertex(0.0, 0.05, 0.0)
        glVertex(-0.05, 0.0, 0.0)
        glVertex(0.0, -0.05, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1, 0.760, 0.239)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.04 + 0.00,sin(angulo) * 0.04 + 0.0 ,0.0) #2/ X Y Y
        glEnd()
        glPopMatrix()


def dibujarObstaculo20(): #ASTEROIDES
    global xObstaculo20
    global yObstaculo20

    if obstaculoVivo20:
        glPushMatrix()
        glTranslate(xObstaculo20, yObstaculo20, 0.0)

        glBegin(GL_POLYGON)
        glColor3f(0.368, 0.380, 0.384)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.03 + 0.0 ,sin(angulo) * 0.03 + 0.0 ,0.0) #2/ X Y Y
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.368, 0.380, 0.384)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.02 - 0.025 ,sin(angulo) * 0.013 - 0.025 ,0.0) #2/ X Y Y
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.368, 0.380, 0.384)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.013 - 0.01 ,sin(angulo) * 0.013 - 0.03 ,0.0) #2/ X Y Y
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.368, 0.380, 0.384)
        for x in range(360):
            angulo = x * 3.1416 / 180.0
            glVertex3f(cos(angulo) * 0.013 + 0.01 ,sin(angulo) * 0.013 - 0.05 ,0.0) #2/ X Y Y
        glEnd()
        glPopMatrix()


def dibujar_bala():
    global disparando
    global xBala
    global yBala
    if disparando == True:
        glPushMatrix()
        glTranslate(xBala, yBala, 0.0)
        glRotate(anguloBala, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(-0.01, 0.01, 0.0)
        glVertex3f(0.01, 0.01, 0.0)
        glVertex3f(0.01, -0.01, 0.0)
        glVertex3f(-0.01, -0.01, 0.0)
        glEnd()
        glPopMatrix()


def dibujarCarrito():
    global colisionando
    global xCarrito
    global yCarrito
    glPushMatrix()
    glTranslate(xCarrito, yCarrito, 0.0)
    glRotate(angulo, 0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    if colisionando == True:
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(0.745, 0.749, 0.749)
    glVertex3f(0.0, 0.05, 0.0)
    glVertex3f(-0.05, -0.05, 0.0)
    glVertex3f(0.05, -0.05, 0.0)
    glEnd()
    glPopMatrix()


def dibujar():
    # rutinas de dibujo
    dibujarObstaculo()
    dibujarObstaculo2()
    dibujarObstaculo3()
    dibujarObstaculo4()
    dibujarObstaculo5()
    dibujarObstaculo6()
    dibujarObstaculo7()
    dibujarObstaculo8()
    dibujarObstaculo9()
    dibujarObstaculo10()
    dibujarObstaculo11()
    dibujarObstaculo12()
    dibujarObstaculo13()
    dibujarObstaculo14()
    dibujarObstaculo15()
    dibujarObstaculo16()
    dibujarObstaculo17()
    dibujarObstaculo18()
    dibujarObstaculo19()
    dibujarObstaculo20()
    dibujarCarrito()
    dibujar_bala() 


def key_callback(window, key, scancode, action, mods):
    global disparando
    global anguloBala
    global xBala
    global yBala
    if not disparando and key == glfw.KEY_SPACE and action == glfw.PRESS:
        disparando = True
        xBala = xCarrito
        yBala = yCarrito
        anguloBala = angulo


def main():
    # inicia glfw
    if not glfw.init():
        return

    # crea la ventana,
    # independientemente del SO que usemos
    window = glfw.create_window(800, 800, "Mi ventana", None, None)

    # Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    # Establecemos el contexto
    glfw.make_context_current(window)

    # Activamos la validación de
    # funciones modernas de OpenGL
    glewExperimental = True

    # Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    # Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    glfw.set_key_callback(window, key_callback)


    while not glfw.window_should_close(window):
        # Establece regiond e dibujo
        glViewport(0, 0, 800, 800)
        # Establece color de borrado
        glClearColor(0.0, 0.0, 0.0, 0)
        # Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar
        actualizar(window)
        dibujar()

        # Preguntar si hubo entradas de perifericos
        # (Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        # Intercambia los buffers
        glfw.swap_buffers(window)

    # Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    # Termina los procesos que inició glfw.init
    glfw.terminate()


if __name__ == "__main__":
    main()
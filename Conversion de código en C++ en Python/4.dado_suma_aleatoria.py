# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:50:21 2020

@author: vilcajoal - Vilca Joel Alberto
"""
# =============================================================================
#                           CÓDIGO C++
# =============================================================================
# SETW(): agrega espacios vacios recibe como parametro un entero 
# RAND(): devuelve un numero aleatorio "1+rand()%6" en el rango de 1 y 6
# SRAND(x): fija al X como semilla para numeros aleatorios
# =============================================================================
#    #include <iostream>
#    #include <cstdlib>
#    #include <ctime>   // contiene prototipo de función time
#    using namespace std;
#    int tiraDados( void );  // prototipo de la función
#    int main()
#    {
#       enum Status { CONTINUA, GANA, PIERDE };
#       int suma;
#       int miPunto;
#       Status estadoJuego;  // CONTINUA, GANA o PIERDE
#       
#       srand( time( 0 ) ); // randomiza números mediante time
#       suma = tiraDados(); // primer tiro de dados
#    
#       switch ( suma ) 
#       {
#          case 7: 
#    	   case 11:            
#             estadoJuego = GANA;
#             break;
#          case 2: 
#    	   case 3: 
#    	   case 12:             
#             estadoJuego = PIERDE;
#             break;
#          default:            
#             estadoJuego = CONTINUA;
#             miPunto = suma;
#             cout << "El punto es " << miPunto << endl;
#             break;                // opcional   
#    
#       }  
#       while ( estadoJuego == CONTINUA ) 
#       { 
#          suma = tiraDados();  // tira dados nuevamente
#          if ( suma == miPunto )       // gana por puntos
#             estadoJuego = GANA;
#          else
#             if ( suma == 7 )          // pierde por obtener 7
#                estadoJuego = PIERDE;
#    
#       } 
#       if ( estadoJuego == GANA )
#          cout << "El jugador gana" << endl;
#       else
#          cout << "El jugador pierde" << endl;
#       return 0;  
#    } 
#    int tiraDados( void )
#    {
#       int dado1;
#       int dado2;
#       int sumaTrabajo;
#       dado1 = 1 + rand() % 6;  // aleatorio del dado1
#       dado2 = 1 + rand() % 6;  // aleatorio del dado2
#       sumaTrabajo = dado1 + dado2;  
#       cout << "El jugador tiro " << dado1 << " + " << dado2
#            << " = " << sumaTrabajo << endl;
#       return sumaTrabajo;         // devuelve suma de los dados
#    } 
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# RANDINT(A,B): devuelve numero aleatorio entre a y b
# str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# 
# =============================================================================
from random import randint


estado = [ "AlTUAL", "CONTINUA", "GANA", "PIERDE"]
suma = 0
mi_puntaje = 0

def tira_dados():
    
    dado_1 = 0
    dado_2 = 0
    suma_trabajo = 0
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    suma_trabajo = dado_1 + dado_2
    print("El jugador tiró {} + {} = {}".format(dado_1, dado_2, suma_trabajo))
    return suma_trabajo
    

def case2():
        global estado
        estado[0]=estado[3]
    
def case3():
        global estado
        estado[0]=estado[3]
        
def case7():
        global estado
        estado[0]=estado[2]
    
def case11():
        global estado
        estado[0]=estado[2]
        
def case12():
        global estado
        estado[0]=estado[3]
    
def default():
        global estado, suma, mi_puntaje
        estado[0]=estado[1]
        mi_puntaje = suma
        print("El punto es {} ".format(mi_puntaje))
        
def Switch(suma):
        switcher = {
                2: case2,
                3: case3,
                7: case7,
                11: case11,
                12: case12
                }
        funcion = switcher.get(suma, "default")
        if funcion == "default": default()
        else: funcion()    
    
def start():
    global estado, suma, mi_puntaje
    suma = tira_dados()
    Switch(suma)
    
    while estado[0]==estado[1]:
        suma = tira_dados()
        if suma==mi_puntaje: estado[0]= estado[2]
        else:
            if suma == 7: estado[0]=estado[3]
    
    if estado[0]==estado[2]: print("El jugador gana")
    else: print("El jugador pierde")
    
if __name__ == '__main__':
    start()





















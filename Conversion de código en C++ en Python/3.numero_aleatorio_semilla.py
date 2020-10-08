# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:44:56 2020

@author: vilcajoal - Vilca Joel Alberto
"""
# =============================================================================
#                           CÓDIGO C++
# =============================================================================
# SETW(): agrega espacios vacios recibe como parametro un entero 
# RAND(): devuelve un numero aleatorio "1+rand()%6" en el rango de 1 y 6
# =============================================================================
#    #include <iostream>
#    #include <iomanip>
#    #include <cstdlib>// contiene srand y rand
#    using namespace std;
#    int main()
#    {
#       unsigned semilla;
#       cout << "Introduzca semilla: ";
#       cin >> semilla;
#       srand( semilla );
#       for ( int contador = 1; contador <= 10; contador++ ) 
#       {
#       		
#            cout << setw( 10 ) << ( 1 + rand() % 6 );
#            
#          	if ( contador % 5 == 0 )
#            	 cout << endl;
#        	
#    		 
#       } 
#       return 0;  
#    }

# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# RANDINT(A,B): devuelve numero aleatorio entre a y b
# str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# SEED(X): fija el X como semilla para generar numeros aleatorios
# =============================================================================

import random
# from random import randint

def start():
    semilla = int(input("Ingrese semilla "))
    random.seed(semilla)
    for contador in range(1, 11):
        print("".ljust(10,) , random.randint(1,6), end = "")
        if contador % 5 == 0:
            print("")
        

    
if __name__ == '__main__':
    start()
    
    
    
    
    
    
    
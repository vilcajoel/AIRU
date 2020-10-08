# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:17:41 2020

@author: vilcajoal - Vilca Joel Alberto
"""
# =============================================================================
#                           CÓDIGO C++
# =============================================================================
# SETW(): agrega espacios vacios recibe como parametro un entero 
# RAND(): devuelve un numero aleatorio "1+rand()%6" en el rango de 1 y 6
# =============================================================================
# //Numero aleatorio estatico
# #include <iostream>
# #include <iomanip>
# #include <cstdlib>   
# using namespace std;
# int main()
# {
#    for ( int contador = 1; contador <= 20; contador++ ) 
#    {
#       cout<< setw( 10 ) << ( 1 + rand() % 6 ); 
#       if ( contador % 5 == 0 )
#          cout << endl;
#    } 
#    return 0;  
# }
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# RANDINT(A,B): devuelve numero aleatorio entre a y b
# str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# =============================================================================

from random import randint

def start():
    for contador in range(1, 21):
        print("".ljust(10,) , randint(1,6), end = "")
        if contador % 5 == 0:
            print("")
        

    
if __name__ == '__main__':
    start()
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:13:00 2020

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
#    #include <iomanip>
#    #include <cstdlib>
#    #include <ctime>
#    using namespace std;
#    int main()
#    {
#       const int tamanoArreglo = 7;
#       int frecuencia[ tamanoArreglo ] = { 0 };
#       srand( time( 0 ) );  
#       // tira los dados 6000 veces
#       for ( int tiro = 1; tiro <= 6000; tiro++ )       
#          ++frecuencia[ 1 + rand() % 6 ]; 
#       cout << "Cara" << setw( 13 ) << "Frecuencia" << endl;
#       // muestra la frecuencia de los elementos 1 a 6 en formato tabular
#       for ( int cara = 1; cara < tamanoArreglo; cara++ )  
#          cout << setw( 4 ) << cara
#               << setw( 13 ) << frecuencia[ cara ] << endl;
#       return 0;  
#    } 
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# RANDINT(A,B): devuelve numero aleatorio entre a y b
# str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# =============================================================================

from random import randint

def start():
    TANANO_ARREGLO = 7
    frecuencia = []
    for i in range(1,TANANO_ARREGLO):
        frecuencia.append(0)
    for i in range(1,6001):
        posicion = randint(1,TANANO_ARREGLO-1)-1
        frecuencia[posicion] = 1 + frecuencia[posicion]
    print("CARA".ljust(10,) + "FRECUENCIA" )
    for i in range(1,TANANO_ARREGLO):
        print("{}".ljust(15,).format(i) + "{}".format(frecuencia[i-1]))
        
    

if __name__ == '__main__':
    start()
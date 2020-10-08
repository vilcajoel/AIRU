# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 03:13:25 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================
# SETW(): agrega espacios vacios recibe como parametro un entero 
# =============================================================================
#    #include <iostream>
#    #include <iomanip>
#    using namespace std;
#    unsigned long factorial( unsigned long ); // prototipo de la función
#    int main()
#    {
#       for ( int i = 0; i <= 10; i++ )
#          cout << setw( 2 ) << i << "! = " 
#               << factorial( i ) << endl;
#    
#       return 0;  // indica terminació exitosa
#    }
#    unsigned long factorial( unsigned long numero )
#    {
#       if ( numero <= 1 )  
#          return 1;
#       else                
#          return numero * factorial( numero - 1 );
#    } 
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# =============================================================================

def factorial(numero):
    if numero <=1:
        return 1
    else :
        return numero * factorial(numero - 1)

def start():
    for i in range(0,11):
        print("".ljust(3,) + "{}".format(i) + "! = ".ljust(10,) + "{}".format(factorial(i)))



if __name__ == '__main__':
    start()
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 03:32:07 2020

@author: vilcajoal - Vilca Joel Alberto
"""
# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================
#    #include <iostream>
#    using namespace std;
#    unsigned long fibonacci( unsigned long ); 
#    int main()
#    {
#       unsigned long resultado, numero;
#       cout << "Introduzca un entero: ";
#       cin >> numero;
#       resultado = fibonacci( numero );
#       cout << "Fibonacci(" << numero << ") = " << resultado << endl;
#       return 0;  
#    } 
#    unsigned long fibonacci( unsigned long n )
#    {
#       if ( n == 0 || n == 1 )  
#          return n;
#       else             
#          return fibonacci( n - 1 ) + fibonacci( n - 2 );
#    }
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# 
# =============================================================================

def fibonacci(n):
    if n ==0 or n==1 :
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)
      
    
def start():
    numero= int(input("Introduzca la posicion deseada de la sucesión  fibonacci: "))
    resultado = fibonacci(numero)
    print("Fibonacci({}) = {}".format(numero,resultado))


if __name__ == '__main__':
    start()

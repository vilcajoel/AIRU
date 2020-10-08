# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 03:52:44 2020

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
#    int main()
#    {
#       const int tamanoArreglo = 10;
#       int n[ tamanoArreglo ] = { 19, 3, 15, 7, 11, 9, 13, 5, 17, 1 };
#       cout << "Elemento" << setw( 13 ) << "Valor"
#            << setw( 17 ) << "Histograma" << endl;
#       for ( int i = 0; i < tamanoArreglo; i++ ) 
#       {
#          cout << setw( 7 ) << i << setw( 13 ) 
#               << n[ i ] << setw( 9 );
#          for ( int j = 0; j < n[ i ]; j++ )   
#             cout << '*';
#          cout << endl;  
#       } 
#       return 0;  
#    } 
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# # str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# =============================================================================

    
def start():
    TAMANO_ARREGLO = 10
    n = ["19", "3 ", "15", "7 ", "11", "9 ", "13", "5 ", "17", "1 "]
    print("Elemento".ljust(15,) + "valor".ljust(17,)+"Histograma")
    for i in range(0, TAMANO_ARREGLO):
        print("{}".ljust(18,).format(i)+ "{}".ljust(15).format(n[i]), end="")
        for j in range(0, int(n[i])):
            print("*", end="")
        print("")


if __name__ == '__main__':
    start()
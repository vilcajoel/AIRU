# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:18:47 2020

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
#    #include <cstdlib> 
#    using namespace std;  
#    int main()
#    {
#       int frecuencia1 = 0;
#       int frecuencia2 = 0;
#       int frecuencia3 = 0; 
#       int frecuencia4 = 0;
#       int frecuencia5 = 0; 
#       int frecuencia6 = 0;
#       int cara;  
#       for ( int tiro = 1; tiro <= 6000; tiro++ ) 
#       {
#          cara = 1 + rand() % 6; 
#          switch ( cara ) {
#             case 1:  
#                ++frecuencia1;
#                break;
#             case 2:  
#                ++frecuencia2;
#                break;
#             case 3:  
#                ++frecuencia3;
#                break;
#             case 4:  
#                ++frecuencia4;
#                break;
#             case 5:  
#                ++frecuencia5;
#                break;
#             case 6:  
#                ++frecuencia6;
#                break;
#             default: 
#                cout<<"¡El programa no debe llegar hasta aquí!";
#          } 
#       } 
#       cout << "Cara" << setw( 13 ) << "Frecuencia"
#            << "\n   1" << setw( 13 ) << frecuencia1
#            << "\n   2" << setw( 13 ) << frecuencia2
#            << "\n   3" << setw( 13 ) << frecuencia3
#            << "\n   4" << setw( 13 ) << frecuencia4
#            << "\n   5" << setw( 13 ) << frecuencia5
#            << "\n   6" << setw( 13 ) << frecuencia6 << endl;
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
frecuencia1 = frecuencia2 = frecuencia3 = frecuencia4 = frecuencia5 = frecuencia6 = 0

def start():
    
    
    def case1():
        global frecuencia1
        frecuencia1+= 1
    
    def case2():
        global frecuencia2
        frecuencia2 += 1
        
    def case3():
        global frecuencia3
        frecuencia3 += 1
    
    def case4():
        global frecuencia4
        frecuencia4 += 1
    
    def case5():
        global frecuencia5
        frecuencia5 += 1
    
    def case6():
        global frecuencia6
        frecuencia6 += 1
    
           
    def Switch(cara):
        switcher = {
                1: case1,
                2: case2,
                3: case3,
                4: case4,
                5: case5,
                6: case6
                }
        funcion = switcher.get(cara, lambda: "El programa no debe llegar aqui")
        funcion()
        
    
    
    cara = 0
    for tiro in range(1,6001):
        cara = randint(1,6)
        Switch(cara)
        
    print ("CARA".ljust(20,), end = "")
    print ("FRECUENCIA")
    print ("1", end = "")
    print ("".ljust(20,), frecuencia1)
    print ("2", end = "")
    print ("".ljust(20,), frecuencia2)
    print ("3", end = "")
    print ("".ljust(20,), frecuencia3)
    print ("4", end = "")
    print ("".ljust(20,), frecuencia4)
    print ("5", end = "")
    print ("".ljust(20,), frecuencia5)
    print ("6", end = "")
    print ("".ljust(20,), frecuencia6)


if __name__ == '__main__':
    start()






















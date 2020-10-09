# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 02:58:15 2020

@author: vilcajoal - Vilca Joel Alberto
"""
# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================
#    // Búsqueda lineal en un arreglo.
#    #include <iostream>
#    using std::cout;
#    using std::cin;
#    using std::endl;
#    using namespace std;
#    int busquedaLineal( const int [], int, int );  // prototipo
#    int main()
#    {
#       const int tamanoArreglo = 100;  // tamaño del arreglo a
#       int a[ tamanoArreglo ];         // crea el arreglo a
#       int claveBusqueda;              // valor a localizar dentro de a
#       for ( int i = 0; i < tamanoArreglo; i++ )  // crea algunos datos
#          a[ i ] = 2 * i;
#          cout << "Introduce la clave de busqueda entera: ";
#          cin >> claveBusqueda;
#      // intenta localizar claveBusqueda dentro del arreglo a
#       int elemento = busquedaLineal( a, claveBusqueda, tamanoArreglo );
#     // despliega los resultados
#       if ( elemento != -1 )
#          cout << "Encontre valor en el elemento " << elemento << endl;
#       else
#          cout << "Valor no encontrado" << endl;
#       return 0;  // indica terminación exitosa
#    } // fin de main
#    // compara la clave con cada elemento del arreglo hasta encontrar su 
#    // ubicación o hasta que se alcanza el final del arreglo; devuelve el subíndice 
#    // del elemento si es la clave o -1 si ésta no se encontró
#    int busquedaLineal( const int arreglo[], int clave, int tamanoDelArreglo )
#    {
#       for ( int j = 0; j < tamanoDelArreglo; j++ )
#          if ( arreglo[ j ] == clave )  // si se encuentra ,
#             return j;              // devuelve la ubicación de la clave
#       return -1;  // la clave no se encontró
#    } // fin de la función busquedaLineal

# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================


def start():
    TANANO_ARREGLO = 100
    a = []
    for i in range(0,TANANO_ARREGLO):
        a.append(0)
    for i in range(0,TANANO_ARREGLO):
        a[i]= 2*i
    clave_busqueda= int(input("Ingrese la clave de busqueda: "))
    elemento =  busqueda_lineal(a, clave_busqueda,TANANO_ARREGLO)
    if elemento != -1 :
        print("Encontre el valor en el elemento {}".format(elemento))
        print(a)
    else:
        print("Valor no encontrado")


def busqueda_lineal(a, clave_busqueda,TANANO_ARREGLO):
    for j in range(0,TANANO_ARREGLO):
        if a[j]==clave_busqueda:
            return j
    return -1
    
    



if __name__=='__main__':
    start()


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:41:32 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================

#    // Búsqueda binaria dentro de un arreglo.
#    #include <iostream>
#    using std::cout;
#    using std::cin;
#    using std::endl;
#    #include <iomanip>
#    using std::setw;
#    // prototipo de la función
#    int busquedaBinaria( const int [], int, int, int, int );
#    void despliegaEncabezado( int );
#    void despliegaFila( const int [], int, int, int, int );
#    int main()
#    {
#       const int tamanoArreglo = 15;  // tamaño del arreglo a
#       int a[ tamanoArreglo ];        // crea el arreglo a
#       int clave;                   // valor a localizar en a
#       for ( int i = 0; i < tamanoArreglo; i++ )  // crea algunos datos
#          a[ i ] = 2 * i;   
#       cout << "Introduzca un numero entre 0 y 28: ";
#       cin >> clave;
#       despliegaEncabezado( tamanoArreglo );
#       // búsqueda de la clave en el arreglo a
#       int resultado = 
#    	      busquedaBinaria( a, clave, 0, tamanoArreglo - 1, tamanoArreglo );
#       // despliega resultados
#       if ( resultado != -1 )
#         cout << '\n' << clave << " se encuentra en el elemento del arreglo "
#              << resultado << endl;
#       else
#         cout << '\n' << clave << " no se encontro" << endl;
#       return 0;  // indica terminación exitosa
#    } // fin de main

#    // función para realizar la búsqueda binaria dentro de un arreglo
#    int busquedaBinaria( const int b[], int claveBusqueda, int bajo, int alto, int tamano )
#    {
#    int central;
#    // repetición hasta que el subíndice bajo sea mayor que el subíndice alto
#       while ( bajo <= alto )
#       {
#         // determina el elemento central del subarreglo en el que se busca
#          central = ( bajo + alto ) / 2;  
#         // despliega el subarreglo utilizado en este ciclo de la iteración
#          despliegaFila( b, bajo, central, alto, tamano );
#        // si claveBusqueda coincide con el elemento central, devuelve el elemento central
#         if ( claveBusqueda == b[ central ] )  // coincide
#            return central;
#         else 
#            // si claveBusqueda es menor que el elemento central, 
#            // establece el nuevo elemento alto
#             if ( claveBusqueda < b[ central ] )
#                alto = central - 1;  // busca bajo hasta el final del arreglo
#             // si claveBusqueda es mayor que el elemento central, 
#             // establece el nuevo elemento bajo
#             else
#                bajo = central + 1;   // busca bajo hasta el final del arreglo
#       }
#      return -1;  // no se encontró claveBusqueda
#    } // fin de la función busquedaBinaria

#    // despliega el encabezado de salida
#    void despliegaEncabezado( int tamano )
#    {
#       cout << "\nSubindices:\n";
#       // muestra encabezados de columnas
#       for ( int j = 0; j < tamano; j++ )
#         cout << setw( 3 ) << j << ' ';
#         cout << '\n';  // comienza nueva línea de salida
#       // despliega línea de caracteres -
#       for ( int k = 1; k <= 4 * tamano; k++ )
#         cout << '-';
#         cout << endl;  // comienza nueva línea de salida
#    } // fin de la función despliegaEncabezado
#    // imprime despliega una fila de salida resultados que muestra la paerte 
#    // actual del arreglo que está en proceso
#    void despliegaFila( const int b[], int bajo, int cen, int alto, int tamano )
#    {
#    // repite a través de todo el arreglo 
#       for ( int m = 0; m < tamano; m++ )
#       // despliega espacios si se encuentra fuera del rango del subarreglo
#       if ( m < bajo || m > alto )
#            cout << "    ";
#       // despliega el elemento central marcado con un *
#       else 
#       if ( m == cen )           // marca el elemento central
#           cout << setw( 3 ) << b[ m ] << '*';  
#      // despliega otros elementos del subarreglo
#       else
#        cout << setw( 3 ) << b[ m ] << ' ';
#    	cout << endl;  // comienza nueva línea de salida
#    } // 	 fin de la función despliegaFila
#    

# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================

def start():
    TANANO_ARREGLO = 15
    a = []
    for i in range(0,TANANO_ARREGLO):
        a.append(0)
    for i in range(0,TANANO_ARREGLO):
        a[i]= 2*i
    clave = int(input("Introduzca numero entre 0 y 28 : "))
    despliega_encabezado(TANANO_ARREGLO)
    resultado= busqueda_binaria(a, clave, 0, TANANO_ARREGLO-1, TANANO_ARREGLO)
    if resultado != -1:
        print("\n {} se encuentra en el elemento del arreglo {} \n".format(clave, resultado))
    else :
        print("\n {} no se encuentró".format(clave))
        
def despliega_encabezado(TANANO_ARREGLO):
    
    print("************************\n \t\tSUBINDICES \n************************\n")
    for j in range(0, TANANO_ARREGLO):
        print("{}".ljust(5,).format(j), end= "")
    print("")
    for k in range(1,4*TANANO_ARREGLO+4):
        print("-", end ="")
    print("")
        
def despliega_fila(a, bajo, central, alto, TANANO_ARREGLO ):
    for m in range(0,TANANO_ARREGLO):
        if m < bajo or m > alto:
            print("", end= "")
        else :
            if m == central :
                print("{}*".ljust(5,).format(a[m]), end= "")
            else:
                print("{}".ljust(5,).format(a[m]), end= "")
    print("")
                          
        
def busqueda_binaria(a, clave, bajo, alto, TANANO_ARREGLO):
    central = 0
    while bajo <= alto:
        central = int((bajo+alto)/2)
        despliega_fila(a, bajo, central, alto, TANANO_ARREGLO )
        if clave == a[central]:
            return central
        else :
            if clave < a[central]:
                alto = central -1
            else :
                bajo = central +1
    
    return -1


if __name__ == '__main__' :
    start()
    

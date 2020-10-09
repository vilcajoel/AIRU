# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:02:33 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================
# SETW(): agrega espacios vacios recibe como parametro un entero 
# =============================================================================
#    // Análisis de encuestas.media,mediana y moda de datos.
#    #include <iostream>
#    using std::fixed;
#    using std::showpoint;
#    #include <iomanip>
#    using namespace std;
#    void media( const int [], int );
#    void mediana( int [], int );
#    void moda( int [], int [], int );
#    void ordenaBurbuja( int[], int );
#    void despliegaArreglo( const int[], int );

#    int main()
#    {
#       const int tamanoRespuestas = 99;  // tamaño del arreglo respuestas
#       int frecuencia[ 10 ] = { 0 };  // inicializa el arreglo frecuencia
#    	   // inicializa el arreglo respuestas
#       int respuestas[ tamanoRespuestas ] =  
#    	          { 6, 7, 8, 9, 8, 7, 8, 9, 8, 9,
#    	            7, 8, 9, 5, 9, 8, 7, 8, 7, 8,
#    	            6, 7, 8, 9, 3, 9, 8, 7, 8, 7,
#    	            7, 8, 9, 8, 9, 8, 9, 7, 8, 9,
#    	            6, 7, 8, 7, 8, 7, 9, 8, 9, 2,
#    	            7, 8, 9, 8, 9, 8, 9, 7, 5, 3,
#    	            5, 6, 7, 2, 5, 3, 9, 4, 6, 4,
#    	            7, 8, 9, 6, 8, 7, 8, 9, 7, 8,
#    	            7, 4, 4, 2, 5, 3, 8, 7, 5, 6,
#    	            4, 5, 6, 1, 6, 5, 7, 8, 7 };
#    
#    	   // procesa las respuestas
#       media( respuestas, tamanoRespuestas );
#       mediana( respuestas, tamanoRespuestas );
#       moda( frecuencia, respuestas, tamanoRespuestas );
#       return 0;  // indica terminación exitosa
#    } // fin de main

#    // calcula el promedio de todos los valores correspondientes a las respuestas
#    void media( const int resp[], int tamanoArreglo )
#    {
#       int total = 0;
#       cout << "********\n  Media\n********\n";
#       // total del valor de las respuestas
#       for ( int i = 0; i < tamanoArreglo; i++ )
#          total += resp[ i ];
#       // da formato y despliega los resultados
#       cout << fixed << setprecision( 4 );
#       cout << "La media es el valor promedio de los elementos\n"
#            << "de datos. La media es igual al total de todos \n"
#            << "los elementos de datos divididos entre el numero\n"
#            << "de elementos de datos (" << tamanoArreglo
#            << "). El valor de la media para \nesta ejecución es: " 
#            << total << " / " << tamanoArreglo << " = "
#            << static_cast< double >( total ) / tamanoArreglo 
#            << "\n\n";
#    } // fin de la función media

#    // ordena el arreglo y determina el valor de la mediana de los elementos
#    void mediana( int resp[], int tamano )
#    {
#       cout << "\n********\n Mediana\n********\n"
#            << "El arreglo desordenado de respuestas es";
#    	   despliegaArreglo( resp, tamano );  // muestra el arreglo desordenado
#    	   ordenaBurbuja( resp, tamano );  // ordena el arreglo
#    	   cout << "\n\nEl arreglo ordenado es";
#    	   despliegaArreglo( resp, tamano );  // muestra el arreglo ordenado 
#       // displiega la mediana
#       cout << "\n\nLa mediana es el elemento " << tamano / 2
#            << " del\narreglo ordenado de " << tamano 
#            << " elementos.\nPara esta ejecucion la mediana es "
#            << resp[ tamano / 2 ] << "\n\n";
#    } // fin de la función mediana

#    // determina la respuesta más frecuente
#    void moda( int frec[], int resp[], int tamano )
#    {
#       int masGrande = 0;    // representa la frecueancia más grande
#       int valorModa = 0;  // representa la respuesta más frecuente
#       cout << "\n********\n  Moda\n********\n";
#       // inicializa las frecuencias en 0
#       for ( int i = 1; i <= 9; i++ )
#          frec[ i ] = 0;
#       // resume las frecuencias
#       for ( int j = 0; j < tamano; j++ )
#          ++frec[ resp[ j ] ];
#       // muestra los encabezados para las columnas de resultados
#       cout << "Respuestas" << setw( 11 ) << "Frecuencia"
#            << setw( 19 ) << "Histograma\n\n" << setw( 55 );
#       // despliega resultados
#       for ( int rating = 1; rating <= 9; rating++ ) 
#       {
#          cout << setw( 8 ) << rating << setw( 11 )
#               << frec[ rating ] << "          ";
#        // da seguimiento al valor de la moda y al valor de la frecuencia más grande
#          if ( frec[ rating ] > masGrande ) 
#    	  {
#    	        masGrande = frec[ rating ];
#    	        valorModa = rating;
#    	  } // fin de if
#        // muestra las barras del histograma que representa los valores de frecuencia
#          for ( int k = 1; k <= frec[ rating ]; k++ )
#             cout << '*';
#             cout << '\n';  // comienza una nueva línea de salida
#       } // fin del for externo
#       // despliega el valor de la moda
#       cout << "La moda es el valor mas frecuente.\n"
#            << "Para esta ejecucion la moda es " << valorModa
#            << " la cual tiene una ocurrencia de " << masGrande << " veces." << endl;
#    } // fin de la función moda

#    // función que ordena el arreglo  mediante el algoritmo del método de la burbuja 
#    void ordenaBurbuja( int a[], int tamano )
#    {
#       int mantiene;  // ubicación temporal utilizada para intercambiar elementos
#       // ciclo para controlar el número de pasadas
#       for ( int pasada = 1; pasada < tamano; pasada++ )
#       // ciclo para controlar el número de comparaciones por pasada
#           for ( int j = 0; j < tamano - 1; j++ )
#             // intercambia elementos desordenados
#    	         if ( a[ j ] > a[ j + 1 ] ) 
#    			 {
#    	            mantiene = a[ j ];
#    	            a[ j ] = a[ j + 1 ];
#    	            a[ j + 1 ] = mantiene;
#    	         } // fin de if
#    
#    } // fin de la función ordenaBurbuja

#    // muestra el contenido del arreglo  (20 valores por fila)
#    void despliegaArreglo( const int a[], int tamano )
#    {
#       for ( int i = 0; i < tamano; i++ ) 
#       {
#          if ( i % 20 == 0 )  // comienza una nueva línea cada 20 valores
#             cout << endl;
#             cout << setw( 2 ) << a[ i ];
#       } // fin de for
#    
#    } // fin de la función despliegaArreglo
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================
# # str.LJUST(X,) : agrega X espacios vacios a la cadena que tiene a la izquierda
# =============================================================================

def despliega_arreglo(respuesta):
    for i in range(0,len(respuesta)):
        if i % 20 == 0 :
            print("")
        print("{}".ljust(5,).format(respuesta[i]), end = "")
 
    
def ordena_burbuja(respuesta):
    mantiene = 0
    for i in range(1,len(respuesta)):
        for j in range(0,len(respuesta)-1):
            if respuesta[j]> respuesta[j+1]:
                mantiene = respuesta[j]
                respuesta[j] = respuesta[j+1]
                respuesta[j+1] = mantiene
    print("")
                

def media(respuesta):   
    total = 0
    print("************************\n \t\tMEDIA \n************************\n")
    total = sum(respuesta)
    print("La media es el valor promedio de los elementos\n"+
          "de datos. La media es igual al total de todos\n"+
          "los elementos de datos divididos entre el numero\n"+
          "de elementos de datos.\nEl valor de la media para esta ejecución es : {} / {} = {:.4} \n\n".format(total,len(respuesta),total/len(respuesta)))


def mediana(respuesta):
    print("************************\n \t\tMEDIANA \n************************\n")
    print("El arreglo desordenado de respuestas es :")
    despliega_arreglo(respuesta)
    ordena_burbuja(respuesta)
    print("\nEl arreglo ordenado de respuestas es :")
    despliega_arreglo(respuesta)
    print("\n\nLa mediana es el elemento {} del\narreglo ordenado de {} elementos.\nPara esta ejecución la mediana es {}".format(int(len(respuesta)/2),len(respuesta),respuesta[int(len(respuesta)/2)]))
    print("")

def moda(frecuencia, respuesta):
    mas_grande = 0
    valor_moda = 0
    print("************************\n \t\tMODA \n************************\n")
    for i in range(1,11):
        frecuencia.append(0)
    for j in range(0,len(respuesta)):
        frecuencia[respuesta[j]]=frecuencia[respuesta[j]]+1
    print("RESPUESTA".ljust(20,)+"FRECUENCIA".ljust(20,)+"HISTOGRAMA")
    for r in range(1,10):
        print("")
        n=25
        if r==7 or r==8 or r==9: #arregla identacion de histograma
            n=24
            
        print("    {}".ljust(20,).format(r)+ "       {} ".ljust(n,).format(frecuencia[r]), end="")
        if frecuencia[r]>mas_grande:
            mas_grande= frecuencia[r]
            valor_moda= r
        for k in range(1,frecuencia[r]+1):
            print("*", end="")
            
    print("\n\nLa moda es el valor mas frecuente.\n"+
          "Para esta ejecución la moda es {} ".format(valor_moda)+
          "la cual tiene una ocurrencia de {} veces.".format(mas_grande))
    

#       for ( int rating = 1; rating <= 9; rating++ ) 
#       {
#          cout << setw( 8 ) << rating << setw( 11 )
#               << frec[ rating ] << "          ";
#        // da seguimiento al valor de la moda y al valor de la frecuencia más grande
        
        
#          if ( frec[ rating ] > masGrande ) 
#    	  {
#    	        masGrande = frec[ rating ];
#    	        valorModa = rating;
#    	  } // fin de if
#        // muestra las barras del histograma que representa los valores de frecuencia
#          for ( int k = 1; k <= frec[ rating ]; k++ )
#             cout << '*';
#             cout << '\n';  // comienza una nueva línea de salida
#       } // fin del for externo
#       // despliega el valor de la moda
#       cout << "La moda es el valor mas frecuente.\n"
#            << "Para esta ejecucion la moda es " << valorModa
#            << " la cual tiene una ocurrencia de " << masGrande << " veces." << endl;
#    } // fin de la función moda

def start():
    frecuencia = []
    respuesta = [
                6, 7, 8, 9, 8, 7, 8, 9, 8, 9,
	            7, 8, 9, 5, 9, 8, 7, 8, 7, 8,
	            6, 7, 8, 9, 3, 9, 8, 7, 8, 7,
	            7, 8, 9, 8, 9, 8, 9, 7, 8, 9,
	            6, 7, 8, 7, 8, 7, 9, 8, 9, 2,
	            7, 8, 9, 8, 9, 8, 9, 7, 5, 3,
	            5, 6, 7, 2, 5, 3, 9, 4, 6, 4,
	            7, 8, 9, 6, 8, 7, 8, 9, 7, 8,
	            7, 4, 4, 2, 5, 3, 8, 7, 5, 6,
	            4, 5, 6, 1, 6, 5, 7, 8, 7 
                ]
    media(respuesta)
    mediana(respuesta)
    moda(frecuencia, respuesta)

if __name__ == '__main__':
    start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
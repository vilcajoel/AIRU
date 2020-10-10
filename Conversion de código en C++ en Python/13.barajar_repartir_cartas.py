# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:27:48 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================

#    // Programa para barajar y repartir cartas.
#    #include <iostream>
#    using std::cout;
#    using std::left;
#    using std::right;
#    #include <iomanip>
#    using std::setw;
#    #include <cstdlib>  // prototipos para rand y srand
#    #include <ctime>    // prototipos para time
#    // prototipos
#    void barajar( int [][ 13 ] );
#    void repartir( const int [][ 13 ], const char *[], const char *[] );
#    int main()
#    {
#       // inicializa el arreglo palo
#       const char *palo[ 4 ] =  
#          { "Corazones", "Diamantes", "Treboles", "Espadas" };
#       // inicializa el arreglo cara
#       const char *cara[ 13 ] = 
#          { "As", "Dos", "Tres", "Cuatro",
#            "Cinco", "Seis", "Siete", "Ocho",
#            "Nueve", "Diez", "Joto", "Quina", "Rey" };
#       // inicializa arreglo baraja
#       int baraja[ 4 ][ 13 ] = { 0 };
#       srand( time( 0 ) );        // semilla del generador de números aleatorios
#       barajar( baraja );
#       repartir( baraja, cara, palo );
#       return 0;  // indica terminación exitosa
#    } // fin de main
#    // baraja las cartas
#    void barajar( int wBaraja[][ 13 ] )
#    {
#       int fila;
#       int columna;
#       // para cada una de las 52 cartas, elige la posición de la baraja al azar
#       for ( int carta = 1; carta <= 52; carta++ ) {
#          // elije nueva ubicación al azar hasta encontrar una posición desocupada
#          do {
#             fila = rand() % 4;
#             columna = rand() % 13;
#          } while( wBaraja[ fila ][ columna ] != 0 ); // fin de do/while
#          // coloca el número de la carta en la posición elegida de la baraja
#          wBaraja[ fila ][ columna ] = carta;
#       } // fin del for
#    } // fin de la función barajar
#    // reparte las cartas de la baraja
#    void repartir( const int wBaraja[][ 13 ], const char *wCara[],
#               const char *wPalo[] )
#    {
#       // para cada una de las 52 cartas
#       for ( int carta = 1; carta <= 52; carta++ )
#          // ciclo a través de las filas en wBaraja
#          for ( int fila = 0; fila <= 3; fila++ )
#             // ciclo a través de las columnas de wBaraja para la fila actual
#             for ( int columna = 0; columna <= 12; columna++ )
#                // si wBaraja contiene la carta actual, despliega la carta
#                if ( wBaraja[ fila ][ columna ] == carta ) 
#    			{
#                   cout << setw( 6 ) << right << wCara[ columna ] 
#                        << " de " << setw( 9 ) << left 
#                        << wPalo[ fila ]
#                        << ( carta % 2 == 0 ? '\n' : '\t' );
#    
#                } // fin de if
#    
#    } // fin de la función repartir
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================

def start():    
    import itertools, random   
    baraja = list(itertools.product(range(1,14),['Espadas','Corazones','Diamantes','Treboles']))   
    random.shuffle(baraja)
    print("************************\n \tCartas barajeadas \n************************\n")
    for i in range(26):
       print(baraja[i][0], "de", baraja[i][1], end ="")
       print("\t", end= "")
       print(baraja[i+1][0], "de", baraja[i][1])

       
if __name__== '__main__':
    start()
















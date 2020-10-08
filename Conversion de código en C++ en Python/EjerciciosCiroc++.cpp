//------------------- 26 -------------------
//				ALEATORIOS
//------------------- 26 -------------------

//------------------- 26 -------------------

//Numero aleatorio estatico
#include <iostream>
#include <iomanip>
#include <cstdlib>   
using namespace std;
int main()
{
   for ( int contador = 1; contador <= 20; contador++ ) 
   {
      cout<< setw( 10 ) << ( 1 + rand() % 6 ); 
      if ( contador % 5 == 0 )
         cout << endl;
   } 
   return 0;  
} 

////------------------- 27 -------------------
//#include <iostream.h>
//#include <iomanip.h>
//#include <cstdlib>   
//int main()
//{
//   int frecuencia1 = 0;
//   int frecuencia2 = 0;
//   int frecuencia3 = 0; 
//   int frecuencia4 = 0;
//   int frecuencia5 = 0; 
//   int frecuencia6 = 0;
//   int cara;  
//   for ( int tiro = 1; tiro <= 6000; tiro++ ) 
//   {
//      cara = 1 + rand() % 6; 
//      switch ( cara ) {
//         case 1:  
//            ++frecuencia1;
//            break;
//         case 2:  
//            ++frecuencia2;
//            break;
//         case 3:  
//            ++frecuencia3;
//            break;
//         case 4:  
//            ++frecuencia4;
//            break;
//         case 5:  
//            ++frecuencia5;
//            break;
//         case 6:  
//            ++frecuencia6;
//            break;
//         default: 
//            cout << "¡El programa no debe llegar hasta aquí!";
//      } 
//   } 
//   cout << "Cara" << setw( 13 ) << "Frecuencia"
//        << "\n   1" << setw( 13 ) << frecuencia1
//        << "\n   2" << setw( 13 ) << frecuencia2
//        << "\n   3" << setw( 13 ) << frecuencia3
//        << "\n   4" << setw( 13 ) << frecuencia4
//        << "\n   5" << setw( 13 ) << frecuencia5
//        << "\n   6" << setw( 13 ) << frecuencia6 << endl;
//   return 0; 
//} 
//------------------- 28 -------------------
//#include <iostream.h>
//#include <iomanip.h>
//#include <cstdlib>// contiene srand y rand
//int main()
//{
//   unsigned semilla;
//   cout << "Introduzca semilla: ";
//   cin >> semilla;
//   srand( semilla );  
//   for ( int contador = 1; contador <= 10; contador++ ) 
//   {
//         cout << setw( 10 ) << ( 1 + rand() % 6 );
//      if ( contador % 5 == 0 )
//         cout << endl;
//   } 
//   return 0;  
//} 
//------------------- 29 -------------------
//#include <iostream.h>
//#include <cstdlib>
//#include <ctime>   // contiene prototipo de función time
//int tiraDados( void );  // prototipo de la función
//int main()
//{
//   enum Status { CONTINUA, GANA, PIERDE };
//   int suma;
//   int miPunto;
//   Status estadoJuego;  // CONTINUA, GANA o PIERDE
//   
//   srand( time( 0 ) ); // randomiza números mediante time
//   suma = tiraDados(); // primer tiro de dados
//   switch ( suma ) 
//   {
//      case 7: 
//	   case 11:            
//         estadoJuego = GANA;
//         break;
//      case 2: 
//	   case 3: 
//	   case 12:             
//         estadoJuego = PIERDE;
//         break;
//      default:            
//         estadoJuego = CONTINUA;
//         miPunto = suma;
//         cout << "El punto es " << miPunto << endl;
//         break;                // opcional   
//
//   }  
//   while ( estadoJuego == CONTINUA ) 
//   { 
//      suma = tiraDados();  // tira dados nuevamente
//      if ( suma == miPunto )       // gana por puntos
//         estadoJuego = GANA;
//      else
//         if ( suma == 7 )          // pierde por obtener 7
//            estadoJuego = PIERDE;
//
//   } 
//   if ( estadoJuego == GANA )
//      cout << "El jugador gana" << endl;
//   else
//      cout << "El jugador pierde" << endl;
//   return 0;  
//} 
//int tiraDados( void )
//{
//   int dado1;
//   int dado2;
//   int sumaTrabajo;
//   dado1 = 1 + rand() % 6;  // aleatorio del dado1
//   dado2 = 1 + rand() % 6;  // aleatorio del dado2
//   sumaTrabajo = dado1 + dado2;  
//   cout << "El jugador tiro " << dado1 << " + " << dado2
//        << " = " << sumaTrabajo << endl;
//   return sumaTrabajo;         // devuelve suma de los dados
//} 
//------------------- 31 -------------------
//#include <iostream.h>
//#include <iomanip.h>
//unsigned long factorial( unsigned long ); // prototipo de la función
//int main()
//{
//   for ( int i = 0; i <= 10; i++ )
//      cout << setw( 2 ) << i << "! = " 
//           << factorial( i ) << endl;
//
//   return 0;  // indica terminació exitosa
//}
//unsigned long factorial( unsigned long numero )
//{
//   if ( numero <= 1 )  
//      return 1;
//   else                
//      return numero * factorial( numero - 1 );
//}
//------------------- 32 -------------------
//#include <iostream.h>
//unsigned long fibonacci( unsigned long ); 
//int main()
//{
//   unsigned long resultado, numero;
//   cout << "Introduzca un entero: ";
//   cin >> numero;
//   resultado = fibonacci( numero );
//   cout << "Fibonacci(" << numero << ") = " << resultado << endl;
//   return 0;  
//} 
//unsigned long fibonacci( unsigned long n )
//{
//   if ( n == 0 || n == 1 )  
//      return n;
//   else             
//      return fibonacci( n - 1 ) + fibonacci( n - 2 );
//} 
//------------------- 33 -------------------
//#include <iostream.h>
//#include <iomanip.h>
//int main()
//{
//   const int tamanoArreglo = 10;
//   int n[ tamanoArreglo ] = { 19, 3, 15, 7, 11, 9, 13, 5, 17, 1 };
//   cout << "Elemento" << setw( 13 ) << "Valor"
//        << setw( 17 ) << "Histograma" << endl;
//   for ( int i = 0; i < tamanoArreglo; i++ ) 
//   {
//      cout << setw( 7 ) << i << setw( 13 ) 
//           << n[ i ] << setw( 9 );
//      for ( int j = 0; j < n[ i ]; j++ )   
//         cout << '*';
//      cout << endl;  
//   } 
//   return 0;  
//} 
//------------------- 52 -------------------
//// Tiro de un dado de seis lados 6000 veces
//#include <iostream.h>
//#include <iomanip.h>
//#include <cstdlib>
//#include <ctime>
//int main()
//{
//   const int tamanoArreglo = 7;
//   int frecuencia[ tamanoArreglo ] = { 0 };
//   srand( time( 0 ) );  
//   // tira los dados 6000 veces
//   for ( int tiro = 1; tiro <= 6000; tiro++ )       
//      ++frecuencia[ 1 + rand() % 6 ]; 
//   cout << "Cara" << setw( 13 ) << "Frecuencia" << endl;
//   // muestra la frecuencia de los elementos 1 a 6 en formato tabular
//   for ( int cara = 1; cara < tamanoArreglo; cara++ )  
//      cout << setw( 4 ) << cara
//           << setw( 13 ) << frecuencia[ cara ] << endl;
//   return 0;  
//} 
//------------------- 52 -------------------
//// Análisis de encuestas.media,mediana y moda de datos.
//#include <iostream>
//using std::fixed;
//using std::showpoint;
//#include <iomanip.h>
//void media( const int [], int );
//void mediana( int [], int );
//void moda( int [], int [], int );
//void ordenaBurbuja( int[], int );
//void despliegaArreglo( const int[], int );
//int main()
//{
//   const int tamanoRespuestas = 99;  // tamaño del arreglo respuestas
//   int frecuencia[ 10 ] = { 0 };  // inicializa el arreglo frecuencia
//	   // inicializa el arreglo respuestas
//   int respuestas[ tamanoRespuestas ] =  
//	          { 6, 7, 8, 9, 8, 7, 8, 9, 8, 9,
//	            7, 8, 9, 5, 9, 8, 7, 8, 7, 8,
//	            6, 7, 8, 9, 3, 9, 8, 7, 8, 7,
//	            7, 8, 9, 8, 9, 8, 9, 7, 8, 9,
//	            6, 7, 8, 7, 8, 7, 9, 8, 9, 2,
//	            7, 8, 9, 8, 9, 8, 9, 7, 5, 3,
//	            5, 6, 7, 2, 5, 3, 9, 4, 6, 4,
//	            7, 8, 9, 6, 8, 7, 8, 9, 7, 8,
//	            7, 4, 4, 2, 5, 3, 8, 7, 5, 6,
//	            4, 5, 6, 1, 6, 5, 7, 8, 7 };
//
//	   // procesa las respuestas
//   media( respuestas, tamanoRespuestas );
//   mediana( respuestas, tamanoRespuestas );
//   moda( frecuencia, respuestas, tamanoRespuestas );
//   return 0;  // indica terminación exitosa
//} // fin de main
//// calcula el promedio de todos los valores correspondientes a las respuestas
//void media( const int resp[], int tamanoArreglo )
//{
//   int total = 0;
//   cout << "********\n  Media\n********\n";
//   // total del valor de las respuestas
//   for ( int i = 0; i < tamanoArreglo; i++ )
//      total += resp[ i ];
//   // da formato y despliega los resultados
//   cout << fixed << setprecision( 4 );
//   cout << "La media es el valor promedio de los elementos\n"
//        << "de datos. La media es igual al total de todos \n"
//        << "los elementos de datos divididos entre el numero\n"
//        << "de elementos de datos (" << tamanoArreglo
//        << "). El valor de la media para \nesta ejecución es: " 
//        << total << " / " << tamanoArreglo << " = "
//        << static_cast< double >( total ) / tamanoArreglo 
//        << "\n\n";
//} // fin de la función media
//// ordena el arreglo y determina el valor de la mediana de los elementos
//void mediana( int resp[], int tamano )
//{
//   cout << "\n********\n Mediana\n********\n"
//        << "El arreglo desordenado de respuestas es";
//	   despliegaArreglo( resp, tamano );  // muestra el arreglo desordenado
//	   ordenaBurbuja( resp, tamano );  // ordena el arreglo
//	   cout << "\n\nEl arreglo ordenado es";
//	   despliegaArreglo( resp, tamano );  // muestra el arreglo ordenado 
//   // displiega la mediana
//   cout << "\n\nLa mediana es el elemento " << tamano / 2
//        << " del\narreglo ordenado de " << tamano 
//        << " elementos.\nPara esta ejecucion la mediana es "
//        << resp[ tamano / 2 ] << "\n\n";
//} // fin de la función mediana
//// determina la respuesta más frecuente
//void moda( int frec[], int resp[], int tamano )
//{
//   int masGrande = 0;    // representa la frecueancia más grande
//   int valorModa = 0;  // representa la respuesta más frecuente
//   cout << "\n********\n  Moda\n********\n";
//   // inicializa las frecuencias en 0
//   for ( int i = 1; i <= 9; i++ )
//      frec[ i ] = 0;
//   // resume las frecuencias
//   for ( int j = 0; j < tamano; j++ )
//      ++frec[ resp[ j ] ];
//   // muestra los encabezados para las columnas de resultados
//   cout << "Respuestas" << setw( 11 ) << "Frecuencia"
//        << setw( 19 ) << "Histograma\n\n" << setw( 55 )
//        << "1    1    2    2\n" << setw( 56 )
//        << "5    0    5    0    5\n\n";
//   // despliega resultados
//   for ( int rating = 1; rating <= 9; rating++ ) 
//   {
//      cout << setw( 8 ) << rating << setw( 11 )
//           << frec[ rating ] << "          ";
//    // da seguimiento al valor de la moda y al valor de la frecuencia más grande
//      if ( frec[ rating ] > masGrande ) 
//	  {
//	        masGrande = frec[ rating ];
//	        valorModa = rating;
//	  } // fin de if
//    // muestra las barras del histograma que representa los valores de frecuencia
//      for ( int k = 1; k <= frec[ rating ]; k++ )
//         cout << '*';
//         cout << '\n';  // comienza una nueva línea de salida
//   } // fin del for externo
//   // despliega el valor de la moda
//   cout << "La moda es el valor mas frecuente.\n"
//        << "Para esta ejecucion la moda es " << valorModa
//        << " la cual tiene una ocurrencia de " << masGrande << " veces." << endl;
//} // fin de la función moda
//// función que ordena el arreglo  mediante el algoritmo del método de la burbuja 
//void ordenaBurbuja( int a[], int tamano )
//{
//   int mantiene;  // ubicación temporal utilizada para intercambiar elementos
//   // ciclo para controlar el número de pasadas
//   for ( int pasada = 1; pasada < tamano; pasada++ )
//   // ciclo para controlar el número de comparaciones por pasada
//       for ( int j = 0; j < tamano - 1; j++ )
//         // intercambia elementos desordenados
//	         if ( a[ j ] > a[ j + 1 ] ) 
//			 {
//	            mantiene = a[ j ];
//	            a[ j ] = a[ j + 1 ];
//	            a[ j + 1 ] = mantiene;
//	         } // fin de if
//
//} // fin de la función ordenaBurbuja
//// muestra el contenido del arreglo  (20 valores por fila)
//void despliegaArreglo( const int a[], int tamano )
//{
//   for ( int i = 0; i < tamano; i++ ) 
//   {
//      if ( i % 20 == 0 )  // comienza una nueva línea cada 20 valores
//         cout << endl;
//         cout << setw( 2 ) << a[ i ];
//   } // fin de for
//
//} // fin de la función despliegaArreglo
//------------------- 60 -------------------
//// Búsqueda lineal en un arreglo.
//#include <iostream>
//using std::cout;
//using std::cin;
//using std::endl;
//int busquedaLineal( const int [], int, int );  // prototipo
//int main()
//{
//   const int tamanoArreglo = 100;  // tamaño del arreglo a
//   int a[ tamanoArreglo ];         // crea el arreglo a
//   int claveBusqueda;              // valor a localizar dentro de a
//   for ( int i = 0; i < tamanoArreglo; i++ )  // crea algunos datos
//      a[ i ] = 2 * i;
//      cout << "Introduce la clave de busqueda entera: ";
//      cin >> claveBusqueda;
//  // intenta localizar claveBusqueda dentro del arreglo a
//   int elemento = busquedaLineal( a, claveBusqueda, tamanoArreglo );
// // despliega los resultados
//   if ( elemento != -1 )
//      cout << "Encontre valor en el elemento " << elemento << endl;
//   else
//      cout << "Valor no encontrado" << endl;
//   return 0;  // indica terminación exitosa
//} // fin de main
//// compara la clave con cada elemento del arreglo hasta encontrar su 
//// ubicación o hasta que se alcanza el final del arreglo; devuelve el subíndice 
//// del elemento si es la clave o -1 si ésta no se encontró
//int busquedaLineal( const int arreglo[], int clave, int tamanoDelArreglo )
//{
//   for ( int j = 0; j < tamanoDelArreglo; j++ )
//      if ( arreglo[ j ] == clave )  // si se encuentra ,
//         return j;              // devuelve la ubicación de la clave
//   return -1;  // la clave no se encontró
//} // fin de la función busquedaLineal
//
//------------------- 61 -------------------
//// Búsqueda binaria dentro de un arreglo.
//#include <iostream>
//using std::cout;
//using std::cin;
//using std::endl;
//#include <iomanip>
//using std::setw;
//// prototipo de la función
//int busquedaBinaria( const int [], int, int, int, int );
//void despliegaEncabezado( int );
//void despliegaFila( const int [], int, int, int, int );
//int main()
//{
//   const int tamanoArreglo = 15;  // tamaño del arreglo a
//   int a[ tamanoArreglo ];        // crea el arreglo a
//   int clave;                   // valor a localizar en a
//   for ( int i = 0; i < tamanoArreglo; i++ )  // crea algunos datos
//      a[ i ] = 2 * i;   
//   cout << "Introduzca un numero entre 0 y 28: ";
//   cin >> clave;
//   despliegaEncabezado( tamanoArreglo );
//   // búsqueda de la clave en el arreglo a
//   int resultado = 
//	      busquedaBinaria( a, clave, 0, tamanoArreglo - 1, tamanoArreglo );
//   // despliega resultados
//   if ( resultado != -1 )
//     cout << '\n' << clave << " se encuentra en el elemento del arreglo "
//          << resultado << endl;
//   else
//     cout << '\n' << clave << " no se encontro" << endl;
//   return 0;  // indica terminación exitosa
//} // fin de main
//// función para realizar la búsqueda binaria dentro de un arreglo
//int busquedaBinaria( const int b[], int claveBusqueda, int bajo, int alto, int tamano )
//{
//int central;
//// repetición hasta que el subíndice bajo sea mayor que el subíndice alto
//   while ( bajo <= alto )
//   {
//     // determina el elemento central del subarreglo en el que se busca
//      central = ( bajo + alto ) / 2;  
//     // despliega el subarreglo utilizado en este ciclo de la iteración
//      despliegaFila( b, bajo, central, alto, tamano );
//    // si claveBusqueda coincide con el elemento central, devuelve el elemento central
//     if ( claveBusqueda == b[ central ] )  // coincide
//        return central;
//     else 
//        // si claveBusqueda es menor que el elemento central, 
//        // establece el nuevo elemento alto
//         if ( claveBusqueda < b[ central ] )
//            alto = central - 1;  // busca bajo hasta el final del arreglo
//         // si claveBusqueda es mayor que el elemento central, 
//         // establece el nuevo elemento bajo
//         else
//            bajo = central + 1;   // busca bajo hasta el final del arreglo
//   }
//  return -1;  // no se encontró claveBusqueda
//} // fin de la función busquedaBinaria
//// despliega el encabezado de salida
//void despliegaEncabezado( int tamano )
//{
//   cout << "\nSubindices:\n";
//   // muestra encabezados de columnas
//   for ( int j = 0; j < tamano; j++ )
//     cout << setw( 3 ) << j << ' ';
//     cout << '\n';  // comienza nueva línea de salida
//   // despliega línea de caracteres -
//   for ( int k = 1; k <= 4 * tamano; k++ )
//     cout << '-';
//     cout << endl;  // comienza nueva línea de salida
//} // fin de la función despliegaEncabezado
//// imprime despliega una fila de salida resultados que muestra la paerte 
//// actual del arreglo que está en proceso
//void despliegaFila( const int b[], int bajo, int cen, int alto, int tamano )
//{
//// repite a través de todo el arreglo 
//   for ( int m = 0; m < tamano; m++ )
//   // despliega espacios si se encuentra fuera del rango del subarreglo
//   if ( m < bajo || m > alto )
//        cout << "    ";
//   // despliega el elemento central marcado con un *
//   else 
//   if ( m == cen )           // marca el elemento central
//       cout << setw( 3 ) << b[ m ] << '*';  
//  // despliega otros elementos del subarreglo
//   else
//    cout << setw( 3 ) << b[ m ] << ' ';
//	cout << endl;  // comienza nueva línea de salida
//} // 	 fin de la función despliegaFila
//
//
//
//
//------------------- 26 -------------------
//PERMUTACIONES
//------------------- 26 -------------------
//
//------------------- 26 -------------------
////Realiza todas las permutaciones posibles de las letras de la palabra ABCDE
//#include <iostream.h> 
//#include <string.h> 
//void Permutaciones(char *, int l=0); 
//
//int main(int argc, char *argv[])
//{
//   char palabra[] = "ABCDE";
//   Permutaciones(palabra);
//   return 0;
//}
//void Permutaciones(char * cad, int l)
//{
//   char c;    /* variable auxiliar para intercambio */
//   int i, j;  /* variables para bucles */
//   int n = strlen(cad);
//
//   for(i = 0; i < n-l; i++)
//   {
//      if(n-l > 2) Permutaciones(cad, l+1);
//      else cout <<cad << ", ";
//      /* Intercambio de posiciones */
//      c = cad[l];
//      cad[l] = cad[l+i+1];
//      cad[l+i+1] = c;
//      if(l+i == n-1)
//      {
//         for(j = l; j < n; j++) cad[j] = cad[j+1];
//         cad[n] = 0;
//      }
//   }
//}
//
//------------------- PERMUTACIONES-------------------
//
//
//------------------- 26 -------------------
//
//// Programa para barajar y repartir cartas.
//#include <iostream>
//using std::cout;
//using std::left;
//using std::right;
//#include <iomanip>
//using std::setw;
//#include <cstdlib>  // prototipos para rand y srand
//#include <ctime>    // prototipos para time
//// prototipos
//void barajar( int [][ 13 ] );
//void repartir( const int [][ 13 ], const char *[], const char *[] );
//int main()
//{
//   // inicializa el arreglo palo
//   const char *palo[ 4 ] =  
//      { "Corazones", "Diamantes", "Treboles", "Espadas" };
//   // inicializa el arreglo cara
//   const char *cara[ 13 ] = 
//      { "As", "Dos", "Tres", "Cuatro",
//        "Cinco", "Seis", "Siete", "Ocho",
//        "Nueve", "Diez", "Joto", "Quina", "Rey" };
//   // inicializa arreglo baraja
//   int baraja[ 4 ][ 13 ] = { 0 };
//   srand( time( 0 ) );        // semilla del generador de números aleatorios
//   barajar( baraja );
//   repartir( baraja, cara, palo );
//   return 0;  // indica terminación exitosa
//} // fin de main
//// baraja las cartas
//void barajar( int wBaraja[][ 13 ] )
//{
//   int fila;
//   int columna;
//   // para cada una de las 52 cartas, elige la posición de la baraja al azar
//   for ( int carta = 1; carta <= 52; carta++ ) {
//      // elije nueva ubicación al azar hasta encontrar una posición desocupada
//      do {
//         fila = rand() % 4;
//         columna = rand() % 13;
//      } while( wBaraja[ fila ][ columna ] != 0 ); // fin de do/while
//      // coloca el número de la carta en la posición elegida de la baraja
//      wBaraja[ fila ][ columna ] = carta;
//   } // fin del for
//} // fin de la función barajar
//// reparte las cartas de la baraja
//void repartir( const int wBaraja[][ 13 ], const char *wCara[],
//           const char *wPalo[] )
//{
//   // para cada una de las 52 cartas
//   for ( int carta = 1; carta <= 52; carta++ )
//      // ciclo a través de las filas en wBaraja
//      for ( int fila = 0; fila <= 3; fila++ )
//         // ciclo a través de las columnas de wBaraja para la fila actual
//         for ( int columna = 0; columna <= 12; columna++ )
//            // si wBaraja contiene la carta actual, despliega la carta
//            if ( wBaraja[ fila ][ columna ] == carta ) 
//			{
//               cout << setw( 6 ) << right << wCara[ columna ] 
//                    << " de " << setw( 9 ) << left 
//                    << wPalo[ fila ]
//                    << ( carta % 2 == 0 ? '\n' : '\t' );
//
//            } // fin de if
//
//} // fin de la función repartir
//---
//
//---------------- DERIVADA ---------------
//*************** DERIVADA ***************
//---------------- DERIVADA ---------------
//------------------- DERIVADA -------------------
////				          4	3    2
////Desarrollo de derivadas de la forma ax + bx + cx + dx + e
//#include<iostream.h>
//#include<math.h>
//double primer( double ); 
//double segundo( double); 
//double tercer(double); 
//double cuarto(double ); 
//double quinto(double ); 
//double a,b,c,d,j;
//double l;
//double h,m;
//void main()
//{
//	cout<<"                       4    3    2        "<<endl;
//	cout<<"Derivada de la forma ax + bx + cx + dx + e"<<endl;
//	cout<<"Ingrese valor a: ";
//	cin>>a;
//	cout<<"Ingrese valor b: ";
//	cin>>b;
//	cout<<"Ingrese valor c: ";
//	cin>>c;
//	cout<<"Ingrese valor d: ";
//	cin>>d;
//	cout<<"Ingrese valor e: ";
//	cin>>j;
//	cout<<"Ingrese el valor a derivar: ";
//	cin>>l;
//	h =  primer(a)+  segundo(b)+ tercer(c)+ cuarto(d)+quinto(j);
//	cout<<"Valor de derivada: "<<h<<endl;
//	
//}
//double primer( double a )
//{
//   double s=pow(l,3);
//   double q=(a*s)*4;
//      return q;
//}
//double segundo( double b )
//{
//	double t=pow(l,2); 
//	double r=(b*t)*3;
//      return  r;
//}
//double tercer( double c )
//{
//	double u=pow(l,1);               
//	double p=(c*u)*2;
//      return  p;
//}
//double cuarto( double d )
//{
//   double w=pow(l,0);
//   double v=(d*w)/1;               
//      return  v;
//}
//double quinto( double j )
//{
//   double g=0;
//   double h=(j*g);               
//      return h;
//}
//
//
//---------------- INTEGRALES  ---------------
//*************** INTEGRALES ***************
//---------------- INTEGRALES  ---------------
//------------------- INTEGRALES -------------------
//#include<iostream.h>
//#include<math.h>
//void main ()
//{
//	cout<<endl<<endl;
//	cout<<"       INTEGRALES DEFINIDAS"<<endl;
//		
//	cout<<endl<<endl;	cout<<endl;
//	cout<<"     ___________________________________"<<endl;
//	cout<<"    |     b                             |"<<endl;
//   	cout<<"    |    (                              |"<<endl;
//	cout<<"    |    ) seno(x)coseno(x)dx           | "<<endl;
//	cout<<"    |   a                               | "<<endl;
//	cout<<"    |___________________________________|"<<endl;
//	cout<<endl;	cout<<endl;
//	double  s,a,b,n,i,delta;
//	cout <<"ingrese  n el numero de particiones  =  ";
//	cin>>n;
//	cout <<"ingrese  a el limite inferior  =  ";
//	cin>>a;
//	cout <<"ingrese  b el limite superior  =  ";
//	cin>>b;
//	cout<<endl<<endl;cout<<endl;
//
//		delta = (b-a)/n;
//		s=0;
//
//		for (i=1;i<=n;i++)
//			{
//				s = s + sin(a + delta * i) * cos(a + delta * i) * delta;
//			}
//	cout<<"la integral es :";	cout<<endl<<endl;
//	cout<<"     ___________________________________ "<<endl;
//	cout<<"    |     b                             |"<<endl;
//   	cout<<"    |    (                              |"<<endl;
//	cout<<"    |    ) seno(x)coseno(x)dx           | = "<<s<<endl;
//	cout<<"    |   a                               |"<<endl;
//	cout<<"    |___________________________________|"<<endl;
//	cout<<endl;	cout<<endl;
//}
//------------------- 275 -------------------
////Se desea desarrollar una aplicacion que permita calcular la integral 
////definida de una funcion:   g    g
////                  f(x) = Cx + Cx ......  
////                         --   --
////                         T1   T2
////  C = Coeficientes; g = Grado del Termino; T = Termino; i-n = intervalo de integral
////					
//#include<iostream.h>
//#include<iomanip.h>
//#include<cstdlib>
//#include<math.h>
//
//int main()
//{	
//  float matrizC[20];//Matriz de Coeficiente
//  float matrizg[20];//Matriz de Grado de Termino
//  double y;
//  int n,i,j,x1,x2;
//  cout<<"            Calculo de Integral definida de una funcion"<<endl<<endl;
//  cout<<"		      n    g    g                   "<<endl;
//  cout<<"                  f(x) = Cx + Cx ......  "<<endl;
//  cout<<"                      i  --   --	        "<<endl;
//  cout<<"                         T1   T2			"<<endl<<endl;
//  cout<<"C = Coeficiente; g = Grado de Termino; T = Termino; i-n= intervalo"<<endl<<endl; 
//	cout<<"Ingrese cantidad de terminos (T) para f(x) a Integrar: ";
//	cin>>n;
//	for (i=1;i<=n;i++)
//		{	
//		  cout<<"Ingrese el coeficiente (C) y grado (g) del T"<<i<<": ";
//		  cin>>matrizC[i]>>matrizg[i];
//		}
//	cout<<endl;
//	cout<<"La funcion f(x) definida es : ";
//	for (i=1;i<=n;i++)
//		{
//		 if (i==1)
//		 cout<<matrizC[i]<<"x"<<matrizg[i]<<setw(2);//se muestra funcion definida
//		 else
//		 cout<<" + "<<matrizC[i]<<"x"<<matrizg[i]<<setw(2);
//		}
//	cout<<endl;
//	cout<<"La integral desarrollada es : ";
//	for (i=1;i<=n;i++)
//	    {	
//		 if (i==1)
//		    cout<<matrizC[i]/(matrizg[i]+1)<<"x"<<matrizg[i]+1<<setw(2);
//		 else
//		    cout<<" + "<<matrizC[i]/(matrizg[i]+1)<<"x"<<matrizg[i]+1<<setw(2);
//		}
//	cout<<endl;
//	cout<<"Ingrese el intervalo (i-n) de la integral: ";
//	cin>>x1>>x2;
//	y=0;
//	for (j=x1;j<=x2;j++)
//	    {	
//		 for(i=1;i<=n;i++)
//		    {
//			y = y + matrizC[i] / ( matrizg[i]+1 )*pow( j,matrizg[i]+1 );
//		    }
//	    }
//	cout<<"El calculo de la integral es : "<<y<<endl;
//	return 0;
//}
//
//
//
//------------------- 276 -------------------
////				         4    3    2
////Desarrollo de Integral de la forma ax + bx + cx + dx + e
//#include<iostream.h>
//#include<math.h>
//double primer( double ); 
//double segundo( double); 
//double tercer(double); 
//double cuarto(double ); 
//double quinto(double ); 
//double pri( double ); 
//double segu( double ); 
//double ter(double ); 
//double cuar( double ); 
//double quin(double ); 
//double a,b,c,d,j;
//double l,n;
//double e,f,g,i,k;
//double h,y,m;
//void main()
//{
//	cout<<"                       4    3    2        "<<endl;
//	cout<<"Derivada de la forma ax + bx + cx + dx + e"<<endl;
//	cout<<"Ingrese valor a: ";
//	cin>>a;
//	cout<<"Ingrese valor b: ";
//	cin>>b;
//	cout<<"Ingrese valor c: ";
//	cin>>c;
//	cout<<"Ingrese valor d: ";
//	cin>>d;
//	cout<<"Ingrese valor e: ";
//	cin>>j;
//	cout<<"Intervalo i a integrar: ";
//	cin>>l;
//	cout<<"Intervalo n a integrar: ";
//	cin>>n;
//	h =  primer(a)+  segundo(b)+ tercer(c)+ cuarto(d)+quinto(j);
//	cout<<"Valor final: "<<h<<endl;
//	y =  pri(e)+  segu(f)+ ter(g)+ cuar(i)+quin(k);
//	cout<<"Valor inicial: "<<y<<endl;
//	m = (h-y);
//	cout<<"Valor de integral: "<<m<<endl;
//}
//double primer( double a )
//{
//   double s=pow(n,5);
//   double q=(a*s)/5;
//      return q;
//}
//double segundo( double b )
//{
//	double t=pow(n,4); 
//	double r=(b*t)/4;
//      return  r;
//}
//double tercer( double c )
//{
//	double u=pow(n,3);               
//	double p=(c*u)/3;
//      return  p;
//}
//double cuarto( double d )
//{
//   double w=pow(n,2);
//   double v=(d*w)/2;               
//      return  v;
//}
//double quinto( double j )
//{
//   double g=pow(n,1);
//   double h=(j*g)/1;               
//      return h;
//}
//
//
//double pri( double e )
//{
//   double s=pow(l,5);
//   double q=(a*s)/5;
//      return  q;
//}
//double segu( double f )
//{
//   double t=pow(l,4);
//   double r=(b*t)/4;
//      return  r;
//}
//double ter( double g )
//{
//   double u=pow(l,3);
//   double p=(c*u)/3;
//      return  p;
//}
//double cuar( double i )
//{
//   double w=pow(l,2);
//   double v=(d*w)/2;
//      return  v;
//}
//double quin( double k )
//{
//   double g=pow(l,1);
//   double h=(j*g)/1;
//      return  h;
//}
//------------------- 277 -------------------
//#include <iostream.h>
//#include <math.h>
//void main ()
//{
//	cout<<endl<<endl<<endl<<endl;
//	cout<<"       INTEGRALES DEFINIDAS"<<endl;
//	double A,B,C,D;
//	double  s,a,b,n,i,delta;
//	cout<<endl<<endl;
//	cout<<"     Integral de cualquier polinomio de tercer grado   "<<endl;
//
//	cout<<"     ___________________________________"<<endl;
//	cout<<"    |     b                             |"<<endl;
//   	cout<<"    |    (   3     2       1        0   |"<<endl;
//	cout<<"    |    ) AX  + BX   +  CX   +   DX    |"<<endl;
//	cout<<"    |   a                               | "<<endl;
//	cout<<"    |___________________________________|"<<endl;
//	cout<<endl;
//	cout<<"ingrese el coeficiente   A  =  ";
//	cin>>A;
//	cout<<"ingrese el coeficiente   B  =  ";
//	cin>>B;	
//	cout<<"ingrese el coeficiente   C  =  ";
//	cin>>C;	
//	cout<<"ingrese el coeficiente   D  =  ";
//	cin>>D;
//	cout<<endl<<endl;cout<<"  El polinomio de tercer grado es  : "<<endl;
//	cout<<"     __________________________________"<<endl;
//	cout<<"    |                                  |"<<endl;
//   	cout<<"    |       3     2       1        0   |"<<endl;
//	cout<<"    |     "<<A<<"X  + "<<B<<"X   +  "<<C<<"X   +  "<<D<<"X     |   "<<endl;
//	cout<<"    |                                  |"<<endl;
//	cout<<"    |__________________________________|"<<endl;
//	cout<<endl;
//	cout<<endl<<endl;
//	cout <<"ingrese  n   el numero de particiones  =  ";
//	cin>>n;	
//	cout <<endl;cout <<"  DONDE  a < b	"<<endl<<endl;
//	cout <<"ingrese  a   el limite inferior  =  ";
//	cin>>a;
//	cout <<"ingrese  b   el limite superior  =  ";
//	cin>>b;
//	cout<<endl<<endl;
//		delta = (b-a)/n;
//		s=0;
//		for (i=1;i<=n;i++)
//		{    
//		s=s+A*(a+delta*i)*(a+delta*i)*(a+delta*i)*delta+B*(a+delta*i)*(a+delta*i)*delta+C*(a+delta*i)*delta+D*delta;
//		}	
//	cout<<"la integral es :"<<endl;
//	cout<<"     ___________________________________"<<endl;
//	cout<<"    |   "<<b<<"                               |"<<endl;
//   	cout<<"    |    (   3     2       1        0   |"<<endl;
//	cout<<"    |    ) "<<A<<"X  + "<<B<<"X   +  "<<C<<"X   +  "<<D<<"X     |  = "<<s<<endl;
//	cout<<"    | "<<a<<"                                 |"<<endl;
//	cout<<"    |___________________________________|"<<endl;
//	cout<<endl;
//	cout<<endl<<endl;
//}
//
//------------------- 278 -------------------
//
//
//------------------- 279 -------------------
////Determinar mediante un mensaje si un numero ingresado es par, impar, cero, positivo, //negativo.
//#include <iostream.h>
//int main()
//{
//int n;
//	cout<<"Ingresar un numero ";
//	cin>>n;
//	if((n<0))
//		{
//		 cout<<"Negativo "<<endl;
//		 if(n%2==0)
//		    cout<<"Par "<<endl;
//	         else
//		    cout<<"Impar "<<endl;
//		}
//	else
//		{
//		 if(n==0)
//		   cout<<"Cero "<<endl;
//		 else
//		   {
//		     cout<<"Positivo "<<endl;
//		     if(n%2==0)
//			cout<<"Par "<<endl;
//		     else
//			cout<<"Impar "<<endl;
//		    }
//		 }
//   return 0; 
//} 
//
//-------------------    -------------------
//// Mediante el uso de tres funciones (cubo, esfera, volumen) realice un programa en C++ //que permita calcular el volumen de lo que queda de un cubo incrustado por una esfera //considere para esto los siguientes volúmenes. E = 4pr3/3    C = (2r)3
//
//#include<iostream.h>
//#include<iomanip.h>
//#include<math.h>
//float r,rc;
//double cubo (double);
//double esfera(double);
//double volumen(double);
//void main()
//{
//	cout<< "Ingrese el valor de r de la esfera  ";
//	cin>> r;
//		cout<< "volumen de la esfera es "<< esfera(r);
//		cout<< endl;
//		cout<< "volumen del cubo es "<< cubo(r);
//		cout<< endl;
//		cout<< "El valor buscado es: "<< volumen(r);
//		cout << endl;
//}
//
//double cubo (double rc)
//{
//	return pow((2*rc),3);
//}
//double esfera (double re)
//{
//	return (4*3.141592*pow(re,3))/3;
//}
//double volumen(double rv)
//{
//	return cubo(rv)-esfera(rv);
//}
//
//-=-=-=-
//
////El número de combinaciones con repetición de  k  elementos, que pueden formarse a //partir de  n  elementos distintos  ( Ckkn ) ,  es:
////                                         ( n  +  k  –  1 ) !
////                                Ckkn   =  –––––––––––––––
////                                         k ! × ( n  –  1 ) !
//#include<iostream.h>
//#include<iomanip.h>
//#include<math.h>
//long k,n;
//long comb(long,long);
//long factorial(long);
//void main()
//{
//	cout<< "Ingrese el valor de k  ";
//	cin>> k;
//	cout<< "Ingrese el valor de n  ";
//	cin >>n;
//	cout<< "El valor buscado es " << comb(k,n);
//	cout << endl;
//}
//long comb(long k1,long n1)
//{
//	 return(factorial(n1+(k1-1)))/factorial(k1)*factorial(n1-1);
//}
//long factorial(long f)
//{
//	if (f<=1)
//		return 1;
//	else
//		return f*factorial(f-1);
//}
//
//-=-=-=-
//#include<iostream.h>
//#include<iomanip.h>
//unsigned long factorial(unsigned long);
//unsigned long fact1(unsigned long,unsigned long);
//unsigned long fact2(unsigned long ,unsigned long);
//unsigned long factT(unsigned long,unsigned long);
//long main()
//{
//	unsigned long n,k;
//	cout<<"****************************************"<<endl;
//	cout<<"*             	                  *"<<endl;
//	cout<<"*    			        *"<<endl;
//	cout<<"****************************************"<<endl<<endl;
//
//	cout<<"Ingrese n y k seguidos de espacios: ";
//	cin>>n>>k;
//	if(n>k)
//	cout<<"el valor de la combinatoria es: "<<factT(n,k)<<endl;
//	else
//		cout<<"ERROR"<<endl;
//	return 0;
//}
//unsigned long factorial(unsigned long  a)
//{
//	if (a<=1)
//		return 1;
//	else
//		return a*factorial(a-1);
//}
//unsigned long fact1(unsigned long b,unsigned long c)
//{
//	int i=b+c;
//	if(i<=1)
//		return 1;
//	else
//		return factorial(i-1);
//}
//unsigned long fact2(unsigned long d,unsigned long e)
//{
//	return factorial(d)*factorial(e-1);
//}
//unsigned long factT(unsigned long f,unsigned long g)
//{
//	return fact1(f,g)/fact2(f,g);
//}
//-=-=-=
////Asuma que Ud. tira tres dado especiales de ocho (08) caras  y que sus resultados //aleatoriamente  dan valores entre 1 y 8 . Realice un programa en C++ que  muestre el //resultado variable de cada dado y muestre la sumatoria de los tres .
//
//#include<math.h>
//#include<stdlib.h>
//int main()
//{
//	cout<<"****************************************"<<endl;
//	cout<<"*             		        *"<<endl;
//	cout<<"****************************************"<<endl<<endl;
//
//   srand( time( 0 ) );
//   int dado1;
//   int dado2;
//   int dado3;
//   int Sumadados;
//   dado1 = 1 + rand() % 8;  
//   dado2 = 1 + rand() % 8;  
//   dado3 = 1 + rand() % 8;  
//   Sumadados = dado1 + dado2 + dado3;  
//   cout <<"la suma de los dados es: "<<dado1 << " + " << dado2<<" + "<<dado3
//        << " = " << Sumadados << endl;
//  return 0;
//} 
//
//
//
//
//
//
//
//-=-=-=-
//
////Tabla de Akima que muestra la Funcion seno(X) con doble precision
///*******************************************************
//*          Akima spline fitting subroutine             *
//* ---------------------------------------------------- *
//* The input table is X(i), Y(i), where Y(i) is the     *
//* dependant variable. The interpolation point is xx,   *
//* which is assumed to be in the interval of the table  *
//* with at least one table value to the left, and three *
//* to the right. The interpolated returned value is yy. *
//* n is returned as an error check (n=0 implies error). *
//* It is also assumed that the X(i) are in ascending    *
//* order.                                               *
//*******************************************************/
//#include <iostream.h>
//#include <math.h>
//#include <iomanip.h>
//#define  SIZE  14
//
//double  X [SIZE+1];
//double  Y [SIZE+1];
//double  XM[SIZE+4];
//double  Z [SIZE+1];
//double  a,b,xx,yy;
//int     i,iv,n;
//
//void Interpol_Akima()  
//{
//  //Labels: 100,200,300
//  int i;
//  n=1;
//  //special case xx=0
//  if (xx==0.0) {
//    yy=0.0; return;
//  }
//  //Check to see if interpolation point is correct
//  if (xx<X[1] || xx>=X[iv-3]) 
//  {
//    n=0 ; return;
//  }
//  X[0]=2.0*X[1]-X[2];
//  //Calculate Akima coefficients, a and b
//  for (i=1; i<iv; i++)
//    //Shift i to i+2
//  XM[i+2]=(Y[i+1]-Y[i])/(X[i+1]-X[i]);
//  XM[iv+2]=2.0*XM[iv+1]-XM[iv];
//  XM[iv+3]=2.0*XM[iv+2]-XM[iv+1];
//  XM[2]=2.0*XM[3]-XM[4];
//  XM[1]=2.0*XM[2]-XM[3];
//  for (i=1; i<iv+1; i++)  
//  {
//    a=fabs(XM[i+3]-XM[i+2]);
//    b=fabs(XM[i+1]-XM[i]);
//    if (a+b!=0) goto e100;
//		Z[i]=(XM[i+2]+XM[i+1])/2.0;
//    goto e200;
//e100: Z[i]=(a*XM[i+1]+b*XM[i+2])/(a+b);
//e200: ;
//  }
//  //Find relevant table interval
//  i=0;
//e300: i++;
//  if (xx>X[i]) goto e300;
//  i--;
//  //Begin interpolation
//  b=X[i+1]-X[i];
//  a=xx-X[i];
//  yy=Y[i]+Z[i]*a+(3.0*XM[i+2]-2.0*Z[i]-Z[i+1])*a*a/b;
//  yy=yy+(Z[i]+Z[i+1]-2.0*XM[i+2])*a*a*a/(b*b);
//  return;
//}
//
//void main()  
//{
//  iv=14;  // Number of pooints in table
//  cout<<"\n Tabla Akima ordenada de SEN(X):\n";
//  /* Input sine table
//  -----------------------------------------------------------------
//   Sine table values from  Handbook of mathematical functions
//  ----------------------------------------------------------------- */
//  X[1]=0.000; Y[1]=0.00000000; X[2]=0.125; Y[2]=0.12467473;
//  X[3]=0.217; Y[3]=0.21530095; X[4]=0.299; Y[4]=0.29456472;
//  X[5]=0.376; Y[5]=0.36720285; X[6]=0.450; Y[6]=0.43496553;
//  X[7]=0.520; Y[7]=0.49688014; X[8]=0.589; Y[8]=0.55552980;
//  X[9]=0.656; Y[9]=0.60995199; X[10]=0.721; Y[10]=0.66013615;
//  X[11]=0.7853981634; Y[11]=0.7071067812;
//  X[12]=0.849; Y[12]=0.75062005; X[13]=0.911; Y[13]=0.79011709;
//  X[14]=0.972; Y[14]=0.82601466;
//  //----------------------------------------------------------------
//  cout<<"\n X   MANUAL DE SEN(X)    INTERPOLACION AKIMA  ERROR  \n";
//  cout<<"----------------------------------------------------\n";
//  xx=0.0;
//  for (i=1; i<17; i++) 
//  {
//    Interpol_Akima();
//    cout<<setprecision(2)<<xx<<setprecision(7)<<setw(13)<<sin(xx)<<setprecision(7)<<setw(20)<<yy<<setprecision(7)<<setw(22)<<(sin(xx)-yy)<<endl;
//    xx += 0.05;
//  }
//  cout<<"----------------------------------------------------\n";
//}
//-=-=-=-
//
///***************************************************
//*  Evaluacion eliptica de Integrales de 1er y 2do Or*
//*  integrals of first and second kinds (completa)  *
//* ------------------------------------------------ *
//* EJEMPLO de CORRIDA                               *
//*                                                  *
//*    K         K(K)          E(K)      PASOS       *
//*  -------------------------------------------     *
//*   1.00     INFINITY      1.0000000     0         *
//*                                                  *
//* Complete elliptic integral of the first and second *
//* kind. The input parameter is xk, which should be   *
//* between 0 and 1. Technique uses Gauss' formula for *
//* the arithmogeometrical mean. e is a measure of the * 
//* convergence accuracy. The returned values are e1,  *
//* the elliptic integral of the first kind, and e2,   *
//* the elliptic integral of the second kind.          *
//*****************************************************/
//#include <stdio.h>
//#include <math.h>
//
//double  A[100], B[100];
//double  e,e1,e2,xk;
//int     i, n;
//
//
//void CElliptic()  
//{
////Label: e100
//  int j, m; double pi;
//  pi = 4*atan(1);
//  A[0]=1.0+xk ; B[0]=1-xk;
//  n=0;
//  if (xk < 0) return;
//  if (xk > 1) return;
//  if (e <= 0) return;
//e100: n++;
//  // Generate improved values
//  A[n]=(A[n-1]+B[n-1])/2.0;
//  B[n]=sqrt(A[n-1]*B[n-1]);
//  if (fabs(A[n]-B[n]) > e) goto e100;
//  e1=pi/2.0/A[n];
//  e2=2.0;
//  m=1;
//  for (j=1; j<n+1; j++) { 
//    e2=e2-m*(A[j]*A[j]-B[j]*B[j]);
//    m=m*2;
//  }
//  e2 *= (e1/2.0);
//}
//
//void main()  
//{
//  e=1e-7;
//  printf("  K         K(K)          E(K)      PASO \n");
//  printf("------------------------------------------\n");
//  xk=0.0;
//  for (i=1; i<21; i++) {
//    CElliptic();
//    printf(" %4.2f     %9.7f     %9.7f     %d\n",xk,e1,e2,n);     
//    xk += 0.05;
//  }
//  printf(" 1.00     INFINITY      1.0000000     0\n\n");
//}
//
//-=-=-=-
//
///*****************************************************************
//*   Program to demonstrate Lagrange derivative interpolation     *
//* -------------------------------------------------------------- *
//* SAMPLE RUN:                                                    *
//*                                                                *
//*   X    2COS(2X)     YP         YP1        ERROR 1     ERROR 2  *
//* -------------------------------------------------------------- *
///****************************************************
//* Lagrange derivative interpolation procedure Deriv *
//* NL is the level of the interpolation ( ex. NL=3 ) *
//* N is the total number of table values.            *
//* X[i], Y[i] are the coordinate table values, Y[i]  *
//* being the dependant variable. The X[i] may be     *
//* arbitrarily spaced. x1 is the interpolation point *
//* which is assumed to be in the interval with at    *
//* least one table value to the left, and NL to the  *
//* right. Yp is returned as the desired derivative.  *
//* error is set at TRUE if x1 is not in the interval.*
//****************************************************/
//#include <stdio.h>
//#include <math.h>
//
//#define  NMAX  100
//#define  pas   0.05
//
//double X[NMAX],Y[NMAX];
//double xx,yy,yy1;
//int    error,i,n,ndata;
//
//
//
//void Deriv(int n, int nl, double *X, double *Y, double x1, double *Yp,int *error) {
//
//  int i,j,k,ll;
//  double L[10], M[10][10];
//    *error=0;
//    // x1 not in interval [1:N-NL] 
//    if (x1<X[1] || x1>X[n-nl])  {
//      *error=1;
//      printf(" STOP: x not between X[1] or X[N-4].\n");
//    }
//    if (*error==0) {
//      i=0;
//      do {
//        i++;
//      } while (x1 >= X[i]);
//      i--;
//      for (j=0; j<nl+1; j++) {
//        L[j]=0.0;
//        for (k=0; k<nl+1; k++) M[j][k]=1.0;
//      }
//      *Yp=0.0;
//      for (k=0; k<nl+1; k++) {
//        for (j=0; j<nl+1; j++) {  
//          if (j!=k) { 
//            for (ll=0; ll<nl+1; ll++) {
//              if (ll!=k) {
//                if (ll==j)
//                  M[ll][k]=M[ll][k]/(X[i+k]-X[i+j]);
//                else
//                  M[ll][k]=M[ll][k]*(x1-X[j+i])/(X[i+k]-X[i+j]);
//              }
//            }
//          }
//        }
//        for (ll=0; ll<nl+1; ll++) 
//          if (ll!=k) L[k]=L[k]+M[ll][k];
//        *Yp=*Yp+L[k]*Y[i+k];
//      }
//    }
//} // Deriv()
//
//     /*********************************************************
//      CALCULE LES COEFFICIENTS A,B DE LA PARABOLE Y=A*X*X+B*X+C
//      PASSANT PAR LES 3 POINTS : (X1,Y1),(X2,Y2) ET (X3,Y3)
//      COEFFICIENT C NON UTILISE ICI.
//      ---------------------------------------------------------
//      Calculates coefficients, a, b of parabola Y=A*X+X+B*X=C
//      passing through 3 points: (X1,Y1), (X2,Y2) and (X3,Y3).
//      Coefficient c is not used here.
//      *********************************************************/
//      void PARABOLE(double x1,double y1,double x2,double y2,
//		            double x3,double y3,double *a,double *b) {
//        double alpha,beta,gamma,delta;
//        alpha=x1*x1-x2*x2;
//        beta=x1-x2;
//        gamma=x2*x2-x3*x3;
//        delta=x2-x3;
//        *a=(y1-2.0*y2+y3)/(alpha-gamma);
//        *b=(y1-y2-alpha**a)/beta;
//      }
//
///***************************************************
//*     Interpolation of order=2 ( parabola )        *
//*                            by J-P Moreau         *
//***************************************************/
//void Deriv1(int n, double *X, double *Y, double x1, double *Yp,
//            int *error)  {
//  double a, b;
//  int i;
//
//  *error=0;
//  if (x1<X[1] || x1>X[n-2]) {
//    *error=1;
//	return;
//  }
//  i=0;
//  while (x1>=X[i]) i++;
//  i--;
//
//  PARABOLE(X[i],Y[i],X[i+1],Y[i+1],X[i+2],Y[i+2],&a,&b);
//
//  //Derivative in x1
//
//  *Yp=2*a*x1+b;
//
//}
//void main() { //derivative of 2*sin(x)*cos(x) between 0 and 1
//  n=4;        //level of Lagrange interpolation
//  ndata=26;   //number of table points
//  // building X & Y Tables
//  for (i=1; i<ndata+1; i++) {
//    X[i]=(double) pas*(i-1);
//    Y[i]=2*cos(X[i])*sin(X[i]);
//  }
//  xx=0.0;
//  printf("  X    2COS(2X)     YP         YP1        ERROR 1     ERROR 2\n");  //heading
//  printf("--------------------------------------------------------------\n");
//  //main loop of derivation
//  do {
//    Deriv(ndata,n,X,Y,xx,&yy,&error);
//    Deriv1(ndata,X,Y,xx,&yy1,&error);
//    if (error==0)  {
//	  printf("%4.2f  %9.6f  %9.6f  %9.6f  %10.7f  %10.7f\n",xx,2*cos(2*xx),yy,yy1,
//		     yy-2*cos(2*xx), yy1-2*cos(2*xx) );
//    }
//    xx=xx+pas;
//  } while(xx<1.0+pas);
//  printf("--------------------------------------------------------------\n");
//}


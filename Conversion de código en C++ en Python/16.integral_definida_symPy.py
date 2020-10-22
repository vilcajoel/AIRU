# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:22:48 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================
#    //Se desea desarrollar una aplicacion que permita calcular la integral 
#    //definida de una funcion:   g    g
#    //                  f(x) = Cx + Cx ......  
#    //                         --   --
#    //                         T1   T2
#    //  C = Coeficientes; g = Grado del Termino; T = Termino; i-n = intervalo de integral
#    //					
#    #include<iostream>
#    #include<iomanip>
#    #include<cstdlib>
#    #include<math.h>
#    using namespace std;
#    int main()
#    {	
#      float matrizC[20];//Matriz de Coeficiente
#      float matrizg[20];//Matriz de Grado de Termino
#      double y;
#      int n,i,j,x1,x2;
#      cout<<"            Calculo de Integral definida de una funcion"<<endl<<endl;
#      cout<<"	            	    n    g    g                   "<<endl;
#      cout<<"                  f(x) = Cx + Cx ......  "<<endl;
#      cout<<"                      i  --   --	        "<<endl;
#      cout<<"                         T1   T2			"<<endl<<endl;
#      cout<<"C = Coeficiente; g = Grado de Termino; T = Termino; i-n= intervalo"<<endl<<endl; 
#    	cout<<"Ingrese cantidad de terminos (T) para f(x) a Integrar: ";
#    	cin>>n;
#    	for (i=1;i<=n;i++)
#    		{	
#    		  cout<<"Ingrese el coeficiente (C) y grado (g) del T"<<i<<": ";
#    		  cin>>matrizC[i]>>matrizg[i];
#    		}
#    	cout<<endl;
#    	cout<<"La funcion f(x) definida es : ";
#    	for (i=1;i<=n;i++)
#    		{
#    		 if (i==1)
#    		 cout<<matrizC[i]<<"x"<<matrizg[i]<<setw(2);//se muestra funcion definida
#    		 else
#    		 cout<<" + "<<matrizC[i]<<"x"<<matrizg[i]<<setw(2);
#    		}
#    	cout<<endl;
#    	cout<<"La integral desarrollada es : ";
#    	for (i=1;i<=n;i++)
#    	    {	
#    		 if (i==1)
#    		    cout<<matrizC[i]/(matrizg[i]+1)<<"x"<<matrizg[i]+1<<setw(2);
#    		 else
#    		    cout<<" + "<<matrizC[i]/(matrizg[i]+1)<<"x"<<matrizg[i]+1<<setw(2);
#    		}
#    	cout<<endl;
#    	cout<<"Ingrese el intervalo (i-n) de la integral: ";
#    	cin>>x1>>x2;
#    	y=0;
#    	for (j=x1;j<=x2;j++)
#    	    {	
#    		 for(i=1;i<=n;i++)
#    		    {
#    			y = y + matrizC[i] / ( matrizg[i]+1 )*pow( j,matrizg[i]+1 );
#    		    }
#    	    }
#    	cout<<"El calculo de la integral es : "<<y<<endl;
#    	return 0;
#    }


# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================
import sympy as sp

x = sp.Symbol("x")
dx = sp.Integral(x**3 - 6*x, x).doit()





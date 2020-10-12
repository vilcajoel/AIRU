# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 01:06:25 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================

#    //------------------- INTEGRALES -------------------
#    #include<iostream>
#    #include<math.h>
#    using namespace std;
#    int main ()
#    {
#    	cout<<endl<<endl;
#    	cout<<"       INTEGRALES DEFINIDAS"<<endl;
#    		
#    	cout<<endl<<endl;	cout<<endl;
#    	cout<<"     ___________________________________"<<endl;
#    	cout<<"    |     b                             |"<<endl;
#      	cout<<"    |    (                              |"<<endl;
#    	cout<<"    |    ) seno(x)coseno(x)dx           | "<<endl;
#    	cout<<"    |   a                               | "<<endl;
#    	cout<<"    |___________________________________|"<<endl;
#    	cout<<endl;	cout<<endl;
#    	double  s,a,b,n,i,delta;
#    	cout <<"ingrese  n el numero de particiones  =  ";
#    	cin>>n;
#    	cout <<"ingrese  a el limite inferior  =  ";
#    	cin>>a;
#    	cout <<"ingrese  b el limite superior  =  ";
#    	cin>>b;
#    	cout<<endl<<endl;cout<<endl;
#    
#    		delta = (b-a)/n;
#    		s=0;
#    
#    		for (i=1;i<=n;i++)
#    			{
#    				s = s + sin(a + delta * i) * cos(a + delta * i) * delta;
#    			}
#    	cout<<"la integral es :";	cout<<endl<<endl;
#    	cout<<"     ___________________________________ "<<endl;
#    	cout<<"    |     b                             |"<<endl;
#      	cout<<"    |    (                              |"<<endl;
#    	cout<<"    |    ) seno(x)coseno(x)dx           | = "<<s<<endl;
#    	cout<<"    |   a                               |"<<endl;
#    	cout<<"    |___________________________________|"<<endl;
#    	cout<<endl;	cout<<endl;
#    }

# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================

import math

def start():
    print("\t\t****************************\n \t\t\tINTEGRALES DEFINIDAS \n\t\t****************************\n")    
    print("     ___________________________________")
    print("    |     b                             |")
    print("    |    (                              |")
    print("    |    ) seno(x)coseno(x)dx           | ")
    print("    |   a                               | ")
    print("    |___________________________________|")
    
    datos = []
    datos.append(int(input("ingrese  n el numero de particiones  =  ")))
    datos.append(int(input("ingrese  a el limite inferior  =  ")))
    datos.append(int(input("ingrese  b el limite superior  =  ")))
    
    delta = ((datos[2]-datos[1])/datos[0])
    s = 0
    for i in range(1, datos[0]+1):
        s = s + math.sin(datos[1]+delta*i) * math.cos(datos[1]+delta*i) * delta
    print("La integral es : \n")
    print("     ___________________________________")
    print("    |     b                             |")
    print("    |    (                              |")
    print("    |    ) seno(x)coseno(x)dx           | = {:.6}".format(s))
    print("    |   a                               | ")
    print("    |___________________________________|")



if __name__ == '__main__':
    start()
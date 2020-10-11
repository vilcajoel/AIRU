# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:20:03 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================

#    //------------------- DERIVADA -------------------
#    //	              			            4	 3    2
#    //Desarrollo de derivadas de la forma ax + bx + cx + dx + e
#    #include<iostream>
#    #include<math.h>
#    using namespace std;
#    double primer( double ); 
#    double segundo( double); 
#    double tercer(double); 
#    double cuarto(double ); 
#    double quinto(double ); 
#    double a,b,c,d,j;
#    double l;
#    double h,m;
#    int main()
#    {
#    	cout<<"                       4    3    2        "<<endl;
#    	cout<<"Derivada de la forma ax + bx + cx + dx + e"<<endl;
#    	cout<<"Ingrese valor a: ";
#    	cin>>a;
#    	cout<<"Ingrese valor b: ";
#    	cin>>b;
#    	cout<<"Ingrese valor c: ";
#    	cin>>c;
#    	cout<<"Ingrese valor d: ";
#    	cin>>d;
#    	cout<<"Ingrese valor e: ";
#    	cin>>j;
#    	cout<<"Ingrese el valor a derivar: ";
#    	cin>>l;
#    	h =  primer(a)+  segundo(b)+ tercer(c)+ cuarto(d)+quinto(j);
#    	cout<<"Valor de derivada: "<<h<<endl;
#    
#    }
#    double primer( double a )
#    {
#       double s=pow(l,3);
#       double q=(a*s)*4;
#          return q;
#    }
#    double segundo( double b )
#    {
#    	double t=pow(l,2); 
#    	double r=(b*t)*3;
#          return  r;
#    }
#    double tercer( double c )
#    {
#    	double u=pow(l,1);               
#    	double p=(c*u)*2;
#          return  p;
#    }
#    double cuarto( double d )
#    {
#       double w=pow(l,0);
#       double v=(d*w)*1;               
#          return  v;
#    }
#    double quinto( double j )
#    {
#       double g=0;
#       double h=(j*g);               
#          return h;
#    }


# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================


def start():
    print("\t\t************************\n \t\t\t\tDERIVADAS \n\t\t************************\n")
    print("                       4    3    2        ")
    print("Derivada de la forma ax + bx + cx + dx + e")
    coeficientes = []
    coeficientes.append(int(input("Ingrese valor a: ")))
    coeficientes.append(int(input("Ingrese valor b: ")))
    coeficientes.append(int(input("Ingrese valor c: ")))
    coeficientes.append(int(input("Ingrese valor d: ")))
    x = int(input("Ingrese el valor a derivar: "))
    print("El valor de la derivada es : {}  ".format(derivar(coeficientes, x)))
    
def derivar(coeficientes, x):
    d = 0
    for i in range(0, 4):      
        d = d + coeficientes[i]*pow(x,3-i)*(4-i)
    return d
    
    
    
    
if __name__ == '__main__':
    start()
    

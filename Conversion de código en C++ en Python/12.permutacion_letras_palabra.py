# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:50:58 2020

@author: vilcajoal - Vilca Joel Alberto
"""

# =============================================================================
#                           CÓDIGO C++
# =============================================================================

# =============================================================================
#    //Realiza todas las permutaciones posibles de las letras de la palabra ABCDE
#    #include <iostream> 
#    #include <string.h> 
#    using namespace std;
#    void Permutaciones(char *, int l=0); 
#    
#    int main(int argc, char *argv[])
#    {
#       char palabra[] = "ABCDE";
#       Permutaciones(palabra);
#       return 0;
#    }

#    void Permutaciones(char * cad, int l)
#    {
#       char c;    /* variable auxiliar para intercambio */
#       int i, j;  /* variables para bucles */
#       int n = strlen(cad);
#    
#       for(i = 0; i < n-l; i++)
#       {
#          if(n-l > 2) Permutaciones(cad, l+1);
#          else cout <<cad << ", ";
#          /* Intercambio de posiciones */
#          c = cad[l];
#          cad[l] = cad[l+i+1];
#          cad[l+i+1] = c;
#          if(l+i == n-1)
#          {
#             for(j = l; j < n; j++) cad[j] = cad[j+1];
#             cad[n] = 0;
#          }
#       }
#    }
# =============================================================================

# =============================================================================
#                           CÓDIGO PYTHON
# =============================================================================

# =============================================================================
def permutaciones(s):        
       if(len(s)==1): return [s]
       result=[]
       for i,v in enumerate(s):
           result += [v+p for p in permutaciones(s[:i]+s[i+1:])]
       return result
        


def start():
    palabra = "ABCDE"
    print(permutaciones(palabra))
    



if __name__ == '__main__':
    start()
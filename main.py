#pip freeze > requirements.txt
import streamlit as st

from streamlit_echarts import st_echarts

from pyvis import network as net
from IPython.core.display import display, HTML
import streamlit.components.v1 as components

import numpy as np

st.title("Opa Tudo Bom!")
st.write('Digite uma palavra que irei consstruir um autômato finido não deterministico para voce :)')

def Sufixo(pk,pqa):
  m = len(pk)
  n = len(pqa) 
  if pqa[n-m:]==pk:
    return True
  else:
    return False

def ComputeTransitionFunction(P,A):
  m = len(P)
  n = len(A)
  delta = np.zeros((m+1,n), dtype=np.int64)
  for q in range(m+1):
    for a in range(n):
      k = min(m+1,q+2)
      while True:
        k = k -1
        #print("\ntestando antes ",P[:k], "com ",P[:q]+A[a])
        if (Sufixo(P[:k],P[:q]+A[a])) :          
          #print("delta ",q," ",a," recebe",k)
          delta[q][a] = k                  
          break
      
  return delta

def AfdStringMatching(P,A):    
    d = ComputeTransitionFunction(P,A)    
    g=net.Network(directed =True, height='400px', width='90%',heading='')
    
    g.add_node(0,label="vazio",color="#009c02")
    for i in range(0,len(d)-1,1):        
        if(i == len(d)-2):       
          g.add_node(i+1,label=P[i],color="#ff0000")
        else:
          g.add_node(i+1,label=P[i])
    
    for i in range(len(d)):
        for j in range(len(d[i])):          
          if(i != int(d[i][j])):
            if(int(d[i][j]) != 0):        
              g.add_edge(i,int(d[i][j]),label=A[j])
            
    
    g.show('afd.html') 
    
    HtmlFile = open("afd.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 450,width=900)
   


P = st.text_input('padrao', 'abc')
A="abcdefghijklmnopqrstuvwxyz"

AfdStringMatching(P,A)


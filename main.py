#pip freeze > requirements.txt
import streamlit as st

from streamlit_echarts import st_echarts

from pyvis import network as net
from IPython.core.display import display, HTML
import streamlit.components.v1 as components

import numpy as np

st.title("Opa Tudo Bom!")


g=net.Network(directed =True, height='400px', width='50%',heading='')
g.add_node(1,label='a')
g.add_node(2,label='b')
g.add_node(3,label='c')
g.add_edge(1,2,label='1')
g.add_edge(2,3,label='1')
g.save_graph('example.html')

HtmlFile = open("example.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 450,width=900)
#display(HTML('example.html'))

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

def AfdStringMatching():
    P="aba"
    A="abc"
    d = ComputeTransitionFunction(P,A)
    st.write(d)
    g=net.Network(directed =True, height='400px', width='50%',heading='')
    
    for i in range(len(d)):
        g.add_node(i,label=A[i-1])
    
    for i in range(len(d)):
        for j in range(len(d[i])):
            print(d[i][j])
    
    g.add_edge(1,2,label='1')
    g.add_edge(1,2,label='1')
    g.add_edge(1,2,label='1')
    g.add_edge(2,3,label='1')
    g.save_graph('afd.html')
    
    HtmlFile = open("afd.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 450,width=900)
   
AfdStringMatching()


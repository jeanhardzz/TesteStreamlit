#pip freeze > requirements.txt
import streamlit as st

from streamlit_echarts import st_echarts

from pyvis import network as net
from IPython.core.display import display, HTML
import streamlit.components.v1 as components

st.title("Opa Tudo Bom!")

bro = st.selectbox("Selecione um bro",["pablin","bias","felope","pedron","jubplay","vitao"])

st.sidebar.title("Menu")

options = {
    "xAxis": {
        "type": "category",
        "data": [bro, bro, bro, bro, bro, bro, bro],
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [120, 200, 150, 80, 70, 110, 130], "type": "bar"}],
}

fig=st_echarts(options=options, height="500px")

st.write(fig)

g=net.Network(directed =True, height='400px', width='50%',heading='')
g.add_node(1,label='a')
g.add_node(2,label='b')
g.add_node(3,label='c')
g.add_edge(1,2,label='1')
g.add_edge(2,3,label='1')
g.save_graph('example.html')

HtmlFile = open("example.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 900,width=900)
#display(HTML('example.html'))




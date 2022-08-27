import streamlit as st
from streamlit_echarts import st_echarts

st.title("Opa Tudo Bom!")

st.selectbox("Selecione um bro",["pablin","bias","felope","pedron","jubplay","vitao"])

st.sidebar.title("Cuidado")

options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [120, 200, 150, 80, 70, 110, 130], "type": "bar"}],
}
st_echarts(options=options, height="500px")

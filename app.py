import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid


info = pd.read_csv("taxaacerto.csv", sep=";", dayfirst=True)

@st.cache_data
def carregar_dados():
    dado = pd.read_csv("taxaacerto.csv", sep=";")
    return dado

# controi a barra lateral
def build_sidebar():
    st.image("images/logofenixvertical.jpeg")
    block_list = pd.read_csv("/workspaces/dashboard_fenix/blocos.csv", index_col=0)
    block = st.multiselect(label="Escolha o MyBlock", options=block_list, placeholder='Bloco', )
    block = [b.strip() for b in block]
    start_date = st.date_input("De", format="DD/MM/YYYY", value=datetime(2024,1,1))
    end_date = st.date_input("Até", format="DD/MM/YYYY", value=("today"))

    if block:
        info = carregar_dados()
        #info_filtered = info[(info["data"] >= start_date) & (info["data"] <= end_date)]
        return block, info
    return None, None

def build_main(block, info):
    
    chart_data = pd.DataFrame(info, columns=block)
    
    quantidade_erro = len(chart_data[block][1:])
    
    chart_data = chart_data.drop(chart_data.index[0], axis=0)
    chart_data
    media = sum(chart_data[block]) / quantidade_erro

    mygrid = grid(5, 5, 5, 5, 5, 5, vertical_align="top")
    for b in block:
        c = mygrid.container(border=True)
        c.subheader(b, divider="red")
        colA, colB, colC = c.columns(3)
     #   colB.metric(label="Erro", value=(media))

    st.subheader('Taxa De Acerto')
    st.line_chart(chart_data)
    # st.line_chart(info, x="data")
    # st.dataframe(info)
    # st.line_chart(info)

    

#st.set_page_config(layout="wide")
st.title('Painel de Controle Inteligente FENIX')
with st.sidebar:
    block, info = build_sidebar()

if block:
        
    build_main(block, info)
    # st.text(block)


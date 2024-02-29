import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid
import os


info = pd.read_csv("taxaacerto.csv", sep=";", dayfirst=True)

@st.cache_data
def carregar_dados():
    dado = pd.read_csv("taxaacerto.csv", sep=";")
    return dado

testesAutoDesaceleracao = []
testesAutoPilotagem = []

def carregar_todos():
    pastaAutoDesaceleracao = './testes/AutoDesaceleracao'
    pastaAutoPilotagem = './testes/AutoPilotagem'

    arquivos_autoDesaceleracao = os.listdir(pastaAutoDesaceleracao)
    arquivos_autoPilotagem = os.listdir(pastaAutoPilotagem)

    for arquivo_csv in arquivos_autoDesaceleracao:
        if arquivo_csv.endswith('.csv'):
            arquivo_csv = pd.read_csv(os.path.join(pastaAutoDesaceleracao, arquivos_autoDesaceleracao))
            testesAutoDesaceleracao.append(df)


    for arquivo_csv in arquivos_autoPilotagem:
        if arquivo_csv.endswith('.csv'):
            arquivo_csv = pd.read_csv(os.path.join(pastaAutoPilotagem, arquivos_autoPilotagem))
            testesAutoPilotagem.append(df)

    
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
    media = chart_data[block].median()
    media
    mygrid = grid(3, 3, 5, 5, 5, 5, vertical_align="top")
    for b in block:
        
        c = mygrid.container(border=True)
        c.subheader(b, divider="red")
        colA, colB = c.columns(2)
        colA.metric(label="Media Acerto", value=(media[b]))
        
        colB.metric(label="Testagens", value=(len(chart_data[b])))

    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.subheader('Taxa De Acerto')
        st.line_chart(chart_data)

    with col2:
        st.subheader('My Block por Saida')

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
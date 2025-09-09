import pandas as pd
import streamlit as st

st.title("Porgrama das 12 casas")
with st.form("Fómulario"):
    nome = st.text_input("Primeiro Nome")
    data_de_nascimento = st.date_input("Data de nascimento"),
    altura = st.number_input("Altura (m)", min_value=0.5, max_value=2.5, step=0.01)
    peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, step=0.1)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])



    submit_button = st.form_submit_button("Enviar")


imc = peso / (altura * altura)

def Fsexo (sexo):
    if(sexo=="Masculino"):
        return True
    elif(sexo=="Feminino"):
        return False


def apto (imc):
    if(imc<18.5):
        return False
    elif(imc>=18.5 and imc<24.9):
        return True
    elif(imc>=25 and imc<29.9):
        return False
    elif(imc>=30 and imc<34.9):
        return False
    elif(imc>=35 and imc<39.9):
        return False
    elif(imc>=40):
        return False

mes = data_de_nascimento[0].month
dia = data_de_nascimento[0].day

if(mes== 1):
    if(dia<21):
        signo= "Capricórnio"
    elif(dia>20):
        signo= "Aquário"
elif(mes== 2):
    if(dia<19):
        signo= "Aquário"
    elif(dia>18):
        signo= "Peixes"
elif(mes== 3):
    if(dia<21):
        signo= "Peixes"
    elif(dia>20):
        signo= "Áries"
elif(mes== 4):
    if(dia<21):
        signo= "Áries"
    elif(dia>20):
        signo= "Touro"
elif(mes== 5):
    if(dia<21):
        signo= "Touro"
    elif(dia>20):
        signo= "Gêmeos"
elif(mes== 6):
    if(dia<21):
        signo= "Gêmeos" 
    elif(dia>20 ):
        signo=  "Câncer"
elif(mes== 7):
    if(dia<23):
        signo= "Câncer"
    elif(dia>22):
        signo= "Leão"
elif(mes== 8):
    if(dia<23):
        signo= "Leão"
    elif(dia>22):
        signo= "Virgem"
elif(mes== 9):
    if(dia<23):
        signo= "Virgem"
    elif(dia>22):
        signo= "Libra"    
elif(mes== 10):
    if(dia<23):
        signo= "Libra"
    elif(dia>22):
        signo= "Escorpião"
elif(mes== 11):
    if(dia<22):
        signo= "Escorpião"
    elif(dia>21):
        signo= "Sargitário"
elif(mes== 12):
    if(dia<22):
        signo= "Sargitário"
    elif(dia>21):
        signo= "Capricórnio"

if (submit_button == True):
    if(apto(imc)==True and Fsexo(sexo)==True):
        st.write(nome + "cavaleiro de ouro de "+signo+" você está pronto para a batalha")
    elif(apto(imc)==True and Fsexo(sexo)==False):
            st.write(nome + " amazona de ouro de "+signo+" você está pronta para a batalha")
    elif(apto(imc)==False and Fsexo(sexo)==True): 
        st.write(nome + " você precisa treinar mais para poder se tornar um cavaleiro")
    elif(apto(imc)==False and Fsexo(sexo)==False):
        st.write(nome + " você precisa treinar mais para poder se tornar uma amazona")

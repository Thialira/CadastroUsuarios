import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, dt_nasc, op_sexo, tipo):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc},{op_sexo},{tipo}\n")

        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📋"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

dt_nasc = st.date_input("Data de Nascimento",
                        format="DD/MM/YYYY",
                        key="dt_nascimento")

op_sexo = st.radio("Escolha uma opção",
                 ["Feminino", "Masculino"],
                 index=None,
                 key="rd_opcao2")

tipo = st.selectbox("Tipo do Cliente",
                    ["Pessoa jurídica", "Pessoa física"],
                    key="inf_pessoa")

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, op_sexo, tipo])


if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Usuario não cadastrado!",
                 icon="❌")

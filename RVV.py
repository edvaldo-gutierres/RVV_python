import streamlit as st
from PIL import Image

#Configurações da página
st.set_page_config(
    page_title="RVV 1.0",
    page_icon="👋",
)

image = Image.open('logo.jpg')


st.write("# Página Inicial RVV 👋")

st.image(image, caption='Remuneração Variável de Vendas')

st.markdown("""
    Aplicação referente ao microfundamento Projeto de Banco de Dados Relacional da PUC Minas 2023.
    
    Banco de dados para um sistema de gerenciamento de cálculo de remuneração variável de vendas (RVV)
     em empresas de vendas, considerando como pilares de cálculos a meta e o realizado de indicadores 
     estratégicos conforme a visão de negócio proposta por sua diretoria comercial.
    
    Os pilares de cálculo são compostos por:
    - **Indicadores**
    - **Departamento**
    - **Cargo**

    **Departamento**: são lotados por funcionários vendedores que atendem a um tipo de varejo (key account, mercado interno e e-commerce).
    
    **Cargos**: são classificados por senioridades (sênior, pleno e júnior)
    
    Os **:blue[indicadores]** são identificados por sequencia numérica exclusiva (id) e contem os atributos código e descrição dos departamentos e cargos, e suas datas de início e fim de vigência.

    Os **:blue[funcionários]** são identificados por seu número exclusivo de matrícula e contém os atributos **nome**, **CPF**, **sexo**, **departamento**, 
    **data de nascimento**, **cargo** e **salário**. Cada **:blue[vendedor]** será lotado em apenas um **:blue[departamento]** e estará relacionando em apenas um **:blue[cargo]**.
     
    A **:blue[comissão]** será calculada com base nos **:blue[indicadores]**, onde o índice de produtividade (I.P.) será medido pela divisão do **:blue[realizado]** pela **:blue[meta]**.
    O valor da **:blue[comissão]** se dará pelo produto do I.P. e a base de cálculo. 
    A base de cálculo é categorizada por cargos de gestão e operacional, onde a definição se dá por percentual do salário e percentual do faturamento bruto, respectivamente.

""")

st.sidebar.markdown("# Sejam bem vindos ao RVV")

st.sidebar.success(" Selecione o módulo desejado.")
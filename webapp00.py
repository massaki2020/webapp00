# myFirstStreamlitApp.py
  
#import the library
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("FunControll")
# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Sobre a nossa Plataforma")
# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Conheça-nos melhor!")
# Use st.write("") para adicionar um texto ao seu Web app
st.write("Nós somos uma plataforma que disponibiliza funções para os gestores das empresas distribuírem as tarefas entre os colaboradores de maneira mais assertiva. Já os colaboradores, podem ver se estão sobrecarregados, a partir de uma maneira tecnológica de identificação. Além disso, disponibilizamos acesso de melhoria de qualidade de vida aos colaboradores, podem agendar sessões com terapeutas, psicólogos e selecionar funções para relaxar, como meditações.")

x = st.slider('Escolha o seu nível de ansiedade devido ao trabalho:')
if x < 50 :
  st.write ("Você não está ansioso")
if x > 80 :
  st.write ("Você está muito ansioso. Consulte um psicólogo!")
else :
  st.write ("Você está ficando ansioso.")

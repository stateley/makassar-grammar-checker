import webbrowser
import streamlit as st 
import pandas as pd
import lexical_analyzer
import parse
from annotated_text import  annotated_text
import numpy as np
import pandas as pd


st.title('Hello World! :sunglasses:')
# User Token Input
kalimat = st.text_input("Masukkan kalimat yang ingin diperiksa")

annotated_text("contoh kalimat masukkan yang diterima :", ("Nakke","SUBJECT"), ("assasa","VERB"), ("motoro","OBJECT"))
st.write("\n")

st.caption("Pastikan inputan sesuai dengan token yang ada di tabel ini ya!")

# Tabel Token
data = {'subject':  ['nakke', 'ammak', 'andi','mangge'],
        'verb': ['assassa','anganre','ancinik',''],
         'object' : ['motoro','konro','maggale',''] }
df = pd.DataFrame(data)
st.table(df)

# Proses Lexical Analyzer
st.subheader(':sparkles: Proses Lexical Analyzer :sparkles:')
is_valid = lexical_analyzer.analyze(kalimat)
if is_valid == True:
   st.success('Semua token yang Anda inputkan adalah valid!')
else :
   st.error('Ups, sepertinya ada yang salah. Yuk coba lagi! :nerd_face:')

# Proses Parse
st.subheader(':sparkles: Proses Parse :sparkles:')
if is_valid == True:
   parse.analyze(kalimat)

# About This Project 
with st.sidebar:
   st.markdown('About **_this project_** :')
   st.caption('Project ini ditujukan untuk memenuhi tugas besar mata kuliah Teori Bahasa dan Automata.')
   st.caption('Pada project ini Anda dapat melakukan pengecekan Grammar berdasarkan kata yang sudah diolah menggunakan proses lexical analyzer dan juga parse.')
   
   st.markdown('User Manual :')
   st.caption('1. Inputkan token sesuai dengan yang ada di tabel')
   st.caption('2. Hasil Lexical Analyzer akan muncul pada bagian Proses Lexical Analyzer')
   st.caption('3. Proses Parse akan dilakukan jika Proses Lexical Analyzer berhasil atau valid')

   st.markdown('Author :\n')
   st.caption('Yunolva Anis Ramaziyah (1301204096)\n')
   st.caption('Alif Faidhil Ahmad (1301204141)\n')
   st.markdown('Find us at : ')    

   url = "https://github.com/yunolva"
   if st.button('Github'):
     webbrowser.open_new_tab(url)
import streamlit as st
from PIL import Image

tab1, tab2, tab3 = st.tabs(["HOME", "PESANAN", "Info"])

with tab1:
   nama = input("Nama : ")
   print(nama)
   
with tab2:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab3:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
   
  

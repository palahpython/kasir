import streamlit as st
st.write("""
DAFTAR
""")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)





nama = st.text-input("Nama Lengkap :")
umur = st.date_input()
number = st.number_input("Nomor Hp. :")
password = st.password_input("Kata Sandi :")

st.write("Nama Lengkap : ",nama)
st.write("Umur : ",umur)
st.write("Nomor Hp  : ",number)
st.write("Kata Sandi : ",password)


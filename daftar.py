import streamlit as st
st.write("""
DAFTAR
""")

nama = st.text_input('Nama Lengkap : ')
umur = st.date(datetime())
number = st.text_input('Nomor Hp. :')
password = st.text_input('Kata Sandi :')

st.write('Nama Lengkap : ',nama)
st.write('Umur : ',umur)
st.write('Nomor Hp  : ',number)
st.write('Kata Sandi : ',password)


import streamlit as st
st.write("""
DAFTAR
""")

nama = st.text_input('Nama Lengkap : ')
number = st.text_input('Nomor Hp. :')
password = st.text_input('Kata Sandi :')
daftar = st.button('KIRIM')


st.write('Nama Lengkap : ',nama)
st.write('Nomor Hp  : ',number)
st.write('Kata Sandi : ',password)


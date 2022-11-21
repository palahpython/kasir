import streamlit as st
from PIL import Image

tab1, tab2, tab3 = st.tabs(["HOME", "PESANAN", "Info"])

with tab1:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab2:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab3:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
   
   st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

tab1, tab2, tab3 = st.tabs(["HOME", "PESANAN", "Info"])

with tab1:
   st.header("kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab2:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab3:
   st.header("Kasir")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


components.html(
    """
    <table>
    <tr>
    <td>HOME</td>
    <td>|<td>
    <td>Help</td>
    </tr>
    </table>
    """,
    height=600,
)

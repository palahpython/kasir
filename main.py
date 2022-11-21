import streamlit as st
import streamlit.components.v1 as components


st.image('kasir.png')
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


st.balloons()

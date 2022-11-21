import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <table>
    <tr>
     <td> <img src="kasir.png"></img></td>
    <td>HOME</td>
    <td>|<td>
    <td>Help</td>
    </tr>
    </table>
    """,
    height=600,
)

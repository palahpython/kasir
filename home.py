import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <table>
    <tr>
    <td>HOME</td>
    <td>Help</td>
    </tr>
    </table>
    """,
    height=600,
)

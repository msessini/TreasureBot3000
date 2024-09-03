from streamlit_folium import folium_static
from map import make_map
import streamlit as st

st.markdown('### Recycling map')

col1, col2, col3 = st.columns(3)
with col1:

    address = st.text_input("Find the nearest recycling bins:", "")

    kind = st.radio(
        "What do you want to dipose ?",
        options=["Glass", "Clothes", "Batteries"],
        horizontal=False
    )

if address:
    with col2:
        folium_static(make_map(address, kind))

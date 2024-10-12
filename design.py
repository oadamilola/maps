from altair import Latitude, Longitude
import streamlit as st
import pydeck as pdk

#title- sets title of page
st.title("WeOutside")
#st.title("This is a title")
#st.title("_Streamlit_ is :blue[cool] :sunglasses:")

with st.sidebar:
    st.text_area("Event Title1","Event Description: .....")
    st.text_area("Event Title2","Event Description: .....")
    st.text_area("Event Title3","Event Description: .....")
    st.text_area("Event Title4","Event Description: .....")

# Embedding Google Maps
# Set up a PyDeck map view
initial_view_state = pdk.ViewState(
    latitude=51.5043,  # Coordinates for the map center 
    longitude=-0.1232,
    zoom=11,
    pitch=50,
)


# Create the map layer
layer = pdk.Layer(
    'HexagonLayer',  # Type of the map layer
    data=[{'position': [lon, lat]} for (lon, lat) in [(Longitude, Latitude)]],  # List of coordinates
    get_position='[lon, lat]',
    radius=200,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)

# Create the map
map = pdk.Deck(
    layers=[layer],
    initial_view_state=initial_view_state,
    tooltip={'text': 'Concentration of events'}
)

st.pydeck_chart(map)
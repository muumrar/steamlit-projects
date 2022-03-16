import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk
import json
import requests

#obj = {"x": 1, "y": 2}
#st.write(obj)
#st.write(json.dumps(obj))

#df = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #columns=['lat', 'lon'])

df = pd.read_csv('https://raw.githubusercontent.com/muumrar/steamlit-projects/main/pydeck/nylatlon.csv')


#st.map(df)
#st.map(df)


## This is the beginning of the pydeck chart
st. pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/satellite-streets-v11', ## map style
     initial_view_state=pdk.ViewState( ## Evident, sets initial view of the map
         latitude=40.65,
         longitude=-74.00,
         zoom=10,
         pitch=40,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer', ## Hexagon Layer chart aggregates points into hexagon
            data=df,
            get_position='[lon, lat]',
            radius=150,
            elevation_scale=5,
            elevation_range=[1, 1000], ## Elevation represents number of points in that radius
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer', ## Tutorial includes Scatter points too, although not sure why
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 60, 160]',
             get_radius=100,
         ),
     ],
 )
)

#json.dump('http://localhost:8501/')
#print(df.head())








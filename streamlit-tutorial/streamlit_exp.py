import streamlit as st
import pandas as pd
import numpy as np

st.title('Recycle Bins in NYC')

#DATE_COLUMN = 'date/time'
DATA_URL = ('https://data.cityofnewyork.us/'
         'api/views/sxx4-xhzg/rows.csv?accessType=DOWNLOAD')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



df = pd.read_csv(DATA_URL, nrows=500)

st.write(df)

df.rename({'Longitude':'lon'}, axis='columns', inplace=True)

df.rename({'Latitude':'lat'}, axis='columns', inplace=True)

geo_options = df['Borough'].unique().tolist()
geo = st.selectbox('Which Borough', geo_options, 0)
df = df[df['Borough']==geo]

st.map(df).dropna(subset=["lon", "lat"])

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)

#borough = pd.DataFrame(data=data, columns=0)
#st.write(borough)

data.rename({'longitude':'lon'}, axis='columns', inplace=True)

data.rename({'latitude':'lat'}, axis='columns', inplace=True)

borough = data['borough'].drop_duplicates()


options = st.multiselect(
     'Which borough you wanna look at?',
     borough)

filtered_data = data[borough == options]

#st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data.dropna(subset=["lon", "lat"]))

#borough_choice = st.sidebar.selectbox('borough: ', borough)


####st.map(data.dropna(subset=["lon", "lat"]))


#st.map(data.dropna(subset=["longitude", "latitude"]))
#st.map(data)
data.lon.dtype
#st.map(data)

#st.subheader('Number of pickups by hour')

#hist_values = np.histogram(
    #data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

#st.bar_chart(hist_values)
#st.write(data['borough'])
#borough_to_filter = st.select_slider('borough', ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'])
#filtered_data = data[data[0] == borough_to_filter]
#st.subheader(f'Map of all pickups at {hour_to_filter}:00')
#st.map(filtered_data)


#st.write(filtered_data)
#st.subheader('Map of all pickups')

#st.map(data)


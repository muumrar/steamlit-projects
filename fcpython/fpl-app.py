import pandas as pd
import numpy as np
import streamlit as st




pd.set_option('display.max_columns', 5000)


df = pd.read_csv('fpldata.csv')


df['90s'] = df['minutes']/90
calc_elements = ['goals', 'assists', 'points']
for each in calc_elements:
    df[f'{each}_p90'] = df[each] / df['90s']

positions = list(df['position'].drop_duplicates())
teams = list(df['team'].drop_duplicates())

print(df.head())

#print(positions)
#print(teams)


#@st.cache
st.sidebar.markdown('### Data Filters')

container = st.sidebar.container()
all = st.sidebar.checkbox("Select all")

if all:
    position_choice = container.multiselect(
    'Choose position: ', positions, positions)
else:
    position_choice = container.multiselect(
    'Choose position: ', positions, default=None
)


if all:
teams_choice = st.sidebar.multiselect(
    "Teams: ", teams, default=teams
)



price_choice = st.sidebar.slider(
    "max Price: ", min_value=4.0, max_value=15.0, step=.5, value=15.0
)

df = df[df['position'].isin(position_choice)]
df = df[df['team'].isin(teams_choice)]
df = df[df['cost'] < price_choice]


# Main
st.title(f"Fantasy Football Analysis")

#Main - dataframes
st.markdown('### Player Dataframe')

st.dataframe(df.sort_values('points', ascending=False).reset_index(drop=True))

## Chart Header
st.markdown('### Cost vs 20/21 Points')
## Plot
st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'cost', 'type': 'quantitative'},
        'y': {'field': 'points', 'type': 'quantitative'},
        'color': {'field': 'position', 'type': 'nominal'},
        'tooltip': [{'field': 'name', 'type': 'nominal'}, {'field': 'cost', 'type': 'quantitative'}, {'field': 'points', 'type': 'quantitative'}],
    },
    'width': 700,
    'height': 400,
})

##Chart header
st.markdown('### Goals p90 vs Assists p90')
## Plot

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'goals_p90', 'type': 'quantitative'},
        'y': {'field': 'assists_p90', 'type': 'quantitative'},
        'color': {'field': 'position', 'type': 'nominal'},
        'tooltip': [{"field": 'name', 'type': 'nominal'}, {'field': 'cost', 'type': 'quantitative'}, {'field': 'points', 'type': 'quantitative'}],
    },
    'width': 700,
    'height': 400,
})







#st.write(df)

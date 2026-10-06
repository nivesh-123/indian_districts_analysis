import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# set the page configuration
st.set_page_config(layout='wide',page_title='Indian districts analysis')

# import the dataframe
df = pd.read_parquet(r"data/final_df.parquet")
# add some important columns
df['literacy_rate'] = round((df['literate']/df['population'])*100)
df['sex_ratio'] = round((df['female']/df['male'])*1000)
df.info()

# define the layout of the app
st.sidebar.title('Analysing Indian Districts')

# getting list of states
list_of_states = sorted(df['state'].unique().tolist())
list_of_states.insert(0,'overall india')

# dropdown for state selection 
state = st.sidebar.selectbox('Select a state',list_of_states)

# dropdown for primary parameter selection
primary = st.sidebar.selectbox('Select primary parameter',df.columns.tolist()[5:])

# dropdown for secondary parameter selection
secondary = st.sidebar.selectbox('Select secondary parameter',df.columns.tolist()[5:])

# to automatically centre on india
mean_lat = df['latitude'].mean()
mean_lon = df['longitude'].mean()


# main routing section
if state == 'overall india':
    
    
    btn1 = st.sidebar.button('Perform Analysis')
    
    mean_lat = df['latitude'].mean()
    mean_lon = df['longitude'].mean()
    
    if btn1:
        st.write('primary parameter represented by size of marker')
        st.write('secondary parameter represented by color of marker')
        fig = px.scatter_map(df,lat='latitude',lon='longitude',size=primary,color=secondary,zoom=3.5,size_max=30,
                             map_style='carto-positron',height=800,width=1600,hover_name='district',
                             center={'lat':mean_lat,'lon':mean_lon})
        st.plotly_chart(fig,width='content',theme=None)
else:
    
    
    state_df = df.query('state == @state')
    
    mean_lat = state_df['latitude'].mean()
    mean_lon = state_df['longitude'].mean()
    
    btn2 = st.sidebar.button('Perform Analysis')
    if btn2:
        st.write('primary parameter represented by size of marker')
        st.write('secondary parameter represented by color of marker')
        fig1 = px.scatter_map(state_df,lat='latitude',lon='longitude',size=primary,
                              color=secondary,hover_name='district',zoom=5.5,size_max=30,
                              map_style='carto-positron',height=800,width=1600,
                              center={'lat':mean_lat,'lon':mean_lon})
        st.plotly_chart(fig1,theme=None,width='content')
# button for performing analysis


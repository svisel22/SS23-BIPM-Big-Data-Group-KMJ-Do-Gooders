import streamlit as st
#hints for debugging: https://awesome-streamlit.readthedocs.io/en/latest/vscode.html
import plotly.express as px
import pandas as pd
from utils.py import get_data

st.title('Happy Graphs')

st.write("Group KMJ Do-Gooders proudly presents: Happy Graphs. Graphs which make us optimistic.")


'''Preparation'''
# CHECK FOR US: Display a table with the cached data
#st.table(cached_data)
#df = st.table(cached_data)

# Read the worldinidicators dataframe
#df = data_processing()

'''Life Expectancy / Prediction'''
st.write("Life expectancy has been increasing for many years. It indicates that our world is still progressing and better off, than we might sometimes think. We invite you to explore more happy charts.")
# filter the df for life expectancy

# do line graph for life expectancy

# do predicition (LATER: for 3 gapminder indicators? on second website?)

# text for prediction


'''Selection of further indicators'''
# Search for an indicator by topic
# todo

# Multiselect widget for selecting indicators
countries = st.multiselect('Select one Indicator', df['value'].unique())
# LATER: compare Indicators --> for special charts?

# Multiselect widget for selecting countries or world
countries = st.multiselect('Select Countries', df['country'].unique())

'''
# Select Year with slider
df_year_min = df['year'].min()
df_year_max = df['year'].max()
year = st.slider('Select Year', min_value=int(df_year_min), max_value=int(df_year_max))
'''

'''Output'''
st.write("") #Indicator
st.write("This indicator is") #sourceNote
st.write("This indicator is") #getting better or worse?

#Line Graph
# Filter the dataframe based on the selected indicator and countries ##QUESTION: and year?
filtered_df = df[(df['value'] == str(value)) & (df['country'].isin(countries))]
# st.write(filtered_df.head())
df_for_plot = filtered_df.copy()

# Check if there are selected countries
if len(indicators) > 0:
    # Create line chart
    
    # Customize the chart layout
   
    # Display the chart
    st.plotly_chart()
else:
    # Display a message if no countries are selected
    st.write('Please select one or more indicators.')


#Explanation why it's getting better


#You can do this to help


#See data
filtered_df

#More interesting charts (combined dashboards)?

#spread the word
# api to automatically create posts
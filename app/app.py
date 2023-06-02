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

# do predicition

# text for prediction


'''Selection of further indicators'''
# Multiselect widget for selecting indicators #QUESTION: how many indicators should they be allowed to track? how compatible are indicators?
countries = st.multiselect('Select Countries', df['value'].unique())

# Multiselect widget for selecting countries
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
if len(countries) > 0:
    # Create line chart
    
    # Customize the chart layout
   
    # Display the chart
    st.plotly_chart()
else:
    # Display a message if no countries are selected
    st.write('Please select one or more countries.')


#Explanation why it's getting better


#You can do this to help


#See data
filtered_df


#spread the word
# api to automatically create posts
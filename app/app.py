import streamlit as st
#hints for debugging: https://awesome-streamlit.readthedocs.io/en/latest/vscode.html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from utils.py import get_data, get_indicator_reason, filter_projects

with open('../pred_lifeexp.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.title('Happy Graphs')

st.write("Group KMJ Do-Gooders proudly presents: Happy Graphs - Graphs which make us optimistic.")


'''Preparation'''
# Read the worldindicators dataframe
df = #ACTION


'''Life Expectancy'''
intro_text = """
Increasing life expectancy is often regarded as a measure of societal progress. It reflects advancements in public health, education, technology, and social development. It indicates that societies are investing in improving the well-being of their citizens and addressing societal challenges.

Below you see a line graph showcasing how life expectancy has been increasing for many years worldwide. Increasing life expectancy makes us optimistic that the world is better off than we might sometimes think. Therefore, we invite you to explore more charts to make us happy.

Sidenote: Please don't get fooled by the decline of life expectancy since 2019. Research suggests that this is due to the Covid-19 pandemic, which has induced the first decline in global life expectancy since World War II. For further information, please read the [Nature Article](https://www.nature.com/articles/s41562-022-01450-3).
"""
st.markdown(intro_text, unsafe_allow_html=True)

'''Show life expectancy world wide compared to German & Mexican'''
# User selection
life_expect_countries = df.columns.tolist()[1:]
st.write("Choose the countries you are interested in. The default countries are Mexico and Germany:")
selected_countries = st.multiselect("Select countries", life_expect_countries, default=['Mexico', 'Germany'])

# Set the chart title and axis labels
chart_title = "Life Expectancy"
x_label = "Year"
y_label = "Life Expectancy"

# Create a new figure and set the chart properties
fig, ax = plt.subplots()
ax.set_title(chart_title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_ylim(0, 100)

# Plot the data for selected countries
for country in selected_countries:
    country_data = df[['Year', country]]
    line_color = st.color_picker(f"Select color for {country}", key=country)
    ax.plot(country_data['Year'], country_data[country], label=country, color=line_color)

    # Add a tooltip to show year, country, and life expectancy on hover
    tooltip = ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                          bbox=dict(boxstyle="round", fc="white", edgecolor="gray"),
                          arrowprops=dict(arrowstyle="->"))
    tooltip.set_visible(False)

    def update_tooltip(event):
        if event.inaxes == ax:
            x = int(event.xdata)
            y = int(event.ydata)
            country = country_data.loc[country_data['Year'] == x].index[0]
            tooltip.xy = (x, y)
            tooltip.set_text(f"Year: {x}\nCountry: {country}\nLife Expectancy: {y}")
            tooltip.set_visible(True)
            fig.canvas.draw_idle()
        else:
            tooltip.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", update_tooltip)

# Add a legend
ax.legend()
# Display the chart
st.pyplot(fig)




'''Prediction with given features'''
#QUESTION: at the moment it's india, maybe rather have Germany? Or having sth like: Are you Mr Müller and then having presettings that should be near to him or also have the presettings for us three
st.write("Choose the country you life in to see your life expectancy:") #ACITON: adapt
#QUESTION: What kind of input do we need? Dropdowns or fields to write in?
#ACTION: adapt to make input one input with default settings #QUESTION: Where is male and female? or how old you are yourself? 
access_to_electricity = 100
armed_forces = 3.338855e+06
child_immunization = 100 
foreign_investm = 1
gdp_per_cap = 12000
measels_immunitization = 97
net_primary_income = 0 
perc_overweigth = 10
primary_school_completion = 100
rural_population = 50
trade_in_services = 15


data = {
    'access_to_electricity': access_to_electricity,
    'armed_forces' : armed_forces, 
    'child_immunization' : child_immunization, 
    'foreign_investm' : foreign_investm, 
    'gdp_per_cap' : gdp_per_cap,
    'measels_immunitization' : measels_immunitization,
    'net_primary_income' : net_primary_income, 
    'perc_overweigth' : perc_overweigth,
    'primary_school_completion' : primary_school_completion,
    'rural_population' : rural_population, 
    'trade_in_services'	: trade_in_services,
}
# transform them into a Dataframe
life_expect_df_test = pd.DataFrame(data, index=range(1))
# Predict using the loaded model
life_expect_df_pred = loaded_model.predict(life_expect_df_test)
# Set up the Streamlit app
st.write("Your predicted life expectancy is ", life_expect_df_pred[0], "years.")


'''Prediction with own features'''
st.write("Now it's your turn!  Below you can predict the life expectancy for a fictive country that has the features you select. Feel free to play around and find out what has which impact on life expectancy:") 
#ACTION: make to input
access_to_electricity = 100
armed_forces = 3.338855e+06
child_immunization = 100 
foreign_investm = 1
gdp_per_cap = 12000
measels_immunitization = 97
net_primary_income = 0 
perc_overweigth = 10
primary_school_completion = 100
rural_population = 50
trade_in_services = 15

data = {
    'access_to_electricity': access_to_electricity,
    'armed_forces' : armed_forces, 
    'child_immunization' : child_immunization, 
    'foreign_investm' : foreign_investm, 
    'gdp_per_cap' : gdp_per_cap,
    'measels_immunitization' : measels_immunitization,
    'net_primary_income' : net_primary_income, 
    'perc_overweigth' : perc_overweigth,
    'primary_school_completion' : primary_school_completion,
    'rural_population' : rural_population, 
    'trade_in_services'	: trade_in_services,
}

# transform them into a Dataframe
life_expect_df_test = pd.DataFrame(data, index=range(1))
# Predict using the loaded model
life_expect_df_pred = loaded_model.predict(life_expect_df_test)
# Set up the Streamlit app
st.write("In your fictive country a person has a predicted life expectancy of ", life_expect_df_pred[0], "years.")




'''Selection of further indicators for line charts'''
#ACTION: Search for an indicator by topic?

# Get the list of available indicators and countries
available_indicators = df.columns.tolist()[1:]
available_countries = df.columns.tolist()[1:]

# User selection
selected_indicator = st.selectbox("Select an indicator", available_indicators)
selected_countries = st.multiselect("Select countries", available_countries) #ACTION: make worldwide as a default
selected_year_range = st.slider("Select a year range", min_value=df['Year'].min(), max_value=df['Year'].max(),
                                value=(df['Year'].min(), df['Year'].max()), step=10)
selected_start_year, selected_end_year = selected_year_range

# Check if an indicator is selected
if not selected_indicator:
    st.text("Please choose an indicator to see its development.")
else:
    # Filter the data for selected countries and time period
    filtered_data = df[['Year'] + selected_countries]
    filtered_data = filtered_data[(filtered_data['Year'] >= selected_start_year) & (filtered_data['Year'] <= selected_end_year)]

    # Create a new figure and set the chart properties
    fig, ax = plt.subplots()
    ax.set_title(selected_indicator)
    ax.set_xlabel('Year')
    ax.set_ylabel(selected_indicator)
    ax.set_ylim(df[selected_indicator].min() - 10, df[selected_indicator].max() + 10)

    # Plot the data for selected countries
    for country in selected_countries:
        country_data = filtered_data[['Year', country]]
        line_color = st.color_picker(f"Select color for {country}", key=country)
        ax.plot(country_data['Year'], country_data[country], label=country, color=line_color)

        # Add a tooltip to show country and indicator value on hover
        tooltip = ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                              bbox=dict(boxstyle="round", fc="white", edgecolor="gray"),
                              arrowprops=dict(arrowstyle="->"))
        tooltip.set_visible(False)

        def update_tooltip(event):
            if event.inaxes == ax:
                x = int(event.xdata)
                y = int(event.ydata)
                tooltip.xy = (x, y)
                tooltip.set_text(f"{country}: {y}")
                tooltip.set_visible(True)
                fig.canvas.draw_idle()
            else:
                tooltip.set_visible(False)
                fig.canvas.draw_idle()

        fig.canvas.mpl_connect("motion_notify_event", update_tooltip)
    # Adjust x-axis scale based on the selected time period
    ax.set_xlim(selected_start_year, selected_end_year)
    # Add a legend
    ax.legend()


#ACTION: Let automatically analyse whether it's getting better? Or do we only make good indicators available?


'''Explanation why it's changing'''
df_year_max = selected_end_year
df_year_min = selected_start_year

answer = get_indicator_reason(selected_indicator, df_year_max, df_year_min, selected_countries) #ACTION: selected countries still has worldwide as a default in utils. we might need to change it or see whether it works
print(answer)



'''You can do this to help'''
#ACTION: write what should be written here
# Example usage
charity_country = ['Afghanistan', 'India']
charity_title = ''
charity_region = ''
charity_theme_name = 'Education'

projects = filter_projects(charity_country, charity_title, charity_region, charity_theme_name)
filtered_projects = filter_projects(country=country, title=charity_title, region=charity_region, theme_name=charity_theme_name)

if filtered_projects:
    for project in filtered_projects:
        print("Project Title:", project['title'])
        # Print other project details
else:
    print("No data found for the specified filters.")

#See data
filtered_df #ACTION

#More interesting charts (combined dashboards)?

#spread the word
# api to automatically create posts
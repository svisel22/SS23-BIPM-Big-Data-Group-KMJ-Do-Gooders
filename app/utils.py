import pandas as pd
import requests

def get_data(id_indicator, countries):

    url = 'https://api.worldbank.org/v2/'

    #create empty Dataframe where the result is stored
    df_complete = pd.DataFrame()
    for country in countries:

        # create a new url
        requesting_url = url + f'country/{(country)}/indicator/{id_indicator}''?format=json'
        response = requests.get(requesting_url)

        # Parse the JSON response and extract the data
        if response.ok:
            data = response.json()

        else:
            print('Error: Request failed with status', response.status_code)

        # Accessing values, dates, and countries
        values = []
        dates = []
        countries = []

        # Extract values, dates, and countries from the JSON data
        for item in data[1]:
            values.append(item['value'])
            dates.append(int(item['date']))
            countries.append(item['country']['value'])

        # create a dataframe out of that
        data = {'Country': countries, 'Date': dates, 'Value': values}
        df = pd.DataFrame(data)

        df_complete = pd.concat([df_complete, df], ignore_index=True)


    return(df_complete)
import plotly.express as px
from plotly.offline import plot
import pandas as pd
import urllib.request
import ssl

from urllib.request import urlopen
import json
ssl._create_default_https_context = ssl._create_unverified_context
response1 = urllib.request.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json')

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][0]



response = urllib.request.urlopen('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url, converters={'fips': lambda x: str(x)})

#Pick a state
df_Maryland = df[ df['state'] == "Maryland"]
last_date = df['date'].max()
df = df_Maryland[ df_Maryland['date'] == last_date]

print(df['cases'].sum())
print(df['deaths'].sum())


fig = px.choropleth(df, geojson=counties, locations='fips', color='cases',
                           color_continuous_scale="Viridis",
                           range_color=(0, 20000)
                          )

#Added for zoom and to set rest of map to invisible. 
fig.update_geos(fitbounds="locations", visible=False)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title_text='COVID-19 Cases From Each County in Maryland')
plot(fig)

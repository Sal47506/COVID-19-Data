import plotly.express as px
from plotly.offline import plot
import plotly.io as pio
import pandas as pd
import ssl
import urllib.request
from urllib.request import urlopen
import os

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
response1 = urllib.request.urlopen('https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv')



url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df = pd.read_csv(url, converters={'fips': lambda x: str(x)})

url = "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
df_abbrev = pd.read_csv(url)

last_date = df['date'].max()
df = df[ df['date'] == last_date]
print(df['cases'].sum())
df = df.groupby('state')['cases'].sum().to_frame()
df = pd.merge(df, df_abbrev, left_on=df.index, right_on='State')

fig = px.choropleth(df, locations=df['Abbreviation'], color=df['cases'],
                    locationmode="USA-states",
                    color_continuous_scale="hot",
                    range_color=(0, 4500000),
                    scope="usa"
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, geo=dict(bgcolor= '#4E5D6C',lakecolor='#4E5D6C'))

fig.show()


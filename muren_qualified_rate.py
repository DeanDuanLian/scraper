import pandas as pd
import re

Oct_urls = ['http://muren-economics.com/qualified-rate/rate{}-october/'.format(i) for i in range(2009,2018)]
Apr_urls = ['http://muren-economics.com/qualified-rate/rate{}-april/'.format(i) for i in range(2010,2018)]

all_urls = Oct_urls + Apr_urls
all_urls.sort()

df_all = pd.DataFrame()
for url in all_urls:
    df_url = pd.read_html(url)[0].rename({0:'name',1:'university'},axis=1)
    df_url['year'] = re.findall(r'\d+', url)[0]
    df_url['month'] = re.findall(r'-([oa]\S+)\/$', url)[0].capitalize()
    df_all = df_all.append(df_url)
df_all = df_all[['year', 'month', 'name', 'university']] 

df_all[df_all['name'].str.contains('励')]

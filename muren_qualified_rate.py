import pandas as pd
import re

Oct_urls = ['http://muren-economics.com/qualified-rate/rate{}-october/'.format(i) for i in range(2009,2018)]
Apr_urls = ['http://muren-economics.com/qualified-rate/rate{}-april/'.format(i) for i in range(2010,2018)]

df_Oct = pd.DataFrame()
for url in Oct_urls:
    df_url = pd.read_html(url)[0].rename({0:'name',1:'university'},axis=1)
    df_url['year'] = re.findall(r'\d+', url)[0]
    df_url['month'] = 'October' 
    df_Oct = df_Oct.append(df_url)

df_Apr = pd.DataFrame()
for url in Apr_urls:
    df_url = pd.read_html(url)[0].rename({0:'name',1:'university'},axis=1)
    df_url['year'] = re.findall(r'\d+', url)[0]
    df_url['month'] = 'April' 
    df_Apr = df_Apr.append(df_url)

df_all = pd.concat([df_Oct,df_Apr])
df_all = df_all[['year', 'month', 'name', 'university']].sort_values(by=['year','month','university'])

df_all[df_all['name'].str.contains('励')]

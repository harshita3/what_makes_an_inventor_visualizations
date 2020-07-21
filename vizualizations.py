#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt


# In[2]:


fp = "/Users/harshitabhatt/tl_2017_us_state/tl_2017_us_state.shp"


# In[3]:


map_df = gpd.read_file(fp)


# In[4]:


map_df.head()


# In[5]:


map_df.plot()


# In[6]:


plt.rcParams['figure.figsize'] = [300, 300] #height, width
map_df.plot()


# In[7]:


state_inv = pd.read_csv("/Users/harshitabhatt/inventor.csv")
state_inv.head()


# In[8]:



# join the geodataframe with the csv dataframe
merged = map_df.merge(state_inv, how='left', left_on="NAME", right_on="par_state")
merged.head()


# In[9]:


# set the value column that will be visualised
variable = 'inventor'
# set the range for the choropleth values
vmin, vmax = 0, 1
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title and annotation
ax.set_title('Rate of innovation', fontdict={'fontsize': '30', 'fontweight' : '6'})
ax.annotate('Raj Chetty', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='Blue')
# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
# add the colorbar to the figure
fig.colorbar(sm)
# create map
merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.9')


# In[ ]:





# In[2]:


import plotly.express as px  # Be sure to import express
state_invo = pd.read_csv("/Users/harshitabhatt/inventor.csv")
state_invo = state_invo.groupby(['par_stateabbrv'], as_index=False, sort=False).mean()
state_invo.head()
fig = px.choropleth(state_invo,  # Input Pandas DataFrame
                    locations="par_stateabbrv",  # DataFrame column with locations
                    color="inventor_g_m",  # DataFrame column with color values
                    hover_name="inventor_g_m", # DataFrame column hover info
                   # range_color=(0,0.013),
                    locationmode = 'USA-states') # Set to plot as US States
fig.update_layout(
    title_text = 'State Rankings', # Create a Title
    geo_scope='usa',  # Plot only the USA instead of globe
)

fig.show()  # 


# In[ ]:





# In[30]:


import plotly.express as px  # Be sure to import express
state_invo = pd.read_csv("/Users/harshitabhatt/inventor.csv")
state_invo = state_invo.groupby(['par_stateabbrv'], as_index=False, sort=False).mean()
state_invo.head()
fig = px.choropleth(state_invo,  # Input Pandas DataFrame
                    locations="par_stateabbrv",  # DataFrame column with locations
                    range_color = (0.001,0.0055),
                    color="inventor_g_f",  # DataFrame column with color values
                    hover_name="inventor_g_f", # DataFrame column hover info
                    locationmode = 'USA-states')# Set to plot as US States
                    
fig.update_layout(
    title_text = 'State Rankings', # Create a Title
    geo_scope='usa',  # Plot only the USA instead of globe
)
fig.show()  # 


# In[37]:





# In[2]:


import plotly.graph_objects as go
df = pd.read_csv('/Users/harshitabhatt/inventor.csv')
df = df.groupby(['par_stateabbrv'], as_index=False, sort=False).mean()
df.head()
fig = go.Figure(data=go.Scatter(
                x=df['par_stateabbrv'],
                y=df['inventor_g_m'],
                mode='markers',
                marker=dict(
                     color='rgb(255, 178, 102)',
                     size=10,
                     line=dict(
                        color='DarkSlateGrey',
                        width=1
                      )
               ))
    ,
                y=df['inventor_g_f'],
                mode='markers',
                marker=dict(
                     color='rgb(255, 178, 102)',
                     size=10,
                     line=dict(
                        color='DarkSlateGrey',
                        width=1
                      )
               )
))
fig.update_layout(
    title='Male inventor rate by state',
    xaxis_title='US-State',
    yaxis_title='Male innovation rate'
)
fig.show()


# In[ ]:





# In[3]:


patents_g=pd.read_csv("/Users/harshitabhatt/table_2a.csv")
patents_g.head()
inventor_rates= pd.read_csv("/Users/harshitabhatt/inventor.csv")
inventor_rates.head()
# join the geodataframe with the csv dataframe
merged = patents_g.merge(inventor_rates, how='left', left_on="stateabbrv", right_on="par_stateabbrv")
merged.head()


# In[4]:


import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(
                x=merged['par_stateabbrv'],
                y=df['inventor_g_m'],
                mode='markers',
                marker=dict(
                     color='rgb(255, 178, 102)',
                     size=10,
                     line=dict(
                        color='DarkSlateGrey',
                        width=1
                      )
               ),
      x=merged['par_stateabbrv'],
                y=df['inventor_g_f'],
                mode='markers',
                marker=dict(
                     color='rgb(255, 178, 102)',
                     size=10,
                     line=dict(
                        color='DarkSlateGrey',
                        width=1
                      )
               )
))
fig.update_layout(
    title='Male inventor rate by state',
    xaxis_title='US-State',
    yaxis_title='Male innovation rate'
)
fig.show()


# In[6]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go
df = pd.read_csv('/Users/harshitabhatt/inventor.csv')
df = df.groupby(['par_stateabbrv'], as_index=False, sort=False).mean()
df.head()
fig = make_subplots(rows=1, cols=2, 
                    shared_xaxes=True, 
                    shared_yaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=("Men", "Women"))

fig.add_trace(go.Scatter(go.Scatter(
                x=df['par_stateabbrv'],
                y=df['inventor_g_m'],
                mode='markers',
                marker=dict(
                     color='rgb(255, 178, 102)',
                     size=10,
                     line=dict(
                        color='DarkSlateGrey',
                        width=1
                      ),
               ))),row=1, col=1)



fig.add_trace(go.Scatter(go.Scatter(
                x=df['par_stateabbrv'],
                y=df['inventor_g_f'],
                mode='markers',
                marker=dict(
                     color='rgb(255, 178, 102)',
                     size=10,
                     line=dict(
                        color='DarkSlateGrey',
                        width=1
                      ),
               ))),row=1, col=2)


fig.update_layout(height=900, width=2000,
                  title_text="Innovation Rates between Men and Women")
fig.show()


# In[ ]:





# In[53]:


import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('/Users/harshitabhatt/inventor.csv')

fig = px.scatter(df.query("Country=='USA'"), x="poor_share2010", y="inventor", hover_name="par_state", color_discrete_sequence=px.colors.qualitative.Safe, log_x=False, size_max=60)
fig.show()


# In[62]:


fig = px.scatter(df, x="share_white2000", y="inventor",color_discrete_sequence=px.colors.qualitative.Safe)
fig.show()




# In[61]:


fig = px.scatter(df, x="poor_share2010", y="inventor")
fig.show()

fig = px.scatter(df, x= "share_white2000", y="inventor")
fig.show()


# In[59]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
school_district.head()
fig = px.scatter(school_district, x="poor_share2000", y="inventor")
fig.show()


# In[62]:


fig = px.scatter(school_district, x="share_black2000", y="poor_share2000")
fig.show()


# In[ ]:


fig = px.scatter(school_district, x="share_black2000", y="poor_share2000")
fig.show()


# In[65]:


fig = px.scatter(school_district, x="share_black2000", y="emp2000")
fig.show() 


# In[159]:


fig = px.scatter(school_district, x="share_white2000", y="emp2000")
fig.show() 


# In[69]:


fig = px.scatter(school_district, x="job_growth_1990_2010", y="inventor")
fig.show() 


# In[70]:


fig = px.scatter(school_district, y="job_growth_1990_2010", x="share_black2000")
fig.show() 


# In[71]:


fig = px.scatter(school_district, y="inventor", x="emp2000")
fig.show() 


# In[80]:


fig = px.scatter(school_district, y="inventor", x="job_density_2013",log_x=True)
fig.show() 


# In[85]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="inventor", x = "num_inst_pc")
fig.show()


# In[90]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="inventor", x = "crime_violent")
fig.show()


# In[91]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="inventor", x = "gini")
fig.show()


# In[95]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="gini", x = "share_black2000",log_y=True)
fig.show()


# In[100]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="inventor", x = "scap_ski90pcm", log_x=True)
fig.show()


# In[150]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, x="share_black2000", y = "scap_ski90pcm", log_x=True)
fig.show()


# In[148]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, x="share_white2000", y = "scap_ski90pcm", log_x=True)
fig.show()


# In[ ]:





# In[151]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, x="share_asian2000", y = "scap_ski90pcm", log_x=True)
fig.show()


# In[146]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="inventor", x = "Income Growth 2000-2006/10", log_x=True)
fig.show()


# In[127]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="School Expenditure per student", x = "share_black2000")
fig.show()


# In[160]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, x="School Expenditure per student", y = "inventor")
fig.show()


# In[155]:


import plotly.express as px
school_district = pd.read_csv("/Users/harshitabhatt/cz_conditions.csv")
fig=px.scatter(school_district, y="Local Government Expenditures per Capita", x = "share_black2000")
fig.show()



# In[163]:


import plotly.express as px  # Be sure to import express
state_invo = pd.read_csv("/Users/harshitabhatt/inventor.csv")
state_invo = state_invo.groupby(['par_stateabbrv'], as_index=False, sort=False).mean()
state_invo.head()
fig = px.choropleth(state_invo,  # Input Pandas DataFrame
                    locations="par_stateabbrv",  # DataFrame column with locations
                    range_color = (-0.001,0.004),
                    color="male-female",  # DataFrame column with color values
                    hover_name="inventor", # DataFrame column hover info
                    locationmode = 'USA-states')# Set to plot as US States
                    
fig.update_layout(
    title_text = 'State Rankings', # Create a Title
    geo_scope='usa',  # Plot only the USA instead of globe
)
fig.show()  # 


# In[ ]:





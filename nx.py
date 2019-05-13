import networkx as nx 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
%matplotlib inline

df_net = pd.read_csv(r'F:\PyData\green201601testsmall.csv')
df_net = df_net[['ID','Pickup_longitude', 'Pickup_latitude','Dropoff_longitude','Dropoff_latitude']]
#df_net.dropna(inplace=True)
df_net['count'] = 0
df_net2 = df_net.copy()
df_net2['Op'] = df_net2['ID'].apply(lambda x: 'O' + str(x))
df_net2['Dp'] = df_net2['ID'].apply(lambda x: 'D' + str(x))
df_net2.reset_index(inplace=True)
dic = {}
for i in range(len(df_net2)):
    dic[df_net2['Op'][i]] = list([df_net2['Pickup_longitude'][i],df_net2['Pickup_latitude'][i]])
    dic[df_net2['Dp'][i]] = list([df_net2['Dropoff_longitude'][i],df_net2['Dropoff_latitude'][i]])
# plt.figure(figsize=(50,50))    
fig, ax = plt.subplots(figsize=(50,50))
country = gpd.GeoDataFrame.from_file(r'C:\Users\Administrator\Desktop\taxizonecut239nx.shp')
country.plot(ax=ax,color='green',alpha=0.5,edgecolor='purple')


#country02 = gpd.GeoDataFrame.from_file(r'D:\Vgis_data\Multi-Source-Data\data_ana\river1.shp')
#country02.plot(ax=ax,color='blue',alpha=0.5)  
#country03 = gpd.GeoDataFrame.from_file(r'D:\Vgis_data\Multi-Source-Data\data_ana\river2.shp')
#country03.plot(ax=ax,color='blue',alpha=0.5) 


GA = nx.from_pandas_edgelist(df_net2, source="Op", target="Dp", edge_attr='count')
pos = dic
edges = GA.edges() 
nx.draw(GA,pos, with_labels=False, node_size=0, alpha=0.01,font_family='SimHei')
nx.draw_networkx_edges(GA, pos, width=0.5, alpha=0.01)
plt.savefig(r'C:\Users\Administrator\Desktop\fig_nj.jpg',dpi = 300)
